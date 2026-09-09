import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    changed = False
    
    # 1. Remove ai-chatbot.js script tag completely
    if '<script src="/assets/js/ai-chatbot.js"></script>' in content:
        content = content.replace('<script src="/assets/js/ai-chatbot.js"></script>', '')
        changed = True
        
    # 2. Move .float-wa (membership.html whatsapp float) to right: 110px
    if '.float-wa {' in content:
        content = re.sub(r'(\.float-wa\s*\{[^}]*right:\s*)30px', r'\g<1>110px', content)
        content = re.sub(r'(\.float-wa\s*\{[^}]*right:\s*)25px', r'\g<1>110px', content)
        changed = True
        
    # 3. Move .desktop-wa-btn (index.html whatsapp float) to right: 110px
    if 'desktop-wa-btn' in content:
        content = re.sub(r'(class="desktop-wa-btn"\s*style="[^"]*right:\s*)[\d]+px', r'\g<1>110px', content)
        changed = True

    if changed:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
