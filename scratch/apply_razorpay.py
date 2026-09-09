import re

with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Razorpay Script
if 'checkout.razorpay.com' not in html:
    html = html.replace('</head>', '  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n</head>')

# 2. Add Partner Logo
# Look for: "OFFICIAL STRATEGIC PAYMENT PARTNERS"
partner_section_match = re.search(r'OFFICIAL STRATEGIC PAYMENT PARTNERS.*?<img.*?PhonePe.*?<img.*?PayPal.*?>', html, re.DOTALL)
if partner_section_match and 'Razorpay' not in partner_section_match.group(0):
    old_partner = partner_section_match.group(0)
    # We'll just add a text logo for Razorpay or use a generic one if we don't have the image.
    # We can inject a text span styled like a logo, or an img if they have one. Let's use text for Razorpay for now, or just an img tag pointing to Razorpay CDN logo.
    razorpay_logo = '<img src="https://razorpay.com/assets/razorpay-logo.svg" alt="Razorpay" style="height: 35px; filter: brightness(0) invert(1);">'
    # Let's insert it right after the PhonePe image
    new_partner = old_partner + '\n          ' + razorpay_logo
    html = html.replace(old_partner, new_partner)

# 3. Modify Tabs
old_tabs = '''<div id="tab-paypal" onclick="switchPayment('paypal')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; background: var(--gold); color: black; font-weight: 700; font-size: 13px;">PayPal</div>
          <div id="tab-qr" onclick="switchPayment('qr')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; color: #94a3b8; font-weight: 600; font-size: 13px;">PhonePe (Auto)</div>
          <div id="tab-manual" onclick="switchPayment('manual')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; color: #94a3b8; font-weight: 600; font-size: 13px;">Manual QR</div>'''

new_tabs = '''<div id="tab-paypal" onclick="switchPayment('paypal')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; background: var(--gold); color: black; font-weight: 700; font-size: 13px;">PayPal</div>
          <div id="tab-razorpay" onclick="switchPayment('razorpay')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; color: #94a3b8; font-weight: 600; font-size: 13px;">Razorpay</div>
          <div id="tab-qr" onclick="switchPayment('qr')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; color: #94a3b8; font-weight: 600; font-size: 13px;">PhonePe (Auto)</div>
          <div id="tab-manual" onclick="switchPayment('manual')" style="flex: 1; text-align: center; padding: 10px; border-radius: 8px; cursor: pointer; color: #94a3b8; font-weight: 600; font-size: 13px;">Manual QR</div>'''

html = html.replace(old_tabs, new_tabs)

# 4. Add Razorpay Section
razorpay_section = '''
      <!-- RAZORPAY SECTION -->
      <div id="razorpaySection" style="display: none; text-align: center; padding: 0;">
          <div style="background: linear-gradient(135deg, #020617, #0b1d36); padding: 40px; border-radius: 20px; border: 1px solid var(--gold); margin-top: 10px;">
              <h2 style="font-family: 'Playfair Display', serif; color: var(--gold); font-size: 24px; margin-bottom: 5px;">Razorpay Gateway</h2>
              <p style="color: #cbd5e1; font-size: 14px; margin-bottom: 30px;">Cards, UPI, NetBanking & Wallets</p>
              
              <div style="font-size: 2.2rem; font-weight: 800; margin-bottom: 5px; color: #4ade80;" id="modalPriceRazorpay">₹59,000</div>
              <p style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 25px;">(Including 18% GST Compliance)</p>

              <button id="razorpayBtn" class="btn" style="background: #3399cc; color: white; font-size: 1.1rem; padding: 20px; width: 100%; border: 2px solid white; display: flex; align-items: center; justify-content: center; gap: 10px;" onclick="initiateRazorpay()">
                  PAY VIA RAZORPAY
              </button>
              <div id="razorpayError" style="color: #ef4444; margin-top: 15px; font-size: 14px; display: none;"></div>
          </div>
      </div>
'''
if '<!-- RAZORPAY SECTION -->' not in html:
    html = html.replace('<!-- MANUAL QR SECTION -->', razorpay_section + '\n      <!-- MANUAL QR SECTION -->')

# 5. Update initiatePayment to populate modalPriceRazorpay
if 'document.getElementById(\'modalPriceINRManual\').innerText = \'₹\' + inr.toLocaleString();' in html:
    html = html.replace("document.getElementById('modalPriceINRManual').innerText = '₹' + inr.toLocaleString();", "document.getElementById('modalPriceINRManual').innerText = '₹' + inr.toLocaleString();\n        if(document.getElementById('modalPriceRazorpay')) document.getElementById('modalPriceRazorpay').innerText = '₹' + inr.toLocaleString();")

# 6. Update switchPayment logic
old_switch = '''        tPayPal.style.background = 'transparent'; tPayPal.style.color = '#94a3b8';
        tQR.style.background = 'transparent'; tQR.style.color = '#94a3b8';
        tManual.style.background = 'transparent'; tManual.style.color = '#94a3b8';
        sPayPal.style.display = 'none';
        sQR.style.display = 'none';
        sManual.style.display = 'none';

        if (method === 'paypal') {
            tPayPal.style.background = 'var(--gold)'; tPayPal.style.color = 'black';
            sPayPal.style.display = 'block';
        } else if (method === 'qr') {
            tQR.style.background = 'var(--gold)'; tQR.style.color = 'black';
            sQR.style.display = 'block';
        } else {
            tManual.style.background = 'var(--gold)'; tManual.style.color = 'black';
            sManual.style.display = 'block';
        }'''

new_switch = '''        const tRazorpay = document.getElementById('tab-razorpay');
        const sRazorpay = document.getElementById('razorpaySection');
        
        tPayPal.style.background = 'transparent'; tPayPal.style.color = '#94a3b8';
        if(tRazorpay) { tRazorpay.style.background = 'transparent'; tRazorpay.style.color = '#94a3b8'; }
        tQR.style.background = 'transparent'; tQR.style.color = '#94a3b8';
        tManual.style.background = 'transparent'; tManual.style.color = '#94a3b8';
        
        sPayPal.style.display = 'none';
        if(sRazorpay) { sRazorpay.style.display = 'none'; }
        sQR.style.display = 'none';
        sManual.style.display = 'none';

        if (method === 'paypal') {
            tPayPal.style.background = 'var(--gold)'; tPayPal.style.color = 'black';
            sPayPal.style.display = 'block';
        } else if (method === 'razorpay') {
            if(tRazorpay) { tRazorpay.style.background = 'var(--gold)'; tRazorpay.style.color = 'black'; }
            if(sRazorpay) { sRazorpay.style.display = 'block'; }
        } else if (method === 'qr') {
            tQR.style.background = 'var(--gold)'; tQR.style.color = 'black';
            sQR.style.display = 'block';
        } else {
            tManual.style.background = 'var(--gold)'; tManual.style.color = 'black';
            sManual.style.display = 'block';
        }'''

html = html.replace(old_switch, new_switch)

# Default to Razorpay instead of QR if currentCurrency is INR
if "if (currentCurrency === 'INR') { switchPayment('qr'); } else { switchPayment('paypal'); }" in html:
    html = html.replace("if (currentCurrency === 'INR') { switchPayment('qr'); } else { switchPayment('paypal'); }", "if (currentCurrency === 'INR') { switchPayment('razorpay'); } else { switchPayment('paypal'); }")


# 7. Add initiateRazorpay JS function
razorpay_js = '''
    async function initiateRazorpay() {
        const btn = document.getElementById('razorpayBtn');
        const err = document.getElementById('razorpayError');
        btn.innerText = 'Processing...';
        btn.disabled = true;
        err.style.display = 'none';

        try {
            // 1. Create Order
            const res = await fetch('/api/razorpay-create-order', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ amount: selectedPlan.inr, currency: 'INR' })
            });
            const data = await res.json();

            if (!res.ok || !data.id) {
                throw new Error(data.error || 'Failed to create Razorpay order');
            }

            // 2. Open Razorpay Checkout
            var options = {
                "key": "rzp_test_TMQmeVth3hlUux", // We pass the key_id to the frontend
                "amount": data.amount,
                "currency": data.currency,
                "name": "APD Global Trade",
                "description": selectedPlan.name,
                "order_id": data.id,
                "handler": async function (response) {
                    try {
                        const verifyRes = await fetch('/api/razorpay-verify', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({
                                razorpay_order_id: response.razorpay_order_id,
                                razorpay_payment_id: response.razorpay_payment_id,
                                razorpay_signature: response.razorpay_signature
                            })
                        });
                        const verifyData = await verifyRes.json();
                        if (verifyData.success) {
                            window.location.href = '/payment-status.html';
                        } else {
                            err.innerText = 'Payment verification failed.';
                            err.style.display = 'block';
                        }
                    } catch(e) {
                        err.innerText = 'Error verifying payment.';
                        err.style.display = 'block';
                    }
                },
                "theme": {
                    "color": "#3399cc"
                }
            };
            var rzp1 = new Razorpay(options);
            rzp1.on('payment.failed', function (response){
                err.innerText = 'Payment failed: ' + response.error.description;
                err.style.display = 'block';
                btn.innerText = 'PAY VIA RAZORPAY';
                btn.disabled = false;
            });
            rzp1.open();
            
            // Re-enable button after opening modal
            btn.innerText = 'PAY VIA RAZORPAY';
            btn.disabled = false;
        } catch(e) { 
            err.innerText = e.message || 'Network error.'; 
            err.style.display = 'block'; 
            btn.innerText = 'PAY VIA RAZORPAY'; 
            btn.disabled = false; 
        }
    }
'''

if 'async function initiateRazorpay()' not in html:
    html = html.replace('async function initiatePhonePe() {', razorpay_js + '\n    async function initiatePhonePe() {')

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Razorpay frontend integration applied.")
