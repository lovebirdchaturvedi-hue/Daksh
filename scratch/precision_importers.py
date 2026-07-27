import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Firebase Auth
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(r"C:\Users\DELL\Downloads\Daksh\serviceAccountKey.jason.txt")
    firebase_admin.initialize_app(cred)

db = firestore.client()

f_path = r"C:\Users\DELL\Downloads\Daksh\IMPORTERS_2026.xlsx"
print(f"Direct Injection: {f_path}...")

def clean_phone(p):
    if pd.isna(p): return None
    s = str(p).replace('.0', '').strip()
    digits = "".join([c for c in s if c.isdigit()])
    if not digits: return None
    if len(digits) == 10: return "91" + digits
    return digits

try:
    df = pd.read_excel(f_path)
    # The Importers file might use different headers, we'll find the phone column by data pattern
    phone_col = None
    for c in df.columns:
        sample = df[c].dropna().head(20).astype(str)
        if any(len("".join(filter(str.isdigit, x))) >= 10 for x in sample):
            phone_col = c
            break
            
    if not phone_col:
        print("Error: Could not find phone column in Importers file.")
        exit()

    print(f"Found phone column: {phone_col}")
    
    batch = db.batch()
    count = 0
    total_in_file = len(df)

    for _, row in df.iterrows():
        phone = clean_phone(row[phone_col])
        if not phone: continue
        
        name = str(row.iloc[0]).strip() if not pd.isna(row.iloc[0]) else "Importer Lead"
        
        lead_id = f"bulk_{phone}"
        ref = db.collection("suppliers").document(lead_id)
        
        batch.set(ref, {
            "companyName": name,
            "contact": phone,
            "status": "approved",
            "plan": "free",
            "isBulkLead": True,
            "sourceFile": "IMPORTERS_2026.xlsx",
            "createdAt": firestore.SERVER_TIMESTAMP
        }, merge=True)
        
        count += 1
        if count % 400 == 0:
            batch.commit()
            batch = db.batch()
            print(f"  Injected {count} / {total_in_file}...")

    batch.commit()
    print(f"DONE. Injected {count} importer leads.")

except Exception as e:
    print(f"Fatal Error: {e}")
