import pandas as pd
import phonenumbers
import pycountry
import time
import os

buyers_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS 2026.xlsx'
exporters_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL EXPORTERS 2026.xlsx'

print("Loading data...")
df1 = pd.read_excel(buyers_path)

custom_mapping = {
    'USA': 'US', 'United States': 'US', 'UK': 'GB', 'UAE': 'AE',
    'United Arab Emirates': 'AE', 'Russia': 'RU', 'South Korea': 'KR',
    'Vietnam': 'VN', 'Iran': 'IR', 'Syria': 'SY', 'Taiwan': 'TW',
    'Turkey': 'TR', 'Turkiye': 'TR', "Cote d'Ivoire": 'CI',
    'Ivory Coast': 'CI', 'Tanzania': 'TZ', 'Venezuela': 'VE',
    'Bolivia': 'BO', 'Czech Republic': 'CZ', 'Czechia': 'CZ'
}

print("Building unique country map...")
all_countries = df1['Country'].dropna().unique()
country_to_iso = {}
for c in all_countries:
    c_str = str(c).strip()
    c_upper = c_str.upper()
    iso = None
    if c_upper in custom_mapping: iso = custom_mapping[c_upper]
    elif c_str in custom_mapping: iso = custom_mapping[c_str]
    else:
        try: iso = pycountry.countries.lookup(c_str).alpha_2
        except LookupError:
            try:
                matches = pycountry.countries.search_fuzzy(c_str)
                if matches: iso = matches[0].alpha_2
            except: pass
    country_to_iso[c] = iso

def clean_phone(row):
    p = str(row['Phone']).strip()
    if p == "nan" or p == "": return ""
    c = row['Country']
    iso = country_to_iso.get(c)
    
    # Try parsing
    try:
        # If the number has a +, phonenumbers will use it to determine country
        # Otherwise it uses 'iso' as default
        parsed = phonenumbers.parse(p, iso)
        if phonenumbers.is_possible_number(parsed):
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except:
        pass
        
    # If parsing failed, just return the original number (without blindly prepending country code)
    # But clean it up a bit
    p = ''.join(ch for ch in p if ch.isdigit() or ch == '+' or ch == '-' or ch == ' ' or ch == '(' or ch == ')')
    return p.strip()

print("Applying phone cleanup...")
start = time.time()
sample = df1.head(10000).copy()
sample['Clean_Phone'] = sample.apply(clean_phone, axis=1)
print(f"10000 rows took {time.time() - start:.2f} seconds")
print(sample[['Country', 'Phone', 'Clean_Phone']].head(20))
