import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

buttons = soup.find_all(lambda tag: tag.name in ['a', 'button'] and 'Live Order' in tag.get_text(strip=True))

for idx, b in enumerate(buttons):
    print(f"Button {idx+1}:")
    print("  Text:", b.get_text(strip=True))
    print("  Href:", b.get('href'))
    print("  Onclick:", b.get('onclick'))
    print("  Class:", b.get('class'))
    print("-" * 40)
