import os
import sys
import json
import re
import pdfplumber

sys.stdout.reconfigure(encoding='utf-8')

target_dir = r"C:\Users\DELL\Downloads\Daksh\Buyers Doanloaded pdf"

# Regex patterns
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
PHONE_REGEX = re.compile(r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
WEBSITE_REGEX = re.compile(r'(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def parse_text(text):
    emails = list(set(EMAIL_REGEX.findall(text)))
    # Phones often match random numbers, so we keep them as raw as possible and clean later
    phones = list(set(PHONE_REGEX.findall(text)))
    phones = [p for p in phones if len(re.sub(r'\D', '', p)) >= 8] # keep if at least 8 digits
    
    return {
        "emails": emails,
        "phones": phones,
        "raw_text_length": len(text)
    }

def process_all_files():
    all_data = []
    total_pdfs = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                total_pdfs += 1
                filepath = os.path.join(root, file)
                if os.name == 'nt' and not filepath.startswith('\\\\?\\\\'):
                    filepath = '\\\\?\\\\' + os.path.abspath(filepath)
                
                print(f"Processing ({total_pdfs}): {file}")
                text = extract_text_from_pdf(filepath)
                
                parsed = parse_text(text)
                
                # Determine type (Importer/Exporter) from filename
                lower_name = file.lower()
                role = "Unknown"
                if "import" in lower_name:
                    role = "Importer"
                elif "export" in lower_name:
                    role = "Exporter"
                    
                commodity = "Unknown"
                # Some basic keywords
                if "onion" in lower_name: commodity = "Onion"
                elif "spice" in lower_name: commodity = "Spices"
                elif "rice" in lower_name: commodity = "Rice"
                elif "fruit" in lower_name or "veg" in lower_name: commodity = "Fruits/Vegetables"
                elif "dung" in lower_name or "fertilizer" in lower_name: commodity = "Organic Fertilizer"
                
                all_data.append({
                    "filename": file,
                    "filepath": filepath,
                    "role": role,
                    "commodity": commodity,
                    "emails": parsed["emails"],
                    "phones": parsed["phones"],
                    "text_length": parsed["raw_text_length"],
                    "needs_ocr": parsed["raw_text_length"] < 100 # If less than 100 chars, it's probably scanned
                })
                
    # Save results
    out_file = 'raw_extracted_leads.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4)
        
    print(f"\nProcessed {total_pdfs} PDFs. Saved to {out_file}")

if __name__ == '__main__':
    process_all_files()
