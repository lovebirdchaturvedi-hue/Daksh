import pandas as pd

file_path = r"C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS Final.xlsx"

leads = [
    ("Eden Val Trading LLC", "04 2354793"),
    ("Elite Food Supplements Manufacturing Co LLC", "052 5064269"),
    ("GAJS Foodstuff Trading LLC", "04 2944715"),
    ("Ghuloom Hussain Ali Naqi Trading", "04 2263574"),
    ("Global Green Food Trading LLC", "04 8829299"),
    ("GRK Food Industry LLC", "052 7108880"),
    ("High Volume Food Stuff Trading LLC", "04 2979189"),
    ("Honest Origin Good Foodstuff Trading LLC", "050 9569939"),
    ("Inox Ventures FZCO", "052 1504512"),
    ("Kahraman Dubai General Trading Co", "04 2251048"),
    ("Kamaki Foodstuff Trading LLC", "04 5687185"),
    ("Kinda Food Stuff Trading LLC", "04 2352515"),
    ("Ridhu Foodstuff Trading LLC", "055 8612680"),
    ("Meridian PF General Trading LLC", "04 5644106"),
    ("Abdul Hamid Al Reza Co", "04 2264775"),
    ("Al Maya Trading Co LLC", "04 3474843"),
    ("Alwan Dubai Mill", "04 2671621"),
    ("Brooks Trading Company LLC", "04 2268791"),
    ("Dhirani Foodstuff Company LLC", "04 2265211"),
    ("Dow Alhaya Flour Mill LLC", "058 5832019"),
    ("Leoste Global LLC FZ", "04 4335655"),
    ("MKK Trade", "04 3281988"),
    ("Najmat Al Abeer Trading LLC", "04 2266854"),
    ("Naseeri General Trading Company LLC", "04 2264043"),
    ("Nawab Foodstuff Trading LLC", "055 3567625"),
    ("Noor Albarakah Goods Wholesalers LLC", "04 5527207"),
    ("Nutty Nuts Foodstuff Factory (LLC)", "04 3479905"),
    ("Prince Sweets", "04 3371766"),
    ("Rabiah Trading", "04 3203744"),
    ("Rashwell Company (LLC)", "04 2262855"),
    ("Rospand Global Techno Services", "052 7542126"),
    ("Royal Golden General Trading", "04 2980073"),
    ("Sakhi Khan International Foodstuff Trading LLC", "050 5085004"),
    ("Sher Muhammed Trading", "04 2252246"),
    ("Yousify General Trading Co. LLC", "04 3309641"),
    ("Zuva Foodstuff Trading LLC", "056 6529222"),
    ("Spices Garden Cafe", "04 43510195"),
]

# Create a dataframe for the new leads
new_rows = []
for name, phone in leads:
    # Format the phone number with the country code
    # Example: "04 3201112" -> " +971 4 3201112"
    clean_num = phone.replace(" ", "")
    if clean_num.startswith("0"):
        clean_num = clean_num[1:]
    
    formatted_phone = f" +971 {clean_num}"
    
    new_rows.append({
        'Source File': 'Custom Added',
        'Type': 'Buyer',
        'Country': 'UAE',
        'Commodity': 'Spices',
        'Company Name': name,
        'Phone': formatted_phone,
        'Original_Phone': phone
    })

new_df = pd.DataFrame(new_rows)

print(f"Reading existing file: {file_path}")
try:
    df = pd.read_excel(file_path)
    # Concatenate the old and new dataframes
    combined_df = pd.concat([df, new_df], ignore_index=True)

    # Save back to the file using pandas
    print(f"Saving {len(combined_df)} total records...")
    combined_df.to_excel(file_path, index=False)
    print(f"Successfully added {len(new_df)} new UAE spices leads with +971 country code!")
except Exception as e:
    print(f"Error: {e}")
