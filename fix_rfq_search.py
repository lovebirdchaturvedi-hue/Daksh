import re

def fix_search_logic():
    with open('buyer-rfqs.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Store window.latestSnapDocs in loadRFQs
    html = html.replace('renderCards(docs);', 'window.latestSnapDocs = docs;\n          // If there is an active search, filter immediately\n          const qval = searchInput.value.trim().toLowerCase();\n          if (qval) {\n              docs = docs.filter(d => (d.data().product || "").toLowerCase().includes(qval));\n          }\n          renderCards(docs);')

    # 2. Replace the searchInput event listener
    # Let's find everything from // SEARCH LOGIC up to the end of the addEventListener block
    search_logic_new = """      // SEARCH LOGIC (Accurate Client-Side Filtering)
      searchInput.addEventListener("input", () => {
          const queryStr = searchInput.value.trim().toLowerCase();
          if (!window.latestSnapDocs) return;
          
          if (!queryStr) {
              renderCards(window.latestSnapDocs);
              return;
          }
          
          const filteredDocs = window.latestSnapDocs.filter(d => {
              const r = d.data();
              const prod = (r.product || "").toLowerCase();
              const dest = (r.destination || r.deliveryPort || r.country || "").toLowerCase();
              return prod.includes(queryStr) || dest.includes(queryStr);
          });
          
          renderCards(filteredDocs);
      });"""

    # We will use regex to replace the old listener
    # Note: earlier I might have changed it to document.getElementById("searchInput").addEventListener("input", (e) => {
    # So I'll match anything that looks like adding an event listener to searchInput
    pattern = re.compile(r'(searchInput|document\.getElementById\("searchInput"\))\.addEventListener\("input".*?\}\);', re.DOTALL)
    html = pattern.sub(search_logic_new, html)

    # I will also ensure urlParams init is safe
    # It might be in the code twice if I ran fix_buyer_search.py twice, but that's ok.
    
    with open('buyer-rfqs.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed buyer RFQ search logic")

fix_search_logic()
