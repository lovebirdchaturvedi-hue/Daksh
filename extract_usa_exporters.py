import pandas as pd
import os

source_file = r"C:\Users\DELL\Downloads\Daksh\APD Global Suppliers Final.xlsx"
output_file = r"C:\Users\DELL\Downloads\Daksh\USA_Exporters_Final.xlsx"

try:
    print(f"Reading {source_file}...")
    df = pd.read_excel(source_file)
    
    # Filter for USA
    if "Country" in df.columns:
        usa_df = df[df["Country"].astype(str).str.contains("USA", case=False, na=False)].copy()
        print(f"Found {len(usa_df)} USA exporters.")
        
        if len(usa_df) > 0:
            usa_df.to_excel(output_file, index=False)
            print(f"Successfully saved to {output_file}")
        else:
            print("No USA exporters found.")
    else:
        print("Country column not found in the file!")
        
except Exception as e:
    print(f"Error: {e}")
