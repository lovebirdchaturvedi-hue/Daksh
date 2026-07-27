import re
import os

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Make the logo bigger
html = html.replace('style="height: 40px; margin-bottom: 5px;"', 'style="height: 90px; margin-bottom: 5px;"')

# 2. Put the logo on the right side top
# The current CSS is: .header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
# I will add flex-direction: row-reverse; to swap the left and right items.
html = html.replace(
    '.header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }',
    '.header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; flex-direction: row-reverse; }'
)
# And make the date left-aligned since it's now on the left
html = html.replace('text-align: right;', 'text-align: left;')

# 3. Ensure no blank page at the end
# Add .page:last-child { page-break-after: auto; }
html = html.replace(
    '</style>',
    '    .page:last-child { page-break-after: auto; }\n    </style>'
)

# Also remove any trailing white space
html = html.strip()

# User requested the file name to be "Updated_Offer_Letter_Ashish 75000"
new_html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.html"
with open(new_html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved HTML to {new_html_path}")

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
        new_html_path
    ]
    subprocess.run(cmd)
    print(f"Saved PDF to {pdf_path}")
else:
    print("Chrome not found.")
