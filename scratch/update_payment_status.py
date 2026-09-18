import re

with open('payment-status.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to change the else block in payment-status.html to handle LiveOrderDeposit
old_js = """
    } else {
        card.innerHTML = `
            <h1>Verification in Progress ⏳</h1>
"""

new_js = """
    } else if (code === 'PAYMENT_SUCCESS' && urlParams.get('ref') && urlParams.get('ref').includes('LiveOrderDeposit')) {
        card.innerHTML = `
            <h1 style="color: #4ade80;">Payment Successful! 🎉</h1>
            <p style="font-size: 16px;">Your $25 Refundable Verification Deposit was processed successfully.</p>
            <div style="background: rgba(34, 197, 94, 0.1); padding: 25px; border-radius: 15px; margin-top: 20px; border: 1px solid rgba(34, 197, 94, 0.3);">
                <p style="margin: 0; color: #fff;">Your Live Order is now officially <strong>Active and Broadcasting</strong> to our network of verified suppliers.</p>
            </div>
            <a href="/buyer-rfqs.html" class="btn" style="background: #22c55e; color: white;">View Live Orders Dashboard</a>
        `;
    } else {
        card.innerHTML = `
            <h1>Verification in Progress ⏳</h1>
"""

text = text.replace(old_js, new_js)

with open('payment-status.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated payment-status.html logic for LiveOrderDeposit.")
