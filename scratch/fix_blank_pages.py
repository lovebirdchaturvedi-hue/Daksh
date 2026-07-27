import re

html_path = r"C:\Users\DELL\Downloads\Updated_Offer_Letter_Ashish 75000.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix the CSS that's causing the blank pages
# The combination of 297mm height and page-break-after: always often causes the browser to spill over to a blank page.
# We will reduce the height slightly to 296mm and width to 209mm to fit safely inside A4 without triggering an overflow page.

old_css = ".page { width: 210mm; min-height: 297mm; padding: 15mm 20mm; margin: auto; background: white; page-break-after: always; position: relative; box-sizing: border-box; }"
new_css = ".page { width: 209mm; height: 296mm; max-height: 296mm; overflow: hidden; padding: 15mm 20mm; margin: auto; background: white; page-break-after: always; position: relative; box-sizing: border-box; }"

html = html.replace(old_css, new_css)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Fixed blank pages in {html_path}")
