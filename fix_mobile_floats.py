import re

# Fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the explicit .float-wa override at the bottom of the file
old_float_wa = '.float-wa { width: 55px; height: 55px; bottom: 25px; right: 25px; }'
new_float_wa = '.float-wa { width: 55px; height: 55px; bottom: 100px !important; right: 25px; }'
content = content.replace(old_float_wa, new_float_wa)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Fix assets/css/sales-bot.css
with open('assets/css/sales-bot.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add a media query for .sales-bot-widget
css_addition = '''
    .sales-bot-widget {
        bottom: 100px !important;
    }
'''

# Find the @media (max-width: 768px) { and insert the new rule
if '@media (max-width: 768px) {' in css_content:
    css_content = css_content.replace(
        '@media (max-width: 768px) {',
        '@media (max-width: 768px) {' + css_addition
    )

with open('assets/css/sales-bot.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Fixed floating widgets for mobile!")
