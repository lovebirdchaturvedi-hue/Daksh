import json
import re

curated_commodities = [
    # CEREALS & GRAINS
    "1121 Basmati Rice",
    "1509 Basmati Rice",
    "1401 Basmati Rice",
    "Non-Basmati Rice",
    "Sona Masoori Rice",
    "IR-64 Parboiled Rice",
    "Wheat",
    "Corn / Maize",
    "Barley",
    "Millets (Bajra, Ragi, Jowar)",

    # PULSES & LENTILS
    "Pulses & Lentils (All)",
    "Chickpeas (Kabuli & Desi)",
    "Pigeon Pea (Toor Dal)",
    "Black Matpe Beans (Urad)",
    "Red Kidney Beans (Rajma)",

    # SPICES (Just one option as requested)
    "Spices (All)",

    # DRY FRUITS & NUTS (Just one option as requested)
    "Dry Fruits & Nuts (All)",

    # SUGAR & SWEETENERS (Minimized)
    "Sugar (All Types)",
    "Jaggery",

    # EDIBLE OILS (Kept separate as requested)
    "Mustard Oil",
    "Sunflower Oil",
    "Palm Oil",
    "Soybean Oil",
    "Groundnut Oil",
    "Canola Oil",
    "Olive Oil",

    # BEVERAGES
    "Tea (Black, Green, CTC)",
    "Coffee (Arabica & Robusta)",

    # OTHERS
    "Fresh Onion",
    "Fresh Potato",
    "Moringa (Powder & Leaves)",
    "Meat & Poultry",
    "Dairy Products (Milk, Butter, Cheese)",

    # INDUSTRIAL
    "Cement",
    "TMT Bars & Steel"
]

curated_commodities = sorted(curated_commodities)

# Register-supplier
checkboxes_html = []
for p in curated_commodities:
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

# Update seed-rfqs.html
options_html = []
for p in curated_commodities:
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

print(f"Updated successfully with {len(curated_commodities)} curated products.")
