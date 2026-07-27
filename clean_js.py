import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire toggleCurrency function
old_func_pattern = re.compile(r'function toggleCurrency\(\) \{.*?\}(?=\n\n    function initiatePayment)', re.DOTALL)

clean_func = '''function toggleCurrency() {
        currentCurrency = currentCurrency === 'USD' ? 'INR' : 'USD';
        const knob = document.getElementById('toggle-knob');
        const lUSD = document.getElementById('label-usd');
        const lINR = document.getElementById('label-inr');
        
        document.body.classList.remove('currency-inr', 'currency-usd');
        document.body.classList.add(currentCurrency === 'INR' ? 'currency-inr' : 'currency-usd');

        if (currentCurrency === 'INR') {
            knob.style.left = '32px';
            lINR.style.opacity = '1';
            lINR.style.fontWeight = '700';
            lINR.style.color = 'var(--gold)';
            lUSD.style.opacity = '0.6';
            lUSD.style.fontWeight = '400';
            lUSD.style.color = '#fff';
        } else {
            knob.style.left = '2px';
            lUSD.style.opacity = '1';
            lUSD.style.fontWeight = '700';
            lUSD.style.color = 'var(--gold)';
            lINR.style.opacity = '0.6';
            lINR.style.fontWeight = '400';
            lINR.style.color = '#fff';
        }
    }'''

html = old_func_pattern.sub(clean_func, html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("JS cleaned up.")
