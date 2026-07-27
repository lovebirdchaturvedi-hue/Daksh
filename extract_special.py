import pandas as pd
import os

print("Extracting Special Commodity Buyers...")
buyers_path = r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL TRADE BUYERS.xlsx'

# Wait until the file exists (in case the clean script is still finishing)
import time
while not os.path.exists(buyers_path):
    print("Waiting for clean data script to finish...")
    time.sleep(5)

buyers = pd.read_excel(buyers_path)

# Fill NAs in searchable columns
search_cols = ['Commodity', 'Business Name', 'Source File']
for col in search_cols:
    if col in buyers.columns:
        buyers[col] = buyers[col].fillna("").astype(str).str.lower()
    else:
        buyers[col] = ""

# Find Onion
onion_mask = buyers['Commodity'].str.contains('onion') | buyers['Business Name'].str.contains('onion') | buyers['Source File'].str.contains('onion')
onion_buyers = buyers[onion_mask]
onion_out = r'C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS.xlsx'
onion_buyers.to_excel(onion_out, index=False)
print(f"Found {len(onion_buyers)} Onion Buyers!")

# Find Cow Dung / Organic Fertilizer
cow_dung_mask = (buyers['Commodity'].str.contains('cow dung') | 
                 buyers['Commodity'].str.contains('fertilizer') | 
                 buyers['Business Name'].str.contains('fertilizer') | 
                 buyers['Source File'].str.contains('cow dung') | 
                 buyers['Source File'].str.contains('fertilizer'))
cow_dung_buyers = buyers[cow_dung_mask]
cow_dung_out = r'C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS.xlsx'
cow_dung_buyers.to_excel(cow_dung_out, index=False)
print(f"Found {len(cow_dung_buyers)} Cow Dung / Fertilizer Buyers!")

print("Special Extraction Complete.")
