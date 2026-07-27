import pandas as pd
import json

path = r"C:\Users\DELL\Downloads\Daksh\Exporters 2026.xlsx"
try:
    df = pd.read_excel(path, engine='openpyxl')
    print("XLSX Length:", len(df))
except Exception as e:
    print("XLSX failed:", e)
    try:
        df = pd.read_csv(path)
        print("CSV Length:", len(df))
        
        # We need to append the 108 exporters to this CSV
        # Wait, the data is lost since the script finished. But I can re-read the json if I saved it? No I didn't save the raw extracted data. 
    except Exception as e2:
        print("CSV failed:", e2)
