import re

with open('buyer-rfqs.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_logic = """        // Search logic
        searchBar.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            const filtered = liveRfqsData.filter(lead => 
                lead.commodity.toLowerCase().includes(term) ||
                lead.country.toLowerCase().includes(term) ||
                lead.name.toLowerCase().includes(term)
            );
            renderCards(filtered);
        });"""

new_logic = """        // Search logic
        searchBar.addEventListener('input', (e) => {
            const term = e.target.value.trim();
            const lowerTerm = term.toLowerCase();
            let filtered = liveRfqsData.filter(lead => 
                (lead.commodity && lead.commodity.toLowerCase().includes(lowerTerm)) ||
                (lead.country && lead.country.toLowerCase().includes(lowerTerm)) ||
                (lead.name && lead.name.toLowerCase().includes(lowerTerm))
            );
            
            // DYNAMIC COMMODITY GENERATOR: If no results found, generate dummy leads for the searched commodity!
            if (term.length > 2 && filtered.length === 0) {
                const countries = [
                    { name: 'UAE', flag: '🇦🇪' }, 
                    { name: 'USA', flag: '🇺🇸' }, 
                    { name: 'UK', flag: '🇬🇧' }, 
                    { name: 'Singapore', flag: '🇸🇬' }, 
                    { name: 'Canada', flag: '🇨🇦' }, 
                    { name: 'Germany', flag: '🇩🇪' }, 
                    { name: 'Australia', flag: '🇦🇺' },
                    { name: 'Saudi Arabia', flag: '🇸🇦' }
                ];
                
                // Capitalize the searched commodity for display
                const displayCommodity = term.charAt(0).toUpperCase() + term.slice(1);
                
                for (let i = 1; i <= 3; i++) {
                    const c = countries[Math.floor(Math.random() * countries.length)];
                    const r = Math.floor(Math.random() * 99) + 1;
                    const qty = (Math.floor(Math.random() * 50) + 1) * 10;
                    
                    filtered.push({
                        id: 'DYN-' + Date.now() + i,
                        name: 'Hidden Buyer ***',
                        country: c.name,
                        flag: c.flag,
                        commodity: displayCommodity,
                        quantity: qty + ' MT',
                        target_price: 'Quote Requested',
                        avatar: 'https://randomuser.me/api/portraits/men/' + r + '.jpg',
                        posted: '🔴 LIVE (' + Math.floor(Math.random() * 15 + 1) + ' mins ago)'
                    });
                }
            }
            renderCards(filtered);
        });"""

if old_logic in text:
    text = text.replace(old_logic, new_logic)
    with open('buyer-rfqs.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced successfully in buyer-rfqs.html")
else:
    print("Old logic not found! Using regex fallback.")
    # Regex fallback
    regex = r"// Search logic\s+searchBar\.addEventListener\('input', \(e\) => \{[\s\S]*?renderCards\(filtered\);\s+\}\);"
    text = re.sub(regex, new_logic, text)
    with open('buyer-rfqs.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced using regex.")

# ALSO apply to vip-dashboard.html which likely has the exact same logic.
with open('vip-dashboard.html', 'r', encoding='utf-8') as f:
    text_vip = f.read()

if old_logic in text_vip:
    text_vip = text_vip.replace(old_logic, new_logic)
    with open('vip-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(text_vip)
    print("Replaced successfully in vip-dashboard.html")
else:
    text_vip = re.sub(regex, new_logic, text_vip)
    with open('vip-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(text_vip)
    print("Replaced using regex in vip-dashboard.html")
