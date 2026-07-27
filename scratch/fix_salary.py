import re
import os

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix Basic Row
old_basic_row = "<tr><td>Basic</td><td>1,00,000.00</td><td>12,00,000.00</td></tr>"
new_basic_row = "<tr><td>Basic</td><td>75,000.00</td><td>9,00,000.00</td></tr>"
html = html.replace(old_basic_row, new_basic_row)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved HTML to {html_path}")

# Convert to PDF
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.pdf"

if os.path.exists(chrome_path):
    import subprocess
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path
    ]
    subprocess.run(cmd)
    print(f"Saved PDF to {pdf_path}")
else:
    print("Chrome not found.")
