import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the Modal text to explain the Refundable Deposit
old_text = '<p style="color: #94a3b8; margin-bottom: 10px; font-size: 0.95rem;">Instantly broadcast your buy requirement to our vetted suppliers.</p>'
new_text = '''<p style="color: #94a3b8; margin-bottom: 10px; font-size: 0.95rem;">Instantly broadcast your buy requirement to our vetted suppliers.</p>
<div style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); padding: 12px; border-radius: 8px; margin-bottom: 15px;">
    <p style="color: #4ade80; margin: 0; font-size: 0.85rem; font-weight: 600;"><i class="fas fa-shield-alt"></i> Genuine Buyer Verification</p>
    <p style="color: #cbd5e1; margin: 5px 0 0 0; font-size: 0.8rem;">To ensure only serious inquiries, a nominal <strong>$25 USD (or ₹2,000) verification deposit</strong> is required. <span style="color:#facc15; font-weight:700;">This will be 100% REFUNDED or adjusted against your final order.</span></p>
</div>'''
text = text.replace(old_text, new_text)


# 2. Update the JS handler to redirect to payment
# I need to find the `window.handleQuickRFQ = async function(e)` block and replace it.
old_js_start = text.find('window.handleQuickRFQ = async function(e) {')
old_js_end = text.find('};', old_js_start) + 2

if old_js_start != -1 and old_js_end != -1:
    new_js = """window.handleQuickRFQ = async function(e) {
        e.preventDefault();
        const btn = document.getElementById("qr_btn");
        btn.innerText = "Securing Order...";
        btn.disabled = true;

        const product = document.getElementById("qr_product").value;
        const qty = document.getElementById("qr_qty").value + " " + document.getElementById("qr_unit").value;
        const dest = document.getElementById("qr_dest").value;

        try {
            // Save it to Firebase as pending
            const docRef = await addDoc(collection(db, "rfqs"), {
                buyerName: document.getElementById("qr_name").value,
                company: document.getElementById("qr_company").value,
                whatsapp: document.getElementById("qr_whatsapp").value,
                product: product,
                quantity: qty,
                destination: dest,
                specifications: document.getElementById("qr_specs").value,
                status: "payment_pending",
                source: "homepage_quick",
                deposit: "refundable",
                createdAt: serverTimestamp()
            });

            // Redirect to custom payment for the refundable deposit
            const isUSD = document.body.classList && document.body.classList.contains('currency-usd');
            const amount = isUSD ? 25 : 2000;
            const currency = isUSD ? 'USD' : 'INR';
            
            // Redirect to the payment page
            window.location.href = `/custom-payment.html?amount=${amount}&currency=${currency}&ref=LiveOrderDeposit_${docRef.id}`;
            return;
        } catch (err) {
            alert('Error initiating verification: ' + err.message);
            btn.innerText = "Pay $25 Refundable Deposit & Post";
            btn.disabled = false;
        }
    };"""
    
    text = text[:old_js_start] + new_js + text[old_js_end:]
else:
    print("Could not find handleQuickRFQ")

# 3. Update the submit button text in the modal
text = text.replace('id="qr_btn" style="background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; padding: 15px; border: none; border-radius: 10px; font-size: 1.1rem; cursor: pointer; text-transform: uppercase; margin-top: 10px; transition: 0.3s; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3);">Post Live Order</button>', 
                    'id="qr_btn" style="background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; padding: 15px; border: none; border-radius: 10px; font-size: 1.1rem; cursor: pointer; text-transform: uppercase; margin-top: 10px; transition: 0.3s; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3);">Pay $25 Refundable Deposit</button>')
# Handle the case where it might already say "Pay & Post Live Order" or similar from earlier modifications
text = text.replace('Pay & Post Live Order</button>', 'Pay $25 Refundable Deposit</button>')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html with refundable deposit logic!")
