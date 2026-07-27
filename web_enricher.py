import pandas as pd
import phonenumbers
from duckduckgo_search import DDGS
import time
import os
import random

def get_country_iso(country_name):
    custom_mapping = {
        'USA': 'US', 'UNITED STATES': 'US', 'UK': 'GB', 'UAE': 'AE',
        'UNITED ARAB EMIRATES': 'AE', 'RUSSIA': 'RU', 'SOUTH KOREA': 'KR',
        'VIETNAM': 'VN', 'IRAN': 'IR', 'SYRIA': 'SY', 'TAIWAN': 'TW',
        'TURKEY': 'TR', 'TURKIYE': 'TR', "COTE D'IVOIRE": 'CI',
        'IVORY COAST': 'CI', 'TANZANIA': 'TZ', 'VENEZUELA': 'VE',
        'BOLIVIA': 'BO', 'CZECH REPUBLIC': 'CZ', 'CZECHIA': 'CZ',
        'INDIA': 'IN'
    }
    return custom_mapping.get(str(country_name).upper().strip(), 'IN')

def extract_phone(text, iso):
    if not text: return None
    try:
        # Check strict first
        for match in phonenumbers.PhoneNumberMatcher(text, iso):
            if phonenumbers.is_valid_number(match.number):
                return phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except: pass
    
    try:
        # Fallback to US
        for match in phonenumbers.PhoneNumberMatcher(text, "US"):
            if phonenumbers.is_valid_number(match.number):
                return phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except: pass
    return None

def process_file(file_path):
    print(f"Processing {file_path}...")
    df = pd.read_excel(file_path)
    
    if 'Original_Phone' not in df.columns:
        df['Original_Phone'] = df['Phone']
        
    save_path = file_path.replace(".xlsx", "_ENRICHED.xlsx")
    
    with DDGS() as ddgs:
        for index, row in df.iterrows():
            phone = str(row['Phone']).strip()
            
            # If phone is missing, "nan", or less than 9 chars (invalid)
            if phone == "nan" or phone == "" or len(phone.replace("+", "").replace(" ", "")) < 9:
                company = str(row['Business Name']).strip()
                country = str(row['Country']).strip()
                if company and company != "nan":
                    query = f'"{company}" "{country}" contact phone number'
                    print(f"Searching: {query}")
                    try:
                        results = list(ddgs.text(query, max_results=3))
                        text_corpus = " ".join([r['body'] for r in results])
                        
                        iso = get_country_iso(country)
                        found_phone = extract_phone(text_corpus, iso)
                        
                        if found_phone:
                            print(f"  -> FOUND: {found_phone}")
                            df.at[index, 'Phone'] = found_phone
                            
                        # Respect rate limits
                        time.sleep(random.uniform(2, 4))
                    except Exception as e:
                        print(f"Search failed for {company}: {e}")
                        time.sleep(10) # Backoff if rate limited
            
            if index % 50 == 0 and index > 0:
                print(f"Autosaving {index}/{len(df)}...")
                df.to_excel(save_path, index=False)
                
    df.to_excel(save_path, index=False)
    print(f"Finished {file_path}!")

if __name__ == "__main__":
    files = [
        r'C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS.xlsx',
        r'C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS.xlsx'
    ]
    for f in files:
        process_file(f)
