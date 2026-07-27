import pandas as pd
import re
import os

files_to_process = [
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS.xlsx"
]

country_codes = {
    "India": "+91",
    "USA": "+1",
    "Canada": "+1",
    "USA/Canada": "+1",
    "UAE": "+971",
    "Malaysia": "+60",
    "Australia": "+61",
    "Singapore": "+65",
    "UK": "+44",
    "Turkey": "+90",
    "Russia": "+7",
    "Vietnam": "+84",
    "Netherlands": "+31",
    "Egypt": "+20",
    "South Korea": "+82",
    "Germany": "+49",
    "Philippines": "+63",
    "Brazil": "+55",
    "Japan": "+81",
    "Bangladesh": "+880",
    "China": "+86",
    "Saudi Arabia": "+966"
}

def clean_phone(phone, country):
    if pd.isna(phone) or str(phone).strip() == "":
        return phone
    
    phone_str = str(phone).strip()
    
    # If country is not in our list, just return the original but cleaned a bit
    target_code = country_codes.get(country)
    
    # Remove all non-numeric except '+'
    digits_only = re.sub(r'[^\d+]', '', phone_str)
    
    if not target_code:
        return digits_only if digits_only else phone_str

    target_code_numeric = target_code.replace("+", "")
    
    # If the phone already starts with the correct +, return it
    if digits_only.startswith(target_code):
        return digits_only
        
    # If it starts with the correct code without +, add the +
    if digits_only.startswith(target_code_numeric) and len(digits_only) > len(target_code_numeric) + 5:
        return "+" + digits_only
        
    # If it starts with 00 followed by the correct code
    if digits_only.startswith("00" + target_code_numeric):
        return "+" + digits_only[2:]
        
    # If it starts with a different +, we assume it's an international number that is correct as is, 
    # OR we replace it? The user said "Make sure every number starting from their coutry code".
    # If it has a +, let's assume it's already an international format. But if it doesn't match the country, maybe it's an error.
    # To be safe, if it starts with + and doesn't match, we still return it (could be a foreigner living there).
    if digits_only.startswith("+"):
        return digits_only
        
    # If it doesn't start with +, we assume it's a local number and prepend the country code.
    # Remove leading zeros before prepending (common for local numbers in many countries)
    local_number = re.sub(r'^0+', '', digits_only)
    
    return f"{target_code}{local_number}"

for file_path in files_to_process:
    print(f"Processing {file_path}...")
    try:
        df = pd.read_excel(file_path)
        
        original_count = len(df)
        print(f"Original rows: {original_count}")
        
        if "Phone" in df.columns:
            # Keep original for reference if user wants it
            if "Original_Phone" not in df.columns:
                df["Original_Phone"] = df["Phone"]
                
            df["Phone"] = df.apply(lambda row: clean_phone(row["Original_Phone"], row.get("Country", "")), axis=1)
            
        # Save as _FIXED.xlsx
        output_path = file_path.replace(".xlsx", "_FIXED.xlsx")
        df.to_excel(output_path, index=False)
        print(f"Successfully saved clean file to {output_path} with {len(df)} rows.")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

