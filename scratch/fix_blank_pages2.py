import re
import subprocess
import os

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Completely remove all manual page breaks and let the browser handle it naturally by height
old_css = ".page { width: 209mm; height: 296mm; max-height: 296mm; overflow: hidden; padding: 15mm 20mm; margin: auto; background: white; page-break-after: always; position: relative; box-sizing: border-box; }"
new_css = ".page { width: 210mm; height: 296mm; padding: 15mm 20mm; margin: 0 auto; background: white; page-break-inside: avoid; position: relative; box-sizing: border-box; }"

html = html.replace(old_css, new_css)
html = html.replace(".page:last-child { page-break-after: auto; }", "")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

pdf_path = r"C:\Users\DELL\Downloads\Offer_Letter_Ashish_Final_100000_Fixed.pdf"
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
