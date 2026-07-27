import re

with open('register-supplier.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the search input right after the div opens, if it's not already there
if 'id="commodity-search"' not in html:
    html = html.replace(
        '<div id="product-checkboxes" style="display: none; position: absolute; top: 100%; left: 0; right: 0; background: #0f172a; border: 1px solid var(--gold); border-radius: 8px; padding: 15px; max-height: 300px; overflow-y: auto; z-index: 100; margin-top: 5px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); flex-direction: column; gap: 12px; color: #fff;">',
        '<div id="product-checkboxes" style="display: none; position: absolute; top: 100%; left: 0; right: 0; background: #0f172a; border: 1px solid var(--gold); border-radius: 8px; padding: 15px; max-height: 300px; overflow-y: auto; z-index: 100; margin-top: 5px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); flex-direction: column; gap: 12px; color: #fff;">\n          <input type="text" id="commodity-search" placeholder="Search your product..." style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: rgba(0,0,0,0.3); color: #fff; width: 100%; box-sizing: border-box; margin-bottom: 10px;" onclick="event.stopPropagation();">'
    )

# Add the JavaScript to handle the search
search_js = """
// Search logic
const searchInput = document.getElementById("commodity-search");
if (searchInput) {
    searchInput.addEventListener("input", function(e) {
        const filter = e.target.value.toLowerCase();
        const labels = checkboxesDiv.querySelectorAll("label");
        labels.forEach(label => {
            if (label.innerText.toLowerCase().includes(filter)) {
                label.style.display = "flex";
            } else {
                label.style.display = "none";
            }
        });
    });
}
"""

if 'const searchInput = document.getElementById("commodity-search");' not in html:
    # Insert it right before the allCheckboxes.forEach loop
    html = html.replace(
        'allCheckboxes.forEach(cb => {',
        search_js + '\nallCheckboxes.forEach(cb => {'
    )

with open('register-supplier.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Search bar added successfully!")
