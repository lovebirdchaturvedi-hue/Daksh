import re

def insert_post_rfq_link(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Avoid duplicate insertion
    if 'href="/create-rfq.html"' in html and 'Post RFQ' in html:
        print(f"Already injected in {filepath}")
        return

    # In index.html Desktop Nav
    new_html = html.replace(
        '<a href="/buyer-rfqs.html">Buyer RFQs</a>',
        '<a href="/buyer-rfqs.html">Buyer RFQs</a>\n      <a href="/create-rfq.html" style="color: var(--gold); font-weight: 800;">Post RFQ <span style="background: var(--gold); color: #020617; font-size: 0.6rem; padding: 2px 6px; border-radius: 4px; margin-left: 5px; vertical-align: middle;">FREE</span></a>'
    )

    # In Mobile Nav (index.html)
    new_html = new_html.replace(
        '<a href="/buyer-rfqs.html" style="font-size: 1.4rem;',
        '<a href="/create-rfq.html" style="font-size: 1.4rem; font-family: \'Playfair Display\', serif; color: var(--gold); text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.05); padding: 15px 40px; display: block; font-weight: 800;">Post RFQ (Free)</a>\n      <a href="/buyer-rfqs.html" style="font-size: 1.4rem;'
    )

    # In header.html
    new_html = new_html.replace(
        '<a href="/rfq.html">Buyer RFQs</a>',
        '<a href="/rfq.html">Buyer RFQs</a>\n    <a href="/create-rfq.html" style="color: #c9a44a; font-weight: bold;">Post RFQ</a>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Updated {filepath}")

insert_post_rfq_link('index.html')
insert_post_rfq_link('header.html')
