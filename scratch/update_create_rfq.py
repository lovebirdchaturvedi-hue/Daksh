import os

with open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add fee information to the UI
fee_info = '''    <div style="background: rgba(212, 175, 55, 0.1); border: 1px solid var(--gold); border-radius: 8px; padding: 20px; margin-bottom: 20px;">
        <h4 style="color: var(--gold); margin-top: 0; font-family: 'Playfair Display', serif; font-size: 18px;">Post a Premium Live Order</h4>
        <p style="color: #cbd5e1; font-size: 14px; margin-bottom: 10px;">Reach 14,000+ verified global suppliers instantly. A one-time posting fee applies to ensure high-quality verified requirements.</p>
        <div style="display: flex; gap: 15px; font-weight: bold; font-size: 16px;">
            <span style="color: #4ade80;" class="inr-price">Fee: ₹49,000 INR</span>
            <span style="color: #4ade80;" class="usd-price" style="display:none;">Fee: $499 USD</span>
        </div>
    </div>'''

text = text.replace('<h3>Buyer Contact Details</h3>', fee_info + '\n    <h3>Buyer Contact Details</h3>')

# Add CSS for dual currency in the head if not exists
currency_css = '''<style>
  body.currency-usd .inr-price { display: none !important; }
  body.currency-usd .usd-price { display: inline !important; }
  body.currency-inr .usd-price { display: none !important; }
  body.currency-inr .inr-price { display: inline !important; }
</style>'''

text = text.replace('</head>', currency_css + '\n</head>')


# Update JS logic to redirect to custom-payment.html
old_js = '''    console.log("Saved RFQ ID:", docRef.id);
    alert("🚀 RFQ submitted successfully!");
    e.target.reset();'''

new_js = '''    console.log("Saved RFQ ID:", docRef.id);
    
    // Determine currency and amount
    const isUSD = document.body.classList.contains('currency-usd');
    const amount = isUSD ? 499 : 49000;
    const currency = isUSD ? 'USD' : 'INR';
    
    // Redirect to payment gateway
    window.location.href = `/custom-payment.html?amount=${amount}&currency=${currency}&ref=LiveOrder_${docRef.id}`;'''

text = text.replace(old_js, new_js)

# Fallback for unicode issues
old_js_2 = '''    console.log("Saved RFQ ID:", docRef.id);
    alert("ï¿½o. RFQ submitted successfully!");
    e.target.reset();'''
text = text.replace(old_js_2, new_js)

# Update submit button text
text = text.replace('<button type="submit">Submit Requirement</button>', '<button type="submit" style="background: linear-gradient(90deg, #d4af37, #facc15); color: #000; font-weight: 800; padding: 16px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; width: 100%;">Pay & Post Live Order</button>')
text = text.replace('<button type="submit">Submit RFQ</button>', '<button type="submit" style="background: linear-gradient(90deg, #d4af37, #facc15); color: #000; font-weight: 800; padding: 16px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; width: 100%;">Pay & Post Live Order</button>')

with open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated create-rfq.html')
