import re

def fix_buyer_search():
    with open('buyer-rfqs.html', 'r', encoding='utf-8') as f:
        html = f.read()

    js_logic = """
      // SEARCH LOGIC (Accurate Client-Side Filtering)
      
      function applySearch(queryStr) {
          queryStr = queryStr.trim().toLowerCase();
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
      }

      // 1. Initial Load from URL Parameters
      const urlParams = new URLSearchParams(window.location.search);
      const initialQuery = urlParams.get('q');
      if (initialQuery) {
          searchInput.value = initialQuery;
          // Apply after a short delay to ensure docs are loaded
          setTimeout(() => applySearch(initialQuery), 500);
          setTimeout(() => applySearch(initialQuery), 1500); // safety fallback
      }

      // 2. Real-time typing
      searchInput.addEventListener("input", () => {
          applySearch(searchInput.value);
      });
"""
    
    # Replace the existing search logic from "// SEARCH LOGIC (Accurate Client-Side Filtering)" to "renderCards(filteredDocs);\n      });"
    html = re.sub(
        r'// SEARCH LOGIC \(Accurate Client-Side Filtering\).*?renderCards\(filteredDocs\);\n      }\);',
        js_logic,
        html,
        flags=re.DOTALL
    )

    with open('buyer-rfqs.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed buyer rfqs search logic")

fix_buyer_search()
