import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<a[^>]+href=[\'\"]([^\'\"]+)[\'\"][^>]*>.*?</a>', text, re.DOTALL)
for m in matches:
    a_tag = m.group(0)
    if any(keyword in a_tag.upper() for keyword in ['BUY', 'GET STARTED', 'MEMBERSHIP', 'PAY', 'SUBSCRIBE', 'JOIN']):
        print("HREF:", m.group(1))
        print(a_tag[:150].replace('\n', ' '))
        print("-" * 40)
