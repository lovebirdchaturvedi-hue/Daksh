import os
import subprocess

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.html"
pdf_path = r"C:\Users\DELL\Downloads\Offer_Letter_Ashish_Final_100000.pdf"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

if os.path.exists(chrome_path):
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path
    ]
    subprocess.run(cmd)
    print(f"Saved perfect PDF to {pdf_path}")
else:
    print("Chrome not found.")
