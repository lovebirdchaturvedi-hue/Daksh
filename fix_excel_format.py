import pandas as pd
import re
import os

files_to_process = [
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS_INTERNATIONAL_ONLY.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS_INTERNATIONAL_ONLY.xlsx"
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
    target_code = country_codes.get(country)
    digits_only = re.sub(r'[^\d+]', '', phone_str)
    
    if not target_code:
        return f" {digits_only}" if digits_only else f" {phone_str}"

    target_code_numeric = target_code.replace("+", "")
    
    if digits_only.startswith(target_code):
        return f" {digits_only}"
        
    if digits_only.startswith(target_code_numeric) and len(digits_only) > len(target_code_numeric) + 5:
        return f" +{digits_only}"
        
    if digits_only.startswith("00" + target_code_numeric):
        return f" +{digits_only[2:]}"
        
    if digits_only.startswith("+"):
        return f" {digits_only}"
        
    local_number = re.sub(r'^0+', '', digits_only)
    
    return f" {target_code}{local_number}"

for file_path in files_to_process:
    print(f"Fixing formatting in {file_path}")
    try:
        df = pd.read_excel(file_path)
        
        if "Original_Phone" in df.columns:
            df["Phone"] = df.apply(lambda row: clean_phone(row["Original_Phone"], row.get("Country", "")), axis=1)
            
        output_path = file_path.replace(".xlsx", "_V2.xlsx")
        df.to_excel(output_path, index=False)
        print(f"Successfully fixed and saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")
