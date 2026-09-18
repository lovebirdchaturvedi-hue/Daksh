import re

with open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure it redirects as LiveOrderDeposit
old_url = 'window.location.href = `/custom-payment.html?amount=${amount}&currency=${currency}&ref=RFQ_${docRef.id}`;'
new_url = 'window.location.href = `/custom-payment.html?amount=${amount}&currency=${currency}&ref=LiveOrderDeposit_${docRef.id}`;'

if old_url in text:
    text = text.replace(old_url, new_url)
    with open('create-rfq.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated create-rfq.html redirect to use LiveOrderDeposit")
else:
    print("Redirect string not found in create-rfq.html. Checking if it's already updated.")
