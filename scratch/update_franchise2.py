import codecs
import re

with codecs.open('franchise.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change Total Consulting Fee to Service Charges
text = text.replace('Total Consulting Fee', 'Service Charges')

# Remove the obsolete balance clause since it's just 49,000 now
block_balance = r'3\. I agree to pay the balance of ₹38,000 upon successful franchise allocation\.'
text = re.sub(block_balance, '', text)

# Just in case there are empty background boxes left from the previous removal
empty_box = r'<div style="background: rgba\(239, 68, 68, 0\.1\); border-left: 3px solid #ef4444; padding: 12px; margin-bottom: 25px; border-radius: 4px;">\s*</div>'
text = re.sub(empty_box, '', text)

with codecs.open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated franchise.html successfully")
