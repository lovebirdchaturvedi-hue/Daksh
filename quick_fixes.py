import re

def run_fixes():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove desktop-only class from mini-search
    # <div id="mini-search" class="desktop-only" ...
    html = html.replace('id="mini-search" class="desktop-only"', 'id="mini-search"')

    # 2. Add height: auto to mobile search inner just in case
    html = html.replace(
        '.hero-search-inner {',
        '.hero-search-inner {\n                    height: auto !important;'
    )
    
    # 3. Remove testimonials section
    # Use regex to find from <!-- 5-STAR TESTIMONIALS SECTION --> to <!-- MEET THE FOUNDER SECTION -->
    pattern = r'<!-- 5-STAR TESTIMONIALS SECTION -->.*?<!-- MEET THE FOUNDER SECTION -->'
    html = re.sub(pattern, '<!-- MEET THE FOUNDER SECTION -->', html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixes applied.")

run_fixes()
