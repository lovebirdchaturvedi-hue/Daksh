import pandas as pd
import os

path = r"C:\Users\DELL\Downloads\Daksh"
files = [
    "MASTER_OUTREACH_2026.xlsx",
    "BULK DOUBLE TICK.xlsx",
    "Jasmine Rice International.xlsx",
    "Edible Oil International Supplier's.xlsx",
    "Rice Exporter (International).xlsx",
    "Sugar International Supplier's.xlsx"
]

for f in files:
    full_path = os.path.join(path, f)
    if os.path.exists(full_path):
        print(f"--- Columns in {f} ---")
        try:
            df = pd.read_excel(full_path, nrows=1)
            print(df.columns.tolist())
        except Exception as e:
            print(f"Error reading {f}: {e}")
