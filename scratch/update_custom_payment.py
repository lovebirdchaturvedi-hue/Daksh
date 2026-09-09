import re

with open('custom-payment.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Razorpay script
if 'checkout.razorpay.com' not in html:
    html = html.replace('</head>', '  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n</head>')

# Update buttons
old_button = '<button class="btn btn-phonepe" id="payBtn" onclick="initiateCustomPayment()">Authorize Payment</button>'
new_buttons = '''
        <div style="display: flex; gap: 10px; margin-top: 10px;">
            <button class="btn btn-phonepe" id="payBtn" onclick="initiateCustomPayment()" style="flex: 1; font-size: 14px; padding: 15px 10px;">PhonePe (UPI)</button>
            <button class="btn" id="razorpayBtn" onclick="initiateRazorpayCustomPayment()" style="flex: 1; background: #3399cc; color: white; font-size: 14px; padding: 15px 10px; margin-top: 0;">Razorpay (Cards)</button>
        </div>
'''
if old_button in html:
    html = html.replace(old_button, new_buttons)

# Add Razorpay Logo
razorpay_logo = '            <img src="https://razorpay.com/assets/razorpay-logo.svg" alt="Razorpay" height="22" style="filter: grayscale(100%) brightness(200%);">'
if 'razorpay.com/assets' not in html:
    html = html.replace('<img src="https://upload.wikimedia.org/wikipedia/commons/7/71/PhonePe_Logo.svg"', razorpay_logo + '\n            <img src="https://upload.wikimedia.org/wikipedia/commons/7/71/PhonePe_Logo.svg"')


# Add Razorpay JS logic
razorpay_js = '''
        async function initiateRazorpayCustomPayment() {
            const amount = document.getElementById('payAmount').value;
            const refName = document.getElementById('refName').value;
            const btn = document.getElementById('razorpayBtn');
            const status = document.getElementById('statusMsg');

            if (!amount || amount <= 0) {
                status.innerText = "Error: Please enter a valid negotiated amount.";
                status.style.display = "block";
                return;
            }

            if (!refName) {
                status.innerText = "Error: Please enter your Registered Entity Name.";
                status.style.display = "block";
                return;
            }

            btn.innerText = "Processing...";
            btn.disabled = true;
            status.style.display = "none";

            try {
                // Create Order
                const res = await fetch('/api/razorpay-create-order', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ amount: parseInt(amount), currency: 'INR' })
                });
                const data = await res.json();

                if (!res.ok || !data.id) {
                    throw new Error(data.error || 'Failed to create Razorpay order');
                }

                var options = {
                    "key": "rzp_test_TMQmeVth3hlUux",
                    "amount": data.amount,
                    "currency": data.currency,
                    "name": "APD Global Trade",
                    "description": "Elite Custom: " + refName,
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
                                status.innerText = 'Payment verification failed.';
                                status.style.display = 'block';
                            }
                        } catch(e) {
                            status.innerText = 'Error verifying payment.';
                            status.style.display = 'block';
                        }
                    },
                    "theme": { "color": "#3399cc" }
                };
                var rzp1 = new Razorpay(options);
                rzp1.on('payment.failed', function (response){
                    status.innerText = 'Payment failed: ' + response.error.description;
                    status.style.display = 'block';
                    btn.innerText = 'Razorpay (Cards)';
                    btn.disabled = false;
                });
                rzp1.open();
                
                btn.innerText = 'Razorpay (Cards)';
                btn.disabled = false;
            } catch (err) {
                console.error(err);
                btn.innerText = "Razorpay (Cards)";
                btn.disabled = false;
                status.innerText = err.message;
                status.style.display = "block";
            }
        }
'''

if 'initiateRazorpayCustomPayment' not in html:
    html = html.replace('async function initiateCustomPayment() {', razorpay_js + '\n        async function initiateCustomPayment() {')

with open('custom-payment.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated custom-payment.html")
