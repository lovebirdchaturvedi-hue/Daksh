import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the subheading to include the live viewer count
old_subheading = '<p style="color: #94a3b8; margin-bottom: 30px; font-size: 0.95rem;">Instantly broadcast your buy requirement to our vetted suppliers.</p>'
new_subheading = '''<p style="color: #94a3b8; margin-bottom: 10px; font-size: 0.95rem;">Instantly broadcast your buy requirement to our vetted suppliers.</p>
<div style="margin-bottom: 25px; padding: 10px; background: rgba(220, 38, 38, 0.1); border: 1px solid rgba(220, 38, 38, 0.3); border-radius: 8px; display: flex; align-items: center; gap: 10px;">
    <span style="display: inline-block; width: 8px; height: 8px; background: #ef4444; border-radius: 50%; box-shadow: 0 0 8px #ef4444; animation: pulse 1.5s infinite;"></span>
    <span style="color: #fca5a5; font-size: 13px; font-weight: 600;" id="liveViewerCount">-- Exporters currently active and ready to quote</span>
</div>
<script>
    // Random viewer count logic (sometimes over 1000)
    document.addEventListener("DOMContentLoaded", function() {
        const countEl = document.getElementById("liveViewerCount");
        if(countEl) {
            const isHigh = Math.random() > 0.7; // 30% chance to be over 1000
            const count = isHigh ? Math.floor(Math.random() * 500) + 1000 : Math.floor(Math.random() * 800) + 100;
            countEl.innerText = count.toLocaleString() + " Exporters currently active and ready to quote";
        }
    });
</script>
'''

text = text.replace(old_subheading, new_subheading)

# Update the button text
text = text.replace('Broadcast RFQ', 'Pay & Post Live Order')

# Replace the JS function logic
old_js = '''            const docRef = await addDoc(collection(db, "rfqs"), {
                buyerName: document.getElementById("qr_name").value,
                company: document.getElementById("qr_company").value,
                whatsapp: document.getElementById("qr_whatsapp").value,
                product: document.getElementById("qr_product").value,
                quantity: document.getElementById("qr_qty").value + " " + document.getElementById("qr_unit").value,
                destination: document.getElementById("qr_dest").value,
                specifications: document.getElementById("qr_specs").value,
                status: "open",
                source: "homepage_quick",
                createdAt: serverTimestamp()
            });
            alert('RFQ Posted Successfully! Suppliers will be notified.');
            document.getElementById('rfqModal').style.display='none';
            e.target.reset();'''

new_js = '''            const docRef = await addDoc(collection(db, "rfqs"), {
                buyerName: document.getElementById("qr_name").value,
                company: document.getElementById("qr_company").value,
                whatsapp: document.getElementById("qr_whatsapp").value,
                product: document.getElementById("qr_product").value,
                quantity: document.getElementById("qr_qty").value + " " + document.getElementById("qr_unit").value,
                destination: document.getElementById("qr_dest").value,
                specifications: document.getElementById("qr_specs").value,
                status: "payment_pending",
                source: "homepage_quick",
                createdAt: serverTimestamp()
            });
            
            // Redirect to payment gateway
            const isUSD = document.body.classList && document.body.classList.contains('currency-usd');
            const amount = isUSD ? 499 : 49000;
            const currency = isUSD ? 'USD' : 'INR';
            
            window.location.href = `/custom-payment.html?amount=${amount}&currency=${currency}&ref=LiveOrder_${docRef.id}`;
            return; // Exit here so it doesn't alert or reset'''

# Because there was no const docRef = in original code, I should use regex
pattern = r'await addDoc\(collection\(db, "rfqs"\), \{.*?\n\s*createdAt: serverTimestamp\(\)\n\s*\}\);\s*alert\([\'"]RFQ Posted.*?[\'"]\);\s*document\.getElementById\([\'"]rfqModal[\'"]\)\.style\.display=[\'"]none[\'"];\s*e\.target\.reset\(\);'
import re
# Wait, it's safer to just replace by block
old_js_exact = """            await addDoc(collection(db, "rfqs"), {
                buyerName: document.getElementById("qr_name").value,
                company: document.getElementById("qr_company").value,
                whatsapp: document.getElementById("qr_whatsapp").value,
                product: document.getElementById("qr_product").value,
                quantity: document.getElementById("qr_qty").value + " " + document.getElementById("qr_unit").value,
                destination: document.getElementById("qr_dest").value,
                specifications: document.getElementById("qr_specs").value,
                status: "open",
                source: "homepage_quick",
                createdAt: serverTimestamp()
            });
            alert('RFQ Posted Successfully! Suppliers will be notified.');
            document.getElementById('rfqModal').style.display='none';
            e.target.reset();"""

if old_js_exact in text:
    text = text.replace(old_js_exact, new_js)
else:
    print("WARNING: Could not find exact JS block to replace")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html modal logic')
