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

# Let's filter out some obvious non-commodities or branded if needed, or just include all.
# The user said "they should have all".
checkboxes_html = []
for p in unique_products:
    # Escape HTML entities
    p_escaped = p.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    checkboxes_html.append(f'<label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="{p_escaped}" style="width: 18px; height: 18px; accent-color: var(--gold);"> {p_escaped}</label>')

# Add Others
checkboxes_html.append('<label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Others" id="other-checkbox" style="width: 18px; height: 18px; accent-color: var(--gold);"> Others (Please specify)</label>')

checkboxes_content = "\n          ".join(checkboxes_html)

new_checkboxes_div = f"""      <div id="product-checkboxes" style="display: none; position: absolute; top: 100%; left: 0; right: 0; background: #0f172a; border: 1px solid var(--gold); border-radius: 8px; padding: 15px; max-height: 300px; overflow-y: auto; z-index: 100; margin-top: 5px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); flex-direction: column; gap: 12px; color: #fff;">
          {checkboxes_content}
      </div>
  </div>
  <input id="other-commodity-input" type="text" placeholder="Please specify your commodity" style="display: none; background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box; color: #fff; margin-bottom: 20px;">"""

# Now update register-supplier.html
with open('register-supplier.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = re.sub(r'<div id="product-checkboxes"[\s\S]*?</div>\s*</div>', new_checkboxes_div, html_content)

# Make sure the script update logic is there.
script_update1 = """const allCheckboxes = document.querySelectorAll('#product-checkboxes input[type="checkbox"]');

allCheckboxes.forEach(cb => {
    cb.addEventListener("change", () => {
        const otherInput = document.getElementById("other-commodity-input");
        const otherCheckbox = document.getElementById("other-checkbox");
        if (otherCheckbox && otherCheckbox.checked) {
            otherInput.style.display = "block";
        } else if (otherInput) {
            otherInput.style.display = "none";
        }
"""
if 'const otherInput = document.getElementById("other-commodity-input");' not in html_content:
    html_content = html_content.replace('const allCheckboxes = document.querySelectorAll(\'#product-checkboxes input[type="checkbox"]\');\n\nselectBox.addEventListener', 'const allCheckboxes = document.querySelectorAll(\'#product-checkboxes input[type="checkbox"]\');\n\nselectBox.addEventListener')
    html_content = html_content.replace('allCheckboxes.forEach(cb => {\n    cb.addEventListener("change", () => {', script_update1)

    script_update2 = """  // Handle multiple selections from checkboxes
  const otherInput = document.getElementById("other-commodity-input");
  const selectedProductsRaw = Array.from(document.querySelectorAll('#product-checkboxes input[type="checkbox"]:checked'));
  
  const selectedProducts = selectedProductsRaw.map(cb => {
      if(cb.value === "Others" && otherInput && otherInput.value.trim() !== "") {
          return otherInput.value.trim();
      }
      return cb.value;
  });"""
    html_content = html_content.replace('  // Handle multiple selections from checkboxes\n  const selectedProducts = Array.from(document.querySelectorAll(\'#product-checkboxes input[type="checkbox"]:checked\')).map(cb => cb.value);', script_update2)

with open('register-supplier.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated successfully with {len(unique_products)} products.")
