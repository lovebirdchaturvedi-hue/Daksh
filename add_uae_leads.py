import pandas as pd

file_path = r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS Final.xlsx"

leads = [
    ("Shokri Hassan Trading Company LLC", "04 3201112"),
    ("South Link International Foodstuff", "04 3330499"),
    ("Veeraytan General Trading LLC", "04 3409738"),
    ("Yalda Trading Company LLC", "054 3658181"),
    ("Fruits Garden Trading LLC", "04 3334629"),
    ("Fruits Trading Co LLC", "04 3202234"),
    ("Ghulam Ali Abdulla Trading LLC", "04 3201782"),
    ("Ghulami General Trading LLC", "04 3201808"),
    ("Gold Fruit International LLC", "04 3201199"),
    ("Green Earth FZCO", "056 7851351"),
    ("Gulf Fruits Trade Co LLC", "04 3332395"),
    ("Jaleel General Trading Company LLC", "04 3339191"),
    ("Kanya Group of Companies", "050 3095288"),
    ("Khalifa Bel Qaizi Trading Establishment", "04 3377324"),
    ("Khorshed Intl Trdg LLC", "04 3440586"),
    ("Kora Fresh Foods (A Div of Seville Products)", "04 3202777"),
    ("Mehta Trading Company LLC", "04 3200029"),
    ("Mehtab Vegetables and Fruits LLC", "04 3331565"),
    ("Mirajkar General Trading Company LLC", "04 2368600"),
    ("Mohammad Malik Interantional General Trading LLC", "04 3202656"),
    ("Mohd Matar Bin Lahej Trading Company LLC", "04 3201333"),
    ("Nasik Fruits And Vegetables Trdg LLC", "04 3205112"),
    ("Nilgiri General Trading LLC", "04 3311630"),
    ("Portobello Vegetables and Fruits Trading LLC", "054 4221087"),
    ("A A K Middle East LLC", "04 3201828"),
    ("A R S B Trading LLC", "056 6090684"),
    ("Aamir Aziz Fruits And Vegetables Trading LLC", "052 2116786"),
    ("Agrotech Foodstuff Trading LLC", "055 8559194"),
    ("Ai Montazah Vegetables & Fruits Trading LLC", "04 3202797"),
    ("Al Haj Ibrahim Samari Co LLC", "04 3330930"),
    ("Al Sheikh Trdg LLC", "04 3200388"),
    ("Al Taqarub Trading", "04 2224662"),
    ("Al Yusra Foodstuff Trading LLC", "056 1807028"),
    ("Al Zayyat Trading", "04 3333755"),
    ("Ali Kath Trading Establishment", "04 3201493"),
    ("Altaf and Khamas Trading Company LLC", "04 3334446"),
    ("Altaf Hussain Trading Company LLC", "04 3335536"),
    ("Barakat Veg and Fruits Company LLC", "04 2393333"),
    ("Big Fresh Vegetables And Fruit Trading LLC", "04 3982398"),
    ("City Home Foodstuff Trdg LLC", "04 3338090"),
    ("Dxbrand Production", "04 8855444"),
    ("Farzana Trading", "04 3200101"),
    ("Fresh Farmed Food Stuff Trading LLC", "04 3216262"),
    ("Fresh Fruits Co", "04 3200001"),
]

# Create a dataframe for the new leads
new_rows = []
for name, phone in leads:
    # Format the phone number with the country code
    # Example: "04 3201112" -> " +971 4 3201112"
    # Remove leading zero and spaces
    clean_num = phone.replace(" ", "")
    if clean_num.startswith("0"):
        clean_num = clean_num[1:]
    
    formatted_phone = f" +971 {clean_num}"
    
    new_rows.append({
        'Source File': 'Custom Added',
        'Type': 'Buyer',
        'Country': 'UAE',
        'Commodity': 'Fruits & Vegetables',
        'Company Name': name,
        'Phone': formatted_phone,
        'Original_Phone': phone
    })

new_df = pd.DataFrame(new_rows)

print(f"Reading existing file: {file_path}")
df = pd.read_excel(file_path)

# Concatenate the old and new dataframes
combined_df = pd.concat([df, new_df], ignore_index=True)

# Save back to the file using bulletproof excel formatting
print(f"Saving {len(combined_df)} total records...")
combined_df.to_excel(file_path, index=False)
print(f"Successfully added {len(new_df)} new UAE leads with +971 country code!")
