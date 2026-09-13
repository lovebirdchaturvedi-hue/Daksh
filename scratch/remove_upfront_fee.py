import os
import re

with open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the fee_info box
pattern = r'<div style="background: rgba\(212, 175, 55, 0\.1\);.*?</div>\s*</div>\s*<h3>Buyer Contact Details</h3>'
text = re.sub(pattern, '<h3>Buyer Contact Details</h3>', text, flags=re.DOTALL)

with open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Removed upfront fee box from create-rfq.html')
