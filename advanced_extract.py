import os
import sys
import json
import re
import fitz  # PyMuPDF
import easyocr
import cv2
import numpy as np
from moviepy import VideoFileClip

sys.stdout.reconfigure(encoding='utf-8')

# Initialize EasyOCR Reader (CPU mode, might be slow but works without CUDA)
print("Loading OCR Model...")
reader = easyocr.Reader(['en'], gpu=False)

target_dir = r"C:\Users\DELL\Downloads\Daksh\Buyers Doanloaded pdf"

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
PHONE_REGEX = re.compile(r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')

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
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # Extract standard text
            page_text = page.get_text("text")
            text += page_text + "\n"
            
            # If text is extremely short, it's likely a scanned page, run OCR on the page image!
            if len(page_text.strip()) < 50:
                pix = page.get_pixmap()
                img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
                if pix.n == 4: # RGBA
                    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
                ocr_results = reader.readtext(img, detail=0)
                text += " ".join(ocr_results) + "\n"
                
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
    return text

def extract_from_image(filepath):
    text = ""
    try:
        ocr_results = reader.readtext(filepath, detail=0)
        text = " ".join(ocr_results)
    except Exception as e:
        print(f"Error reading Image {filepath}: {e}")
    return text

def extract_from_video(filepath):
    text = ""
    try:
        clip = VideoFileClip(filepath)
        duration = clip.duration
        # Extract a frame every 5 seconds to avoid endless OCR
        for t in range(0, int(duration), 5):
            frame = clip.get_frame(t)
            ocr_results = reader.readtext(frame, detail=0)
            text += " ".join(ocr_results) + "\n"
        clip.close()
    except Exception as e:
        print(f"Error reading Video {filepath}: {e}")
    return text

def process_all():
    all_data = []
    file_count = 0
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_count += 1
            filepath = os.path.join(root, file)
            if os.name == 'nt' and not filepath.startswith('\\\\?\\\\'):
                filepath = '\\\\?\\\\' + os.path.abspath(filepath)
                
            print(f"Processing ({file_count}): {file}")
            
            text = ""
            ext = file.lower()
            
            if ext.endswith('.pdf'):
                text = extract_from_pdf(filepath)
            elif ext.endswith(('.png', '.jpg', '.jpeg')):
                text = extract_from_image(filepath)
            elif ext.endswith(('.mp4', '.avi', '.mov')):
                text = extract_from_video(filepath)
            elif ext.endswith(('.txt', '.csv')):
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        text = f.read()
                except Exception as e:
                    print(f"Error reading text file {file}: {e}")
                    
            emails = list(set(EMAIL_REGEX.findall(text)))
            phones = list(set(clean_phones(PHONE_REGEX.findall(text))))
            
            role = "Importer" if "import" in ext else ("Exporter" if "export" in ext else "Unknown")
            commodity = "Unknown"
            if "onion" in ext: commodity = "Onion"
            elif "spice" in ext: commodity = "Spices"
            elif "rice" in ext: commodity = "Rice"
            elif "fruit" in ext or "veg" in ext: commodity = "Fruits/Vegetables"
            elif "dung" in ext or "fertilizer" in ext: commodity = "Organic Fertilizer"
            
            all_data.append({
                "filename": file,
                "role": role,
                "commodity": commodity,
                "emails": emails,
                "phones": phones,
                "has_text": len(text) > 0
            })
            
    with open('advanced_raw_leads.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4)
        
    print(f"\nAdvanced extraction complete. Processed {file_count} files.")

if __name__ == '__main__':
    process_all()
