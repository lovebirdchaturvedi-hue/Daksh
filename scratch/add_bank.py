import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The banking section starts with <section style="padding: 80px 5%; background: #0f172a; border-top: 1px solid rgba(255,255,255,0.05);">
match = re.search(r'<section style="padding: 80px 5%; background: #0f172a; border-top: 1px solid rgba\(255,255,255,0\.05\);">.*?</section>', text, re.DOTALL)
if match and 'Global Banking Partners' in match.group(0):
    banking_html = match.group(0)
    
    with open('membership.html', 'r', encoding='utf-8') as mf:
        m_text = mf.read()
    
    if 'Global Banking Partners' not in m_text:
        m_text = m_text.replace('<!-- FOOTER -->', banking_html + '\n\n    <!-- FOOTER -->')
        with open('membership.html', 'w', encoding='utf-8') as mf:
            mf.write(m_text)
        print('Added Global Banking Partners to membership.html')
    else:
        print('Already in membership.html')
else:
    print('Could not extract banking partners from index.html')
