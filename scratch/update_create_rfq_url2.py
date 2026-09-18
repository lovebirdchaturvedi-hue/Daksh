import re

with open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('ref=LiveOrder_${docRef.id}', 'ref=LiveOrderDeposit_${docRef.id}')
# Also make sure the amount is 25 USD / 2000 INR
text = re.sub(r'const amount = isUSD \? \d+ : \d+;', 'const amount = isUSD ? 25 : 2000;', text)

with open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated create-rfq.html to use LiveOrderDeposit and $25 fee")
