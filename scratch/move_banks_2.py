import re

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change website cost
text = text.replace('₹24,999', '₹50,000 - ₹1,00,000')

# Extract banking section safely
banking_match = re.search(r'<section[^>]*>.*?Global Banking Partners.*?</section>', text, re.DOTALL)
if banking_match:
    banking_html = banking_match.group(0)
    
    # Remove it from its current position
    text = text.replace(banking_html, '')
    
    # Scale it down
    banking_html = banking_html.replace('padding: 120px 8%', 'padding: 40px 5%')
    
    # Insert it right before the export compliance header
    # Let's search for the actual HTML tag of the export compliance header instead of comment
    target_match = re.search(r'<h2 class=\"section-title\"[^>]*>Export Compliance & Digital Setup</h2>', text)
    if target_match:
        target = target_match.group(0)
        # Find the comment that precedes it
        idx = text.find(target)
        comment_idx = text.rfind('<!-- EXPORT COMPLIANCE', 0, idx)
        if comment_idx != -1:
            insertion_idx = comment_idx
        else:
            insertion_idx = idx
            
        new_text = text[:insertion_idx] + banking_html + '\n\n' + text[insertion_idx:]
        with open('membership.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Moved banking section and updated website cost!")
    else:
        print("Could not find compliance header")
else:
    print("Could not find banking section")
