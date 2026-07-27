import json
import re

content_md_path = r"C:\Users\DELL\.gemini\antigravity\brain\b8316f7d-0311-469d-8d36-c289345e0c44\.system_generated\steps\2170\content.md"

with open(content_md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract JSON from the script block
match = re.search(r'<script type="application/json" id="search-config">\s*(\{.*?\})\s*</script>', text, re.DOTALL)
if not match:
    print("Could not find search-config JSON.")
    exit(1)

config_json = json.loads(match.group(1))
products = config_json.get("products", [])

# Remove duplicates and sort
unique_products = sorted(list(set([p.strip() for p in products if p.strip()])))

options_html = []
for p in unique_products:
    p_escaped = p.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    options_html.append(f'      <option value="{p_escaped}">{p_escaped}</option>')

options_content = "\n".join(options_html)

new_select = f"""<select id="customCommodity" style="padding: 10px; border-radius: 5px; border: 1px solid #ccc; flex: 1;">
{options_content}
    </select>"""

with open('seed-rfqs.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = re.sub(r'<select id="customCommodity"[\s\S]*?</select>', new_select, html_content)

with open('seed-rfqs.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"seed-rfqs.html updated successfully with {len(unique_products)} options.")
