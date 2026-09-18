import re

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change website cost
text = text.replace('₹24,999', '₹50,000 - ₹1,00,000')

# Change IEC cost
text = text.replace('₹14,999', '₹25,000')

banking_match = re.search(r'<section[^>]*>.*?Global Banking Partners.*?</section>', text, re.DOTALL)
if banking_match:
    banking_html = banking_match.group(0)
    
    # Remove it from its current position
    text = text.replace(banking_html, '')
    
    # Scale it down
    banking_html = banking_html.replace('padding: 120px 8%', 'padding: 40px 5%')
    
    # Insert it right before the export compliance comment
    target = '<!-- EXPORT COMPLIANCE & DIGITAL SETUP SERVICES -->'
    if target in text:
        text = text.replace(target, banking_html + '\n\n    ' + target)
        with open('membership.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Moved banking section and updated costs successfully!")
    else:
        print("Could not find compliance target")
else:
    print("Could not find banking section")
