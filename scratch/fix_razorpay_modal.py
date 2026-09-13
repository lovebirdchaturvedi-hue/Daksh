import os

filepath = 'membership.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_line = "if(document.getElementById('modalPriceRazorpay')) document.getElementById('modalPriceRazorpay').innerText = '₹' + inr.toLocaleString();"
new_lines = """if(document.getElementById('modalPriceRazorpay')) {
            if (currentCurrency === 'USD') {
                document.getElementById('modalPriceRazorpay').innerText = '$' + usd.toLocaleString();
            } else {
                document.getElementById('modalPriceRazorpay').innerText = '₹' + inr.toLocaleString();
            }
        }"""

if old_line in content:
    content = content.replace(old_line, new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed Razorpay modal price update logic in membership.html")
else:
    print("Could not find the target line to replace in membership.html")
