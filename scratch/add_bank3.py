import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract precisely the Global Banking Partners section
start_str = '<section style="padding: 120px 8%; background: #020617; position: relative; overflow: hidden;">'
start_idx = text.find(start_str)

if start_idx != -1:
    end_idx = text.find('</section>', start_idx) + len('</section>')
    banking_html = text[start_idx:end_idx]
    
    with open('membership.html', 'r', encoding='utf-8') as mf:
        m_text = mf.read()
    
    # Clean injection: Find <footer and insert right before it
    footer_idx = m_text.find('<footer')
    if footer_idx != -1:
        new_m_text = m_text[:footer_idx] + banking_html + '\n\n' + m_text[footer_idx:]
        with open('membership.html', 'w', encoding='utf-8') as mf:
            mf.write(new_m_text)
        print('Injected successfully!')
    else:
        print('Footer not found in membership.html')
else:
    print('Start string not found in index.html')
