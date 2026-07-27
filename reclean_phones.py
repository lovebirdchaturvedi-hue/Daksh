import pandas as pd
import phonenumbers
import multiprocessing as mp
import time

def clean_phone_chunk(df):
    custom_mapping = {
        'USA': 'US', 'UNITED STATES': 'US', 'UK': 'GB', 'UAE': 'AE',
        'UNITED ARAB EMIRATES': 'AE', 'RUSSIA': 'RU', 'SOUTH KOREA': 'KR',
        'VIETNAM': 'VN', 'IRAN': 'IR', 'SYRIA': 'SY', 'TAIWAN': 'TW',
        'TURKEY': 'TR', 'TURKIYE': 'TR', "COTE D'IVOIRE": 'CI',
        'IVORY COAST': 'CI', 'TANZANIA': 'TZ', 'VENEZUELA': 'VE',
        'BOLIVIA': 'BO', 'CZECH REPUBLIC': 'CZ', 'CZECHIA': 'CZ',
        'INDIA': 'IN'
    }

    def process_val(p, c):
        p = str(p).strip()
        if p == "nan" or p == "": return ""
        
        # If it was blindly prepended with +91 by my previous script, let's strip it to re-evaluate
        # Wait, the previous script SAVED to the APD GLOBAL files, but here I am reading from APD GLOBAL EXPORTERS 2026.xlsx!
        # Wait, the previous script OVERWROTE those files!
        if p.startswith("+91 ") and len(p) > 13:
            # Let's see if the remaining part is valid on its own, if so it might have been a US number
            pass # Actually, parsing +91 612-963-4676 will fail in phonenumbers because it's not a valid IN number.

        c = str(c).upper().strip()
        iso = custom_mapping.get(c, 'IN')
        
        def try_parse(num, region):
            try:
                parsed = phonenumbers.parse(num, region)
                if phonenumbers.is_possible_number(parsed) and phonenumbers.is_valid_number(parsed):
                    return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            except: pass
            
            try:
                for match in phonenumbers.PhoneNumberMatcher(num, region):
                    if phonenumbers.is_valid_number(match.number):
                        return phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            except: pass
            return None
            
        # Try original
        res = try_parse(p, iso)
        if res: return res
        
        # If it starts with +91 but is invalid (e.g. +91 612-963-4676), strip +91 and try 'US' or 'iso'
        if p.startswith("+91"):
            stripped = p[3:].strip()
            res2 = try_parse(stripped, iso)
            if res2: return res2
            res3 = try_parse(stripped, 'US')
            if res3: return res3
            
        # Fallback to US
        res4 = try_parse(p, 'US')
        if res4: return res4
            
        # If totally invalid, return just digits if it's garbage
        # If it was +91 15791331, strip the +91 so we just show the raw garbage
        if p.startswith("+91"):
            raw = p[3:].strip()
            if len(raw) < 9: return raw
            return raw

        return p # Give up, return original

    df['Phone'] = df.apply(lambda row: process_val(row['Phone'], row['Country']), axis=1)
    return df

if __name__ == '__main__':
    start = time.time()
    buyers_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS 2026.xlsx'
    exporters_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL EXPORTERS 2026.xlsx'
    
    print("Loading Original Data...")
    buyers = pd.read_excel(buyers_path)
    exporters = pd.read_excel(exporters_path)
    
    print("Parallel processing...")
    cpu_cores = mp.cpu_count()
    
    # Split buyers
    b_chunks = [buyers[i::cpu_cores] for i in range(cpu_cores)]
    with mp.Pool(cpu_cores) as pool:
        b_results = pool.map(clean_phone_chunk, b_chunks)
    buyers = pd.concat(b_results)
    
    # Split exporters
    e_chunks = [exporters[i::cpu_cores] for i in range(cpu_cores)]
    with mp.Pool(cpu_cores) as pool:
        e_results = pool.map(clean_phone_chunk, e_chunks)
    exporters = pd.concat(e_results)
    
    print("Re-Extracting Specials...")
    search_cols = ['Commodity', 'Business Name', 'Source File']
    buyers_search = buyers.copy()
    for col in search_cols:
        if col in buyers_search.columns: buyers_search[col] = buyers_search[col].fillna("").astype(str).str.lower()
        else: buyers_search[col] = ""
    onion_mask = buyers_search['Commodity'].str.contains('onion') | buyers_search['Business Name'].str.contains('onion') | buyers_search['Source File'].str.contains('onion')
    onion_buyers = buyers[onion_mask]
    cow_mask = (buyers_search['Commodity'].str.contains('cow dung') | buyers_search['Commodity'].str.contains('fertilizer') | 
                buyers_search['Business Name'].str.contains('fertilizer') | buyers_search['Source File'].str.contains('cow dung') | 
                buyers_search['Source File'].str.contains('fertilizer'))
    cow_buyers = buyers[cow_mask]
    
    print("Saving...")
    buyers.to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE BUYERS.xlsx', index=False)
    exporters.to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE EXPORTERS.xlsx', index=False)
    
    # Master
    pd.concat([buyers, exporters], ignore_index=True).to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE MASTER.xlsx', index=False)
    onion_buyers.to_excel(r'C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS.xlsx', index=False)
    cow_buyers.to_excel(r'C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS.xlsx', index=False)
    
    print(f"Done in {time.time()-start:.2f}s")
