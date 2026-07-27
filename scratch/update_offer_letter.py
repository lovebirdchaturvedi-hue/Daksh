import re
import base64
import os

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish.html"
img_path = r"C:\Users\DELL\Downloads\TRADO IMAGE OFFER.PNG"

# Read original HTML
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Base64 encode logo
with open(img_path, "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')
logo_data_uri = f"data:image/png;base64,{b64_logo}"

# Replace the text-based logo with the image
html = re.sub(
    r'<div class="logo-area">.*?</div>',
    f'<img src="{logo_data_uri}" alt="tradologie.com" style="height: 40px; margin-bottom: 5px;">',
    html,
    flags=re.DOTALL
)

# 1. Designation
html = html.replace("Assistant Manager", "International Sales Head")
html = html.replace("Asst Manager-International Sales", "International Sales Head")

# 2. Total Salary (75,000 -> 100,000)
html = html.replace("Total Remuneration: 75,000/- per month", "Total Remuneration: 1,00,000/- per month")

# 3. Basic Pay in text
html = html.replace("basic pay (50,000/-)", "basic pay (75,000/-)")

# 4. Salary Table Updates
# Find the table rows and replace the values
html = html.replace("<td>50,000.00</td><td>6,00,000.00</td>", "<td>75,000.00</td><td>9,00,000.00</td>")
html = html.replace("<td>75,000.00</td><td>9,00,000.00</td>", "<td>1,00,000.00</td><td>12,00,000.00</td>", 1) # Only the total line! Wait, the first one replaces the Basic pay!

# Let's do it safer:
# Basic line:
html = html.replace("<tr><td>Basic</td><td>50,000.00</td><td>6,00,000.00</td></tr>", "<tr><td>Basic</td><td>75,000.00</td><td>9,00,000.00</td></tr>")
# Total line:
html = html.replace("<tr><td style=\"font-weight:bold;\">Cost to Company</td><td style=\"font-weight:bold;\">75,000.00</td><td style=\"font-weight:bold;\">9,00,000.00</td></tr>", "<tr><td style=\"font-weight:bold;\">Cost to Company</td><td style=\"font-weight:bold;\">1,00,000.00</td><td style=\"font-weight:bold;\">12,00,000.00</td></tr>")

# CTC Per Annum in table 3
html = html.replace("<td>CTC Per Annum</td><td>9,00,000.00</td>", "<td>CTC Per Annum</td><td>12,00,000.00</td>")

# Save the new HTML
new_html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish_100000.html"
with open(new_html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved HTML to {new_html_path}")

# Convert to PDF using headless Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish_100000.pdf"

if os.path.exists(chrome_path):
    import subprocess
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        new_html_path
    ]
    subprocess.run(cmd)
    print(f"Saved PDF to {pdf_path}")
else:
    print("Chrome not found for PDF conversion.")
