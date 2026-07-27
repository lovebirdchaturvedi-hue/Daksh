import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Fix Hardcoded USD Pricing in index.html to include INR
index_html = index_html.replace(
    '<div class="plan-price">$499</div>',
    '<div class="plan-price"><span style="font-size: 0.6em; color: #9ca3af;">₹19,999 | </span>$499</div>'
)
index_html = index_html.replace(
    '<div class="plan-price">$2,000</div>',
    '<div class="plan-price"><span style="font-size: 0.6em; color: #9ca3af;">₹84,999 | </span>$2,000</div>'
)
index_html = index_html.replace(
    '<div class="plan-price">$3,500</div>',
    '<div class="plan-price"><span style="font-size: 0.6em; color: #9ca3af;">₹1,49,999 | </span>$3,500</div>'
)

# 2. Remove Guarantees/Refunds from index.html
guarantees_block = """<div style="margin-top: 80px; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">
            <div style="max-width: 300px;">
                <h3 style="color: var(--gold); margin-bottom: 10px;">🛡️ 48-Hour RFQ Guarantee</h3>
                <p style="font-size: 0.9rem; color: #94a3b8;">Receive your first matched buyer inquiry within 48 hours of verification or we extend your support free.</p>
            </div>
            <div style="max-width: 300px;">
                <h3 style="color: var(--gold); margin-bottom: 10px;">🔒 No Commitment</h3>
                <p style="font-size: 0.9rem; color: #94a3b8;">Try the platform for 3 months with no auto-renewal. Pay only for the value you receive.</p>
            </div>
        </div>"""

replacement_block = """<div style="margin-top: 80px; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">
            <div style="max-width: 300px;">
                <h3 style="color: var(--gold); margin-bottom: 10px;">🛡️ Secure Escrow Partnerships</h3>
                <p style="font-size: 0.9rem; color: #94a3b8;">All subscriptions are processed via secured 256-bit institutional payment gateways (Stripe/Razorpay).</p>
            </div>
            <div style="max-width: 300px;">
                <h3 style="color: var(--gold); margin-bottom: 10px;">🔒 Zero Commission</h3>
                <p style="font-size: 0.9rem; color: #94a3b8;">We strictly operate on a membership model. No hidden fees, no broker cuts, and no refund policies—pure direct trade.</p>
            </div>
        </div>"""

index_html = index_html.replace(guarantees_block, replacement_block)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# 3. Remove 14-Day Money-Back Guarantee from membership.html
mem_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"
with open(mem_path, "r", encoding="utf-8") as f:
    mem_html = f.read()

mem_html = mem_html.replace(
    '<span style="font-size: 14px; font-weight: 600;">14-Day Money-Back Guarantee</span>',
    '<span style="font-size: 14px; font-weight: 600;">Zero Commission & Direct Trade</span>'
)
mem_html = mem_html.replace(
    '<span style="font-size: 14px; font-weight: 600;">Trade Assurance Active</span>',
    '<span style="font-size: 14px; font-weight: 600;">Zero Commission & Direct Trade</span>'
)

with open(mem_path, "w", encoding="utf-8") as f:
    f.write(mem_html)
