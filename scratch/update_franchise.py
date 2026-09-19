import codecs
import re

with codecs.open('franchise.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the booking amount block
block1 = r'<p[^>]*><strong>Booking Amount:</strong> ₹11,000 \(Non-Refundable\)</p>\s*<p[^>]*>The remaining balance of ₹38,000 is strictly payable ONLY upon successful franchise allocation.</p>'
text = re.sub(block1, '', text)

# Remove the consultation fee term
block2 = r'2\. The initial consultation fee of ₹11,000 is strictly non-refundable under any circumstances\.<br>'
text = re.sub(block2, '', text)

# Change button text
text = text.replace('SUBMIT & PAY ₹11,000', 'SUBMIT APPLICATION')

with codecs.open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated franchise.html successfully")
