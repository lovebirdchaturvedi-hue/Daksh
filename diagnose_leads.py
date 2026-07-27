import pandas as pd
import json

files = [
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_COW_DUNG_FERTILIZER_BUYERS_ENRICHED.xlsx",
    r"C:\Users\DELL\Downloads\Daksh\SPECIAL_ONION_BUYERS_ENRICHED.xlsx"
]

results = {}
for f in files:
    try:
        df = pd.read_excel(f)
        if "Country" in df.columns:
            counts = df["Country"].value_counts().to_dict()
        else:
            counts = "No Country column"
        
        sample = df.head(3).to_dict(orient='records')
        results[f.split('\\')[-1]] = {
            "total_rows": len(df),
            "country_distribution": counts,
            "sample_columns": list(df.columns),
            "sample_data": sample
        }
    except Exception as e:
        results[f.split('\\')[-1]] = str(e)

print(json.dumps(results, indent=2))
