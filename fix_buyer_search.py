import re

def fix_buyer_search():
    with open('buyer-rfqs.html', 'r', encoding='utf-8') as f:
        html = f.read()

    js_to_add = """
    // Grab search query from URL if exists
    const urlParams = new URLSearchParams(window.location.search);
    const initialQuery = urlParams.get('q');
    if (initialQuery) {
        document.getElementById('searchInput').value = initialQuery;
        setTimeout(() => {
            document.getElementById('searchInput').dispatchEvent(new Event('input'));
        }, 500);
    }
"""

    if 'urlParams.get' not in html:
        html = html.replace(
            'document.getElementById("searchInput").addEventListener("input", (e) => {',
            js_to_add + '\n    document.getElementById("searchInput").addEventListener("input", (e) => {'
        )
        with open('buyer-rfqs.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Fixed buyer search init")

fix_buyer_search()
