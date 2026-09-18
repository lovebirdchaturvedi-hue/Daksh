import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find mobile-post-btn CSS
css_match = re.search(r'\.mobile-post-btn\s*\{[^}]*\}', text)
if css_match:
    new_css = '''.mobile-post-btn { 
                display: flex !important; 
                background: linear-gradient(180deg, #ef4444, #b91c1c); 
                color: #fff !important; 
                padding: 10px 20px; 
                font-weight: 900; 
                font-size: 1rem; 
                border-radius: 50px; 
                text-decoration: none;
                align-items: center;
                white-space: nowrap;
                box-shadow: 0 0 20px rgba(239, 68, 68, 0.8);
                animation: heavyBlink 1.5s infinite;
            }'''
    text = text[:css_match.start()] + new_css + text[css_match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Mobile CSS updated successfully.")
else:
    print("Mobile CSS not found.")
