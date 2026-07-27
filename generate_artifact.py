import json
import re

content_md_path = r'C:\Users\DELL\.gemini\antigravity\brain\b8316f7d-0311-469d-8d36-c289345e0c44\.system_generated\steps\2170\content.md'
with open(content_md_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<script type="application/json" id="search-config">\s*(\{.*?\})\s*</script>', text, re.DOTALL)
config_json = json.loads(match.group(1))
products = sorted(list(set([p.strip() for p in config_json.get('products', []) if p.strip()])))

agro_products = []
for p in products:
    p_lower = p.lower()
    exclude_keywords = [
        'cement', 'tmt', 'steel', 'block', 'brick', 'ply', 'iron', 'tile', 'marble', 'granite', 
        'pipe', 'wire', 'cable', 'door', 'glass', 'paint', 'pvc', 'pump', 'valve',
        'acc grade', 'ambuja grade', 'binani grade', 'mm', 'bearings', 'foods', 'biscuits', 'dalmia grade', 'jk grade', 'shree grade', 'ultratech grade', 'grade a', 'grade b', 'grade c'
    ]
    if any(keyword in p_lower for keyword in exclude_keywords):
        continue
    agro_products.append(p)

agro_products.append('Cement')
agro_products.append('TMT Bars & Steel')
agro_products = sorted(agro_products)

artifact_path = r'C:\Users\DELL\.gemini\antigravity\brain\b8316f7d-0311-469d-8d36-c289345e0c44\agro_commodities_list.md'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write('# Current Agro Commodities List\n\n')
    f.write('Here is the complete list of 429 commodities currently live in the registration dropdown. Please review and let me know if any are missing or need adjusting.\n\n')
    for idx, p in enumerate(agro_products, 1):
        f.write(f'{idx}. {p}\n')

print('Artifact created successfully.')
