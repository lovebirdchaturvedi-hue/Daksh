import re
with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script blocks to see the initiatePayment function and modal logic
script_matches = re.findall(r'<script.*?>.*?</script>', html, re.DOTALL)
out = []
for m in script_matches:
    if 'initiatePayment' in m:
        out.append(m)

# Also extract the payment modal HTML if it exists
modal_match = re.search(r'<div id="paymentModal".*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if modal_match:
    out.append(modal_match.group(0))

with open('scratch/initiate_payment_logic.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n---SCRIPT---\n\n'.join(out))
