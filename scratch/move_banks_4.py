import re

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change website cost
text = text.replace('₹24,999', '₹50,000 - ₹1,00,000')

# Change IEC cost
text = text.replace('₹14,999', '₹25,000')

# Safely extract the LAST section (which is our banking section)
last_section_idx = text.rfind('<section')
if last_section_idx != -1 and 'Global Banking Partners' in text[last_section_idx:]:
    end_idx = text.find('</section>', last_section_idx) + len('</section>')
    banking_html = text[last_section_idx:end_idx]
    
    # Remove it from its current position
    text = text[:last_section_idx] + text[end_idx:]
    
    # Scale it down
    banking_html = banking_html.replace('padding: 120px 8%', 'padding: 60px 5%')
    
    # Insert it right before the export compliance comment
    target = '<!-- EXPORT COMPLIANCE & DIGITAL SETUP SERVICES -->'
    if target in text:
        text = text.replace(target, banking_html + '\n\n    ' + target)
        with open('membership.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Moved banking section safely and updated costs successfully!")
    else:
        print("Could not find compliance target")
else:
    print("Could not find banking section cleanly")
