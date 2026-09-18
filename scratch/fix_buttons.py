import os

for filename in ['buyer-rfqs.html', 'vip-dashboard.html', 'supplier-rfqs.html']:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            
        text = text.replace(
            "onclick=\"window.location.href='/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_' + lead.id\">Unlock Lead ($49)</button>",
            "onclick=\"window.location.href='/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_${lead.id}'\">Submit Quote</button>"
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)

if os.path.exists('supplier-dashboard.html'):
    with open('supplier-dashboard.html', 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace(
        '⭐ Unlock Lead ($49)',
        '⭐ Unlock Buyer Now'
    )
    with open('supplier-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(text)

print("Fixed buttons successfully.")
