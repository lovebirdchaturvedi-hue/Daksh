import pandas as pd
import os
import firebase_admin
from firebase_admin import credentials, firestore
import time
import sys

# Encoding fix
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 1. Firebase Auth
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(r"C:\Users\DELL\Downloads\Daksh\serviceAccountKey.jason.txt")
    firebase_admin.initialize_app(cred)

db = firestore.client()
path = r"C:\Users\DELL\Downloads\Daksh"

def clean_phone(p):
    if pd.isna(p): return None
    s = str(p).replace('.0', '').strip()
    digits = "".join([c for c in s if c.isdigit()])
    if not digits: return None
    if len(digits) == 10: return "91" + digits
    return digits

# Deep Column Mapping
NAME_VARIANTS = ['name', 'company', 'company name', 'full name', 'commodity name', 'entity', 'company ', 'full_name']
PHONE_VARIANTS = ['phone', 'mobile no', 'contact no1', 'contact', 'phone number', 'contact no', 'mobile number', 'contact number', 'whatsapp', 'mobile no.', 'contact_no']

total_synced = 0

# Scan ALL Excel and CSV files in the folder
all_files = [f for f in os.listdir(path) if f.endswith(('.xlsx', '.csv'))]

print(f"Starting Deep Sync of {len(all_files)} files...")

for f_name in all_files:
    full_path = os.path.join(path, f_name)
    print(f"Syncing: {f_name}...")
    
    try:
        if f_name.endswith('.csv'):
            df = pd.read_csv(full_path, on_bad_lines='skip', low_memory=False)
        else:
            df = pd.read_excel(full_path)
            
        name_col = next((c for c in df.columns if str(c).lower().strip() in NAME_VARIANTS), None)
        phone_col = next((c for c in df.columns if str(c).lower().strip() in PHONE_VARIANTS), None)
        
        # Emergency Mapping (if no header match, look for a col with 10-12 digit numbers)
        if not phone_col:
            for c in df.columns:
                sample = df[c].dropna().head(10).astype(str)
                if any(len("".join(filter(str.isdigit, x))) >= 10 for x in sample):
                    phone_col = c
                    break
        
        if not phone_col:
            print(f"  Skipping {f_name} - No phone column found.")
            continue

        if not name_col: name_col = df.columns[0] # Default to first column

        batch = db.batch()
        count = 0
        
        for _, row in df.iterrows():
            name = str(row[name_col]).strip() if not pd.isna(row[name_col]) else "Institutional Lead"
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
            total_synced += 1
            
            if count % 400 == 0:
                batch.commit()
                batch = db.batch()
        
        batch.commit()
        print(f"  Finished {f_name}. Synced {count} leads.")

    except Exception as e:
        print(f"  Error in {f_name}: {e}")

print(f"\n✅ DEEP SYNC COMPLETE. Total Leads in Command Center: {total_synced}")
