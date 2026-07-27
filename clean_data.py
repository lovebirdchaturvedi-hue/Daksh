import pandas as pd
import phonenumbers
import pycountry

print("Loading data for cleaning...")
buyers_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS 2026.xlsx'
exporters_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL EXPORTERS 2026.xlsx'

buyers = pd.read_excel(buyers_path)
exporters = pd.read_excel(exporters_path)

# Custom mapping for common country names that pycountry might struggle with
custom_mapping = {
    'USA': 'US',
    'United States': 'US',
    'UK': 'GB',
    'UAE': 'AE',
    'United Arab Emirates': 'AE',
    'Russia': 'RU',
    'South Korea': 'KR',
    'Vietnam': 'VN',
    'Iran': 'IR',
    'Syria': 'SY',
    'Taiwan': 'TW',
    'Turkey': 'TR',
    'Turkiye': 'TR',
    'Cote d\'Ivoire': 'CI',
    'Ivory Coast': 'CI',
    'Tanzania': 'TZ',
    'Venezuela': 'VE',
    'Bolivia': 'BO',
    'Czech Republic': 'CZ',
    'Czechia': 'CZ'
}

def get_iso_code(country_name):
    if not isinstance(country_name, str):
        return None
    name = country_name.strip()
    if name.upper() in custom_mapping:
        return custom_mapping[name.upper()]
    if name in custom_mapping:
        return custom_mapping[name]
    
    try:
        # Try exact match
        return pycountry.countries.lookup(name).alpha_2
    except LookupError:
        # Try fuzzy search
        try:
            matches = pycountry.countries.search_fuzzy(name)
            if matches:
                return matches[0].alpha_2
        except:
            return None
    return None

def format_phone(phone, country_name):
    if not isinstance(phone, str) or str(phone).strip() == "" or pd.isna(phone):
        return phone
    
    # Clean the phone string
    phone = str(phone).strip()
    # If it already starts with +, return it as is or try to format it
    iso_code = get_iso_code(country_name)
    
    try:
        if phone.startswith('+'):
            parsed = phonenumbers.parse(phone, None)
        else:
            if not iso_code:
                return phone
            parsed = phonenumbers.parse(phone, iso_code)
            
        if phonenumbers.is_valid_number(parsed) or phonenumbers.is_possible_number(parsed):
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except phonenumbers.NumberParseException:
        pass
    
    return phone

print("Standardizing phone numbers for buyers...")
buyers['Phone'] = buyers.apply(lambda row: format_phone(row['Phone'], row['Country']), axis=1)

print("Standardizing phone numbers for exporters...")
exporters['Phone'] = exporters.apply(lambda row: format_phone(row['Phone'], row['Country']), axis=1)

print("Saving final formatted files...")
buyers_out = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE BUYERS.xlsx'
exporters_out = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE EXPORTERS.xlsx'
combined_out = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE MASTER.xlsx'

buyers.to_excel(buyers_out, index=False)
exporters.to_excel(exporters_out, index=False)

combined = pd.concat([buyers, exporters], ignore_index=True)
combined.to_excel(combined_out, index=False)

print(f"Done! Cleaned Buyers: {len(buyers)}, Cleaned Exporters: {len(exporters)}, Master: {len(combined)}")
