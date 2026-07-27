import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix dual style tags on buttons
# e.g., style="margin-top: auto;" style="background: #d4af37; ..."
html = re.sub(r'style="margin-top: auto;"\s+style="([^"]*)"', r'style="margin-top: auto; \1"', html)

# Fix dual style tags on plan divs
html = re.sub(r'style="display: flex; flex-direction: column;"\s+style="([^"]*)"', r'style="display: flex; flex-direction: column; \1"', html)

# Remove the invalid div inside ul
html = html.replace('<ul class="features" style="flex-grow: 1;">\n<div style="flex-grow: 1;"></div>', '<ul class="features" style="flex-grow: 1;">')
html = html.replace('<ul style="flex-grow: 1;">\n<div style="flex-grow: 1;"></div>', '<ul style="flex-grow: 1;">')
html = html.replace('<ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 30px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">\n<div style="flex-grow: 1;"></div>', '<ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 30px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">')
html = html.replace('<ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 20px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">\n<div style="flex-grow: 1;"></div>', '<ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 20px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">')

# Ensure the JS is completely removed for tax replacement since we do it in CSS or let's just make it generic in JS if needed.
# Actually I never fixed the tax text to be toggleable.
# Let's add span for tax text too.

tax1_old = '<p style="font-size: 0.8rem; opacity: 0.6; margin-bottom: 30px;" id="tax-plan1">Inclusive of GST</p>'
tax1_new = '<p style="font-size: 0.8rem; opacity: 0.6; margin-bottom: 30px;"><span class="show-inr">Inclusive of GST</span><span class="show-usd">No tax on export services</span></p>'
html = html.replace(tax1_old, tax1_new)

tax2_old = '<p style="font-size: 0.8rem; opacity: 0.6; margin-bottom: 30px;" id="tax-plan2">Inclusive of GST</p>'
html = html.replace(tax2_old, tax1_new)

tax3_old = '<p style="font-size: 0.8rem; opacity: 0.6; margin-bottom: 30px;" id="tax-plan3">Inclusive of GST</p>'
html = html.replace(tax3_old, tax1_new)

tax4_old = '<p style="font-size: 0.8rem; opacity: 0.6; margin-bottom: 30px;" id="tax-plan4">Inclusive of GST</p>'
html = html.replace(tax4_old, tax1_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Styles and alignment fixed.")
