import pdfplumber
import os

pdf_dir = r"C:\Users\DELL\Downloads\Daksh\Buyers Doanloaded pdf\7 13 2026"
pdfs = [
    "420526951-China-Food-Importer-List.pdf",
    "697367414-Importers-of-Agricultural-products.pdf",
    "document.pdf",
    "toaz.info-importers-list-pr_98bc73023d6049fb30162cde2425ac6a.pdf"
]

for pdf in pdfs:
    path = os.path.join(pdf_dir, pdf)
    print(f"\n--- Reading {pdf} ---")
    try:
        with pdfplumber.open(path) as p:
            text = ""
            for i, page in enumerate(p.pages[:2]):
                text += page.extract_text() + "\n"
            print(text[:1000])
    except Exception as e:
        print(f"Error reading {pdf}: {e}")
