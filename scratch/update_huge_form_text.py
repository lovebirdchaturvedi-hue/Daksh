import re
import codecs

with codecs.open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure the huge form actually tells them it's a $25 refundable deposit instead of the old sunk cost text
text = re.sub(
    r'<button type="submit" id="submitBtn".*?</button>',
    '<button type="submit" id="submitBtn" style="background: linear-gradient(135deg, #d4af37, #facc15); color: #020617; padding: 18px 40px; border: none; border-radius: 12px; font-size: 1.2rem; font-weight: 800; cursor: pointer; width: 100%; box-shadow: 0 10px 25px rgba(212, 175, 55, 0.4); text-transform: uppercase;">Pay $25 Refundable Deposit & Post Live Order</button>',
    text,
    flags=re.DOTALL
)

# Insert the notification banner explaining the deposit
deposit_banner = """
<div style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); padding: 15px; border-radius: 8px; margin-bottom: 25px; text-align: left;">
    <p style="color: #4ade80; margin: 0; font-size: 1.0rem; font-weight: 700;">✅ Genuine Buyer Verification</p>
    <p style="color: #cbd5e1; margin: 5px 0 0 0; font-size: 0.9rem;">To ensure only serious inquiries, a nominal <strong>$25 USD (or ₹2,000) verification deposit</strong> is required. <span style="color:#facc15; font-weight:700;">This will be 100% REFUNDED or adjusted against your final order.</span></p>
</div>
"""
# Insert it right before the submit button if it's not already there
if 'Genuine Buyer Verification' not in text:
    text = text.replace('<button type="submit"', deposit_banner + '\n<button type="submit"')

with codecs.open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated create-rfq.html text and submit button to reflect $25 fee.")
