import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import time

# 1. Firebase Auth
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(r"C:\Users\DELL\Downloads\Daksh\serviceAccountKey.jason.txt")
    firebase_admin.initialize_app(cred)

db = firestore.client()

f_path = r"C:\Users\DELL\Downloads\Daksh\IMPORTERS_2026.xlsx"
print(f"Direct Precision Injection: {f_path}...")

def clean_phone(p):
    if pd.isna(p): return None
    s = str(p).replace('.0', '').strip()
    digits = "".join([c for c in s if c.isdigit()])
    if not digits: return None
    if len(digits) == 10: return "91" + digits
    return digits

try:
    df = pd.read_excel(f_path)
    
    # Manual Mapping for IMPORTERS_2026 based on common patterns
    # If headers are missing, use indices
    name_col = df.columns[0]
    phone_col = df.columns[1] # Usually second column is phone in these bulk lists
    
    # Better detection
    for c in df.columns:
        low = str(c).lower()
        if 'phone' in low or 'mobile' in low or 'contact' in low:
            phone_col = c
            break
            
    print(f"Mapped Columns -> Name: {name_col}, Phone: {phone_col}")
    
    batch = db.batch()
    count = 0
    total_in_file = len(df)

    for i, row in df.iterrows():
        phone = clean_phone(row[phone_col])
        if not phone: continue
        
        name = str(row[name_col]).strip() if not pd.isna(row[name_col]) else "Importer Lead"
        
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
        if count % 300 == 0:
            batch.commit()
            batch = db.batch()
            print(f"  Injected {count} / {total_in_file}...")
            time.sleep(2) # SLOW DOWN TO PREVENT QUOTA ERROR

    batch.commit()
    print(f"DONE. Total leads now in database should be ~41,000.")

except Exception as e:
    print(f"Fatal Error: {e}")
