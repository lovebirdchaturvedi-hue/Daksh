import pdfplumber
import os
import re
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r"C:\Users\DELL\Downloads\Daksh\Buyers Doanloaded pdf\7 13 2026"
out_dir = r"C:\Users\DELL\Downloads\Daksh"

importers_xlsx_path = os.path.join(out_dir, "REAL BUYERS 2026.xlsx")
exporters_xlsx_path = os.path.join(out_dir, "Exporters 2026.xlsx")

pdfs = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

importers_data = []
exporters_data = []

email_regex = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
phone_regex = re.compile(r"\+?\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}")

def extract_from_text(text, default_country, default_commodity, is_exporter):
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        emails = email_regex.findall(line)
        phones = phone_regex.findall(line)
        phones = [p for p in phones if len(re.sub(r'\D', '', p)) >= 8]
        
        if emails or len(phones) > 0:
            email = emails[0] if emails else "Not Mentioned"
            phone = phones[0] if phones else "Not Mentioned"
            
            if i > 0 and len(lines[i-1].strip()) > 3 and not email_regex.findall(lines[i-1]):
                company = lines[i-1].strip()
            elif i > 1 and len(lines[i-2].strip()) > 3 and not email_regex.findall(lines[i-2]):
                company = lines[i-2].strip()
            else:
                company = "Not Mentioned"
                
            entry = {
                "Company Name": company,
                "Contact Name": "Not Mentioned",
                "Email": email,
                "WhatsApp Number": phone,
                "Commodity": default_commodity,
                "Country": default_country,
                "Quantity": "Not Mentioned"
            }
            
            if email == "Not Mentioned" and phone == "Not Mentioned":
                continue
                
            if is_exporter:
                exporters_data.append(entry)
            else:
                importers_data.append(entry)

def process_pdf(filename, path):
    print(f"Processing {filename}...", flush=True)
    is_exporter = "exporter" in filename.lower()
    
    country = "Not Mentioned"
    if "china" in filename.lower(): country = "China"
    if "uae" in filename.lower(): country = "UAE"
    if "france" in filename.lower(): country = "France"
    if "taiwan" in filename.lower() or "全國" in filename: country = "Taiwan"
    
    commodity = "Agricultural Products"
    if "food" in filename.lower(): commodity = "Food Products"
    
    try:
        with pdfplumber.open(path) as p:
            # ONLY READ FIRST 10 PAGES MAX TO PREVENT HANGING
            num_pages = min(len(p.pages), 10) 
            text = ""
            for i in range(num_pages):
                page_text = p.pages[i].extract_text()
                if page_text:
                    text += page_text + "\n"
            extract_from_text(text, country, commodity, is_exporter)
        print(f"Done processing {filename}.", flush=True)
    except Exception as e:
        print(f"Failed {filename}: {e}", flush=True)

for pdf in pdfs:
    process_pdf(pdf, os.path.join(pdf_dir, pdf))

def deduplicate(data):
    unique = []
    seen = set()
    for row in data:
        email = row['Email']
        phone = row['WhatsApp Number']
        key = f"{email}_{phone}"
        if key not in seen:
            seen.add(key)
            unique.append(row)
    return unique

importers_data = deduplicate(importers_data)
exporters_data = deduplicate(exporters_data)

print(f"Found {len(importers_data)} new importers and {len(exporters_data)} new exporters.", flush=True)

def append_to_excel(filepath, new_data):
    if not os.path.exists(filepath):
        print(f"{filepath} not found!", flush=True)
        return 0
        
    print(f"Appending to {filepath}...", flush=True)
    try:
        existing_df = pd.read_excel(filepath)
        
        if not new_data:
            return len(existing_df)
            
        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        if 'Email' in combined_df.columns:
            combined_df.drop_duplicates(subset=['Email'], keep='last', inplace=True, ignore_index=True)
        
        combined_df.to_excel(filepath, index=False)
        return len(combined_df)
    except Exception as e:
        print(f"Failed to append to {filepath}: {e}", flush=True)
        return 0

total_importers = append_to_excel(importers_xlsx_path, importers_data)
total_exporters = append_to_excel(exporters_xlsx_path, exporters_data)

print(f"TOTAL_IMPORTERS:{total_importers}", flush=True)
print(f"TOTAL_EXPORTERS:{total_exporters}", flush=True)
