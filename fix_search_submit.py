import re

def fix_search_buttons():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix hero button
    html = re.sub(
        r'<button(.*?)onclick="window\.location\.href=\'/buyer-rfqs\.html\'"(.*?)>Search</button>',
        r'<button\1type="submit"\2>Search</button>',
        html
    )

    # The mini search button was already fixed in final_tweaks_2.py:
    # <button type="submit" ...>🔎</button>
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed hero submit button")

fix_search_buttons()
