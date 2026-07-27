import pandas as pd
import os

fixed_files = [
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS_FIXED.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS_FIXED.xlsx"
]

for file_path in fixed_files:
    print(f"Processing {file_path} for purely international buyers...")
    try:
        df = pd.read_excel(file_path)
        original_len = len(df)
        
        # Filter out India
        df_international = df[df["Country"] != "India"].copy()
        
        filtered_len = len(df_international)
        removed_count = original_len - filtered_len
        
        print(f"Removed {removed_count} Indian buyers.")
        
        # We will save this as the ultimate clean version
        final_path = file_path.replace("_FIXED.xlsx", "_INTERNATIONAL_ONLY.xlsx")
        
        df_international.to_excel(final_path, index=False)
        
        print(f"Saved {filtered_len} pure international buyers to {final_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
