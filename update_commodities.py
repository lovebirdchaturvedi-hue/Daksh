import re

with open('register-supplier.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace checkboxes
new_checkboxes = """      <div id="product-checkboxes" style="display: none; position: absolute; top: 100%; left: 0; right: 0; background: #0f172a; border: 1px solid var(--gold); border-radius: 8px; padding: 15px; max-height: 200px; overflow-y: auto; z-index: 100; margin-top: 5px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); flex-direction: column; gap: 12px; color: #fff;">
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Basmati Rice" style="width: 18px; height: 18px; accent-color: var(--gold);"> Basmati Rice</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Non-Basmati Rice" style="width: 18px; height: 18px; accent-color: var(--gold);"> Non-Basmati Rice</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Wheat & Wheat Flour" style="width: 18px; height: 18px; accent-color: var(--gold);"> Wheat & Wheat Flour</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Corn & Maize" style="width: 18px; height: 18px; accent-color: var(--gold);"> Corn & Maize</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Millet (Bajra, Jowar, Ragi)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Millet (Bajra, Jowar, Ragi)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Chickpeas (Chana)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Chickpeas (Chana)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Red Lentils (Masoor)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Red Lentils (Masoor)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Yellow Pigeon Peas (Toor)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Yellow Pigeon Peas (Toor)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Green Gram (Moong)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Green Gram (Moong)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Black Gram (Urad)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Black Gram (Urad)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Kidney Beans (Rajma)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Kidney Beans (Rajma)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Soybean Meal" style="width: 18px; height: 18px; accent-color: var(--gold);"> Soybean Meal</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Turmeric" style="width: 18px; height: 18px; accent-color: var(--gold);"> Turmeric</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Turmeric Powder" style="width: 18px; height: 18px; accent-color: var(--gold);"> Turmeric Powder</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cumin Seeds" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cumin Seeds</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Black Pepper" style="width: 18px; height: 18px; accent-color: var(--gold);"> Black Pepper</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cardamom" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cardamom</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Coriander Seeds" style="width: 18px; height: 18px; accent-color: var(--gold);"> Coriander Seeds</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Fenugreek Seeds" style="width: 18px; height: 18px; accent-color: var(--gold);"> Fenugreek Seeds</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Fennel Seeds" style="width: 18px; height: 18px; accent-color: var(--gold);"> Fennel Seeds</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cloves" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cloves</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Nutmeg" style="width: 18px; height: 18px; accent-color: var(--gold);"> Nutmeg</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cinnamon" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cinnamon</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Ginger (Dried, Powder, etc)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Ginger (Dried, Powder, etc)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Red Chilli Powder" style="width: 18px; height: 18px; accent-color: var(--gold);"> Red Chilli Powder</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Potatoes" style="width: 18px; height: 18px; accent-color: var(--gold);"> Potatoes</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Potato Flakes" style="width: 18px; height: 18px; accent-color: var(--gold);"> Potato Flakes</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Mangoes" style="width: 18px; height: 18px; accent-color: var(--gold);"> Mangoes</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Red Onion" style="width: 18px; height: 18px; accent-color: var(--gold);"> Red Onion</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Fresh Onions" style="width: 18px; height: 18px; accent-color: var(--gold);"> Fresh Onions</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Fresh Garlic" style="width: 18px; height: 18px; accent-color: var(--gold);"> Fresh Garlic</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Grapes" style="width: 18px; height: 18px; accent-color: var(--gold);"> Grapes</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Pomegranates" style="width: 18px; height: 18px; accent-color: var(--gold);"> Pomegranates</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Bananas" style="width: 18px; height: 18px; accent-color: var(--gold);"> Bananas</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Apples" style="width: 18px; height: 18px; accent-color: var(--gold);"> Apples</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Sugar (Raw & White)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Sugar (Raw & White)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Sesame Seeds" style="width: 18px; height: 18px; accent-color: var(--gold);"> Sesame Seeds</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Castor Seed/Oil" style="width: 18px; height: 18px; accent-color: var(--gold);"> Castor Seed/Oil</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Peanuts (Groundnuts)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Peanuts (Groundnuts)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Guar Gum" style="width: 18px; height: 18px; accent-color: var(--gold);"> Guar Gum</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cotton" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cotton</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Sunflower Oil" style="width: 18px; height: 18px; accent-color: var(--gold);"> Sunflower Oil</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Palm Oil" style="width: 18px; height: 18px; accent-color: var(--gold);"> Palm Oil</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Mustard Oil" style="width: 18px; height: 18px; accent-color: var(--gold);"> Mustard Oil</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Dry Fruits & Nuts" style="width: 18px; height: 18px; accent-color: var(--gold);"> Dry Fruits & Nuts</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cashew Nuts" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cashew Nuts</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Frozen Meat & Poultry" style="width: 18px; height: 18px; accent-color: var(--gold);"> Frozen Meat & Poultry</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Tea" style="width: 18px; height: 18px; accent-color: var(--gold);"> Tea</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cocoa Powder" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cocoa Powder</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Coffee Beans" style="width: 18px; height: 18px; accent-color: var(--gold);"> Coffee Beans</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Makhana (Fox Nuts)" style="width: 18px; height: 18px; accent-color: var(--gold);"> Makhana (Fox Nuts)</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Moringa Powder" style="width: 18px; height: 18px; accent-color: var(--gold);"> Moringa Powder</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Cow Dung" style="width: 18px; height: 18px; accent-color: var(--gold);"> Cow Dung</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Medical & Pharma" style="width: 18px; height: 18px; accent-color: var(--gold);"> Medical & Pharma</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Construction Cement" style="width: 18px; height: 18px; accent-color: var(--gold);"> Construction Cement</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Plywood & Timber" style="width: 18px; height: 18px; accent-color: var(--gold);"> Plywood & Timber</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="TMT Bars & Steel" style="width: 18px; height: 18px; accent-color: var(--gold);"> TMT Bars & Steel</label>
          <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="checkbox" value="Others" id="other-checkbox" style="width: 18px; height: 18px; accent-color: var(--gold);"> Others (Please specify)</label>
      </div>
  </div>
  <input id="other-commodity-input" type="text" placeholder="Please specify your commodity" style="display: none; background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 15px; width: 100%; box-sizing: border-box; color: #fff; margin-bottom: 20px;">"""

content = re.sub(r'<div id="product-checkboxes"[\s\S]*?</div>\s*</div>', new_checkboxes, content)

# update allCheckboxes definition logic to include toggling "Other" input
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
content = content.replace('const allCheckboxes = document.querySelectorAll(\'#product-checkboxes input[type="checkbox"]\');\n\nselectBox.addEventListener', 'const allCheckboxes = document.querySelectorAll(\'#product-checkboxes input[type="checkbox"]\');\n\nselectBox.addEventListener')

content = content.replace('allCheckboxes.forEach(cb => {\n    cb.addEventListener("change", () => {', script_update1)


script_update2 = """  // Handle multiple selections from checkboxes
  const otherInput = document.getElementById("other-commodity-input");
  const selectedProductsRaw = Array.from(document.querySelectorAll('#product-checkboxes input[type="checkbox"]:checked'));
  
  const selectedProducts = selectedProductsRaw.map(cb => {
      if(cb.value === "Others" && otherInput && otherInput.value.trim() !== "") {
          return otherInput.value.trim();
      }
      return cb.value;
  });"""

content = content.replace('  // Handle multiple selections from checkboxes\n  const selectedProducts = Array.from(document.querySelectorAll(\'#product-checkboxes input[type="checkbox"]:checked\')).map(cb => cb.value);', script_update2)


with open('register-supplier.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated successfully.")
