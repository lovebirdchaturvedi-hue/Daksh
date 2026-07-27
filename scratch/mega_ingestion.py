import pandas as pd
import os
import firebase_admin
from firebase_admin import credentials, firestore
import time

# 1. Firebase Auth
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
    # Add India prefix if missing and looks like Indian number
    if len(digits) == 10: return "91" + digits
    return digits

total_inserted = 0

for f_name in files:
    full_path = os.path.join(path, f_name)
    if not os.path.exists(full_path):
        print(f"Skipping {f_name} - Not found.")
        continue

    print(f"Processing {f_name}...")
    try:
        df = pd.read_excel(full_path)
        
        # Smart Column Mapping
        name_col = None
        phone_col = None
        
        # Find Name Column
        for c in df.columns:
            low = str(c).lower().strip()
            if low in ['name', 'company', 'company name', 'full name', 'commodity name']:
                name_col = c
                break
        
        # Find Phone Column
        for c in df.columns:
            low = str(c).lower().strip()
            if low in ['phone', 'mobile no', 'contact no1', 'contact', 'phone number', 'contact no']:
                phone_col = c
                break
        
        if not name_col or not phone_col:
            print(f"Warning: Could not map columns for {f_name}. Cols: {df.columns.tolist()}")
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
            
            # Commit in batches of 400 (Firestore limit is 500)
            if count % 400 == 0:
                batch.commit()
                batch = db.batch()
                print(f"  Inserted {count} leads from {f_name}...")
        
        batch.commit()
        print(f"Finished {f_name}. Total from file: {count}")

    except Exception as e:
        print(f"Error processing {f_name}: {e}")

print(f"\n✅ MEGA INGESTION COMPLETE. Total leads injected: {total_inserted}")
