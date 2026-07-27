import pandas as pd
import re

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

def clean_phone_bulletproof(phone, country):
    if pd.isna(phone) or str(phone).strip() == "":
        return phone
    
    phone_str = str(phone).strip()
    target_code = country_codes.get(country)
    digits_only = re.sub(r'[^\d]', '', phone_str) # only digits
    
    if not target_code:
        if "+" in phone_str:
            return phone_str
        return digits_only if digits_only else phone_str

    target_code_numeric = target_code.replace("+", "")
    
    if digits_only.startswith(target_code_numeric):
        local_number = digits_only[len(target_code_numeric):]
        local_number = re.sub(r'^0+', '', local_number)
        if local_number:
            return f"{target_code} {local_number}"
        else:
            return f"{target_code}"
            
    if digits_only.startswith("00" + target_code_numeric):
        local_number = digits_only[2 + len(target_code_numeric):]
        local_number = re.sub(r'^0+', '', local_number)
        if local_number:
            return f"{target_code} {local_number}"
        else:
            return f"{target_code}"
            
    local_number = re.sub(r'^0+', '', digits_only)
    if local_number:
        return f"{target_code} {local_number}"
    else:
        return f"{target_code}"

for file_path in files_to_process:
    print(f"Applying bulletproof formatting to {file_path}")
    try:
        df = pd.read_excel(file_path)
        
        if "Original_Phone" in df.columns:
            df["Phone"] = df.apply(lambda row: clean_phone_bulletproof(row["Original_Phone"], row.get("Country", "")), axis=1)
        else:
            df["Phone"] = df.apply(lambda row: clean_phone_bulletproof(row["Phone"], row.get("Country", "")), axis=1)
            
        output_path = file_path.replace(".xlsx", "_V3.xlsx")
        
        # Write to excel using standard engine
        df.to_excel(output_path, index=False)
        print(f"Successfully saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")
