import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The banking section
match = re.search(r'<section[^>]*>.*?Global Banking Partners.*?</section>', text, re.DOTALL)
if match:
    banking_html = match.group(0)
    
    with open('membership.html', 'r', encoding='utf-8') as mf:
        m_text = mf.read()
    
    if 'Global Banking Partners' not in m_text:
        m_text = m_text.replace('<footer style=', banking_html + '\n\n<footer style=')
        with open('membership.html', 'w', encoding='utf-8') as mf:
            mf.write(m_text)
        print('Added Global Banking Partners to membership.html successfully')
    else:
        print('Already in membership.html')
else:
    print('Could not extract banking partners from index.html')
