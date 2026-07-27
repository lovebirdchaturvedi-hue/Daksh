import json
import re

content_md_path = r"C:\Users\DELL\.gemini\antigravity\brain\b8316f7d-0311-469d-8d36-c289345e0c44\.system_generated\steps\2170\content.md"
with open(content_md_path, 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<script type="application/json" id="search-config">\s*(\{.*?\})\s*</script>', text, re.DOTALL)
config_json = json.loads(match.group(1))
products = sorted(list(set([p.strip() for p in config_json.get('products', []) if p.strip()])))

agro_products = []
for p in products:
    p_lower = p.lower()
    
    # Exclude non-agro and specific grades
    exclude_keywords = [
        "cement", "tmt", "steel", "block", "brick", "ply", "iron", "tile", "marble", "granite", 
        "pipe", "wire", "cable", "door", "glass", "paint", "pvc", "pump", "valve",
        "acc grade", "ambuja grade", "binani grade", "mm", "bearings", "foods", "biscuits", "dalmia grade", "jk grade", "shree grade", "ultratech grade", "grade a", "grade b", "grade c"
    ]
    
    if any(keyword in p_lower for keyword in exclude_keywords):
        continue
        
    agro_products.append(p)

# Now add generic ones for Cement and TMT
agro_products.append("Cement")
agro_products.append("TMT Bars & Steel")

# Sort them properly
agro_products = sorted(agro_products)

# Output for register-supplier.html
checkboxes_html = []
for p in agro_products:
    p_escaped = p.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    checkboxes_html.append(f'<label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="{p_escaped}" style="width: 18px; height: 18px; accent-color: var(--gold);"> {p_escaped}</label>')

checkboxes_html.append('<label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Others" id="other-checkbox" style="width: 18px; height: 18px; accent-color: var(--gold);"> Others (Please specify)</label>')

checkboxes_content = "\n          ".join(checkboxes_html)

new_checkboxes_div = f"""      <div id="product-checkboxes" style="display: none; position: absolute; top: 100%; left: 0; right: 0; background: #0f172a; border: 1px solid var(--gold); border-radius: 8px; padding: 15px; max-height: 300px; overflow-y: auto; z-index: 100; margin-top: 5px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); flex-direction: column; gap: 12px; color: #fff;">
          {checkboxes_content}
      </div>
  </div>
  <input id="other-commodity-input" type="text" placeholder="Please specify your commodity" style="display: none; background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box; color: #fff; margin-bottom: 20px;">"""

with open('register-supplier.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = re.sub(r'<div id="product-checkboxes"[\s\S]*?</div>\s*</div>', new_checkboxes_div, html_content)

with open('register-supplier.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"register-supplier.html updated successfully with {len(agro_products)} products.")

# Update seed-rfqs.html
options_html = []
for p in agro_products:
    p_escaped = p.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    options_html.append(f'      <option value="{p_escaped}">{p_escaped}</option>')

options_content = "\n".join(options_html)

new_select = f"""<select id="customCommodity" style="padding: 10px; border-radius: 5px; border: 1px solid #ccc; flex: 1;">
{options_content}
    </select>"""

with open('seed-rfqs.html', 'r', encoding='utf-8') as f:
    html_content_seed = f.read()

html_content_seed = re.sub(r'<select id="customCommodity"[\s\S]*?</select>', new_select, html_content_seed)

with open('seed-rfqs.html', 'w', encoding='utf-8') as f:
    f.write(html_content_seed)

print(f"seed-rfqs.html updated successfully.")
