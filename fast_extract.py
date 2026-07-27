import os
import sys
import json
import re
import fitz  # PyMuPDF
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

target_dir = r"C:\Users\DELL\Downloads\Daksh\Buyers Doanloaded pdf"

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
PHONE_REGEX = re.compile(r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
WEBSITE_REGEX = re.compile(r'(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

def clean_phones(phones):
    cleaned = []
    for p in phones:
        nums = re.sub(r'\D', '', p)
        if len(nums) >= 8:
            cleaned.append(p)
    return cleaned

def extract_from_pdf(filepath):
    text = ""
    try:
        doc = fitz.open(filepath)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error reading PDF {os.path.basename(filepath)}: {e}")
    return text

def process_all():
    all_data = []
    file_count = 0
    total_emails = 0
    total_phones = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_count += 1
            filepath = os.path.join(root, file)
            if os.name == 'nt' and not filepath.startswith('\\\\?\\\\'):
                filepath = '\\\\?\\\\' + os.path.abspath(filepath)
                
            text = ""
            ext = file.lower()
            
            if ext.endswith('.pdf'):
                text = extract_from_pdf(filepath)
            elif ext.endswith(('.txt', '.csv')):
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        text = f.read()
                except:
                    pass
            
            # If no text (e.g. image/video), we at least use the filename
            if not text:
                text = file
                
            emails = list(set(EMAIL_REGEX.findall(text)))
            phones = list(set(clean_phones(PHONE_REGEX.findall(text))))
            websites = list(set(WEBSITE_REGEX.findall(text)))
            
            # Filter websites a bit to avoid matching emails or random files
            websites = [w for w in websites if '@' not in w and not w.endswith(('.pdf', '.png', '.jpg', '.mp4'))]
            
            role = "Importer"
            if "export" in ext or "exporter" in text.lower()[:500]: 
                role = "Exporter"
                
            commodity = "Unknown"
            text_lower = text.lower()
            if "onion" in ext or "onion" in text_lower: commodity = "Onion"
            elif "spice" in ext or "spice" in text_lower: commodity = "Spices"
            elif "rice" in ext or "rice" in text_lower: commodity = "Rice"
            elif "fruit" in ext or "veg" in ext or "fruits" in text_lower: commodity = "Fruits/Vegetables"
            elif "dung" in ext or "fertilizer" in ext or "cow dung" in text_lower or "organic fe" in text_lower: 
                commodity = "Organic Fertilizer/Cow Dung"
            elif "garlic" in text_lower: commodity = "Garlic"
            elif "potato" in text_lower: commodity = "Potato"
            elif "maize" in text_lower: commodity = "Maize"
            elif "wheat" in text_lower: commodity = "Wheat"
            
            # Try to guess country from phone
            country = "Unknown"
            if any(p.startswith(('+91', '919', '918', '917', '916')) for p in phones): country = "India"
            elif any(p.startswith(('+971', '971')) for p in phones): country = "UAE"
            elif any(p.startswith(('+1', '1')) for p in phones): country = "USA/Canada"
            elif any(p.startswith(('+44', '44')) for p in phones): country = "UK"
            elif any(p.startswith(('+61', '61')) for p in phones): country = "Australia"
            
            total_emails += len(emails)
            total_phones += len(phones)
            
            # Since some files have HUNDREDS of emails (it's a directory), we should unroll them if there are many.
            # If it's a list, we create an entry for each email to populate the Excel properly.
            if len(emails) > 0 or len(phones) > 0:
                max_len = max(len(emails), len(phones))
                for i in range(max_len):
                    all_data.append({
                        "Source File": file,
                        "Role": role,
                        "Commodity": commodity,
                        "Country": country,
                        "Business Name": "", # Hard to extract without NLP
                        "Email": emails[i] if i < len(emails) else "",
                        "Phone": phones[i] if i < len(phones) else "",
                        "Website": websites[i] if i < len(websites) else ""
                    })
            else:
                all_data.append({
                    "Source File": file,
                    "Role": role,
                    "Commodity": commodity,
                    "Country": country,
                    "Business Name": "",
                    "Email": "",
                    "Phone": "",
                    "Website": ""
                })
                
    df = pd.DataFrame(all_data)
    # Deduplicate by Email and Phone (if both present)
    df = df.drop_duplicates(subset=['Email', 'Phone'], keep='first')
    
    # Split into Importers and Exporters
    importers = df[df['Role'] == 'Importer']
    exporters = df[df['Role'] == 'Exporter']
    
    importers.to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS 2026.xlsx', index=False)
    exporters.to_excel(r'C:\Users\DELL\Downloads\Daksh\APD GLOBAL EXPORTERS 2026.xlsx', index=False)
    
    print(f"Extraction Complete! Processed {file_count} files.")
    print(f"Total Unique Importers (Buyers): {len(importers)}")
    print(f"Total Unique Exporters: {len(exporters)}")

if __name__ == '__main__':
    process_all()
