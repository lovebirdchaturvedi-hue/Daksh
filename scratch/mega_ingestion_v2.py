import pandas as pd
import os
import firebase_admin
from firebase_admin import credentials, firestore
import time
import sys

# Set encoding to handle emojis/special chars in console
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 1. Firebase Auth (Re-use existing app if possible, or handle error)
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(r"C:\Users\DELL\Downloads\Daksh\serviceAccountKey.jason.txt")
    firebase_admin.initialize_app(cred)

db = firestore.client()

path = r"C:\Users\DELL\Downloads\Daksh"
files = [
    "MASTER_OUTREACH_2026.xlsx",
    "BULK DOUBLE TICK.xlsx",
    "Jasmine Rice International.xlsx",
    "Edible Oil International Supplier's.xlsx",
    "Rice Exporter (International).xlsx",
    "Sugar International Supplier's.xlsx",
    "Varities Requirments Country Wise.xlsx",
    "Indian Exporters Data (Verified).xlsx",
    "INTERNATIONAL_EXPORTERS_SK.xlsx",
    "Palm Oil- Indonesia.xlsx",
    "Palm Oil- Malaysia.xlsx",
    "International suppliers only.xlsx",
    "Enchaned Data.xlsx",
    "Seller Leads Campaign Data.xlsx",
    "OnBoarding Tracker.xlsx"
]

def clean_phone(p):
    if pd.isna(p): return None
    s = str(p).replace('.0', '').strip()
    digits = "".join([c for c in s if c.isdigit()])
    if not digits: return None
    if len(digits) == 10: return "91" + digits
    return digits

total_inserted = 0

# Mapping variations for messy Excel files
NAME_VARIANTS = ['name', 'company', 'company name', 'full name', 'commodity name', 'entity']
PHONE_VARIANTS = ['phone', 'mobile no', 'contact no1', 'contact', 'phone number', 'contact no', 'mobile number', 'contact number']

for f_name in files:
    full_path = os.path.join(path, f_name)
    if not os.path.exists(full_path):
        print(f"Skipping {f_name} - Not found.")
        continue

    print(f"Processing {f_name}...")
    try:
        df = pd.read_excel(full_path)
        
        name_col = next((c for c in df.columns if str(c).lower().strip() in NAME_VARIANTS), None)
        phone_col = next((c for c in df.columns if str(c).lower().strip() in PHONE_VARIANTS), None)
        
        if not name_col or not phone_col:
            print(f"Warning: Manual mapping for {f_name} failed. Cols: {df.columns.tolist()}")
            continue

        batch = db.batch()
        count = 0
        
        for index, row in df.iterrows():
            name = str(row[name_col]).strip() if not pd.isna(row[name_col]) else "Bulk Entity"
            phone = clean_phone(row[phone_col])
            
            if not phone: continue
            
            lead_id = f"bulk_{phone}"
            ref = db.collection("suppliers").document(lead_id)
            
            batch.set(ref, {
                "companyName": name,
                "contact": phone,
                "status": "approved",
                "plan": "free",
                "isBulkLead": True,
                "sourceFile": f_name,
                "createdAt": firestore.SERVER_TIMESTAMP
            }, merge=True)
            
            count += 1
            total_inserted += 1
            
            if count % 400 == 0:
                batch.commit()
                batch = db.batch()
        
        batch.commit()
        print(f"Finished {f_name}. Total from file: {count}")

    except Exception as e:
        print(f"Error processing {f_name}: {e}")

print(f"\nSUCCESS: Mega Ingestion Complete. Total leads injected: {total_inserted}")
