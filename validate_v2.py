import pandas as pd

files = [
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS_INTERNATIONAL_ONLY_V2.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS_INTERNATIONAL_ONLY_V2.xlsx"
]

for f in files:
    try:
        df = pd.read_excel(f)
        print(f"\n--- Validation for {f.split('\\')[-1]} ---")
        print(f"Total Rows: {len(df)}")
        print(f"Total Columns: {len(df.columns)}")
        print("First 3 Phones:")
        print(df["Phone"].head(3).tolist())
    except Exception as e:
        print(e)
