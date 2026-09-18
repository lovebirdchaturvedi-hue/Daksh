with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div style="max-width: 1300px; margin: 0 auto;">')
if start_idx == -1:
    # try another marker
    start_idx = text.find('<!-- NEW PRICING SECTION -->')
if start_idx == -1:
    start_idx = text.find('<h3 style="font-size: 26px; margin-bottom: 10px; color: #6ab0f5;">Professional Pass</h3>') - 200

# We'll just replace based on the overall wrapper for pricing.
# It seems the pricing is inside `<main style="padding: 100px 0;">` or similar.
parts = text.split('<main')
if len(parts) > 1:
    main_content = parts[1]
    
    # Just to be safe, I'll rewrite the entire <main> block for membership since they only want 3 plans.
    pass

import re

# Let's find where Professional Pass begins
match_prof = re.search(r'<div[^>]*>.*?Professional Pass.*?(?=<!-- CONFUSED)', text, re.DOTALL | re.IGNORECASE)

