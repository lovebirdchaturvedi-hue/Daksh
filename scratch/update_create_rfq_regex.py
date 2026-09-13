import os
import re

with open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the success block
pattern = r'console\.log\("Saved RFQ ID:", docRef\.id\);\s*alert\([^)]+\);\s*e\.target\.reset\(\);'
new_js = '''console.log("Saved RFQ ID:", docRef.id);
    
    // Determine currency and amount
    const isUSD = document.body.classList.contains('currency-usd');
    const amount = isUSD ? 499 : 49000;
    const currency = isUSD ? 'USD' : 'INR';
    
    // Redirect to payment gateway
    window.location.href = `/custom-payment.html?amount=${amount}&currency=${currency}&ref=LiveOrder_${docRef.id}`;'''

text = re.sub(pattern, new_js, text)

with open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated create-rfq.html via regex')
