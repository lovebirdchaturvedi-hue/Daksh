import os
import re

files1 = ['buyer-rfqs.html', 'vip-dashboard.html', 'supplier-rfqs.html']
for filename in files1:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(
            r'<button class="offer-btn" onclick="document.getElementById\(\'premiumModal\'\).style.display=\'flex\'">Submit Quote</button>',
            r'<button class="offer-btn" onclick="window.location.href=\'/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_\' + lead.id">Unlock Lead ($49)</button>',
            content
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filename}')

if os.path.exists('supplier-dashboard.html'):
    with open('supplier-dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the anchor tag. Since whitespace can vary, we use regex.
    content = re.sub(
        r'<a href="/membership\.html" style="display: block; width: 100%; background: #d4af37; color: #000; text-align: center; padding: 12px; border-radius: 6px; font-weight: 900; text-decoration: none; font-size: 14px; box-shadow: 0 4px 10px rgba\(212, 175, 55, 0\.3\);">\s*⭐ Unlock Buyer Now\s*</a>',
        r'<a href="/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_${lead.id}" style="display: block; width: 100%; background: #d4af37; color: #000; text-align: center; padding: 12px; border-radius: 6px; font-weight: 900; text-decoration: none; font-size: 14px; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.3);">\n                            ⭐ Unlock Lead ($49)\n                        </a>',
        content
    )
    
    with open('supplier-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated supplier-dashboard.html')
