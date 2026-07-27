import os

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.html"
pdf_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish_1_Lac.pdf"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

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
