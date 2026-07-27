import pandas as pd
import phonenumbers
import pycountry
import time

start = time.time()
print("Loading data...")
buyers_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS 2026.xlsx'
exporters_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL EXPORTERS 2026.xlsx'

buyers = pd.read_excel(buyers_path)
exporters = pd.read_excel(exporters_path)

custom_mapping = {
    'USA': 'US', 'United States': 'US', 'UK': 'GB', 'UAE': 'AE',
    'United Arab Emirates': 'AE', 'Russia': 'RU', 'South Korea': 'KR',
    'Vietnam': 'VN', 'Iran': 'IR', 'Syria': 'SY', 'Taiwan': 'TW',
    'Turkey': 'TR', 'Turkiye': 'TR', "Cote d'Ivoire": 'CI',
    'Ivory Coast': 'CI', 'Tanzania': 'TZ', 'Venezuela': 'VE',
    'Bolivia': 'BO', 'Czech Republic': 'CZ', 'Czechia': 'CZ'
}

print("Building unique country map (Fast Mode)...")
all_countries = pd.concat([buyers['Country'], exporters['Country']]).dropna().unique()

country_to_code = {}
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
    
    prefix = ""
    if iso:
        for code, regions in phonenumbers.COUNTRY_CODE_TO_REGION_CODE.items():
            if iso in regions:
                prefix = f"+{code}"
                break
    country_to_code[c] = prefix

print("Vectorizing phone number formatting...")
def fast_format(row):
    p = str(row['Phone']).strip()
    if p == "nan" or p == "": return ""
    if p.startswith("+"): return p
    c = row['Country']
    if pd.notna(c) and c in country_to_code and country_to_code[c]:
        # Don't prepend if it already starts with the country code digits
        prefix = country_to_code[c]
        if not p.startswith(prefix.replace("+", "")):
            return f"{prefix} {p}"
    return p

buyers['Phone'] = buyers.apply(fast_format, axis=1)
exporters['Phone'] = exporters.apply(fast_format, axis=1)

print("Extracting Special Commodities...")
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

print("Saving final files...")
buyers.to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE BUYERS.xlsx', index=False)
exporters.to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE EXPORTERS.xlsx', index=False)
pd.concat([buyers, exporters], ignore_index=True).to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE MASTER.xlsx', index=False)

onion_buyers.to_excel(r'C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS.xlsx', index=False)
cow_buyers.to_excel(r'C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS.xlsx', index=False)

print(f"All done in {time.time() - start:.2f} seconds!")
