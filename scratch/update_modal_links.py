import os

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<a href="/create-rfq.html" style="color: var(--gold) !important; font-weight: 700 !important;">Post Live Order',
                    '<a href="#" onclick="document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;" style="color: var(--gold) !important; font-weight: 700 !important;">Post Live Order')

text = text.replace('<a href="/create-rfq.html" style="font-size: 1.4rem; font-family: \'Playfair Display\', serif; color: var(--gold); text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.05); padding: 15px 40px; display: block; font-weight: 800;">Post Live Order',
                    '<a href="#" onclick="document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;" style="font-size: 1.4rem; font-family: \'Playfair Display\', serif; color: var(--gold); text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.05); padding: 15px 40px; display: block; font-weight: 800;">Post Live Order')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html to use modal for all Post Live Order links')
