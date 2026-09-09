import os

filepath = 'vip-dashboard.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Membership Modal with a Bid Form Modal
old_modal = """
    <!-- MEMBERSHIP PAYWALL MODAL -->
    <div class="modal-overlay" id="membershipModal" onclick="if(event.target==this) this.style.display='none'">
        <div class="modal-content">
            <h2 class="modal-title">Verified Members Only</h2>
            <p style="color: #cbd5e1; margin-bottom: 20px; font-size: 0.95rem; line-height: 1.5;">You must be a Verified Supplier Member to unlock direct buyer contact details and submit competitive bids on live RFQs.</p>
            <div style="background: rgba(250, 204, 21, 0.1); border: 1px solid rgba(250, 204, 21, 0.3); padding: 15px; border-radius: 8px; margin-bottom: 25px;">
                <p style="color: #facc15; font-weight: 700; margin-bottom: 8px; font-size: 0.9rem;">⭐ Premium Benefits Include:</p>
                <ul style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6; padding-left: 20px;">
                    <li>Instant access to Buyer phone & WhatsApp</li>
                    <li>Ability to send direct quotes</li>
                    <li>Bypass middle-man commissions</li>
                </ul>
            </div>
            <div style="display: flex; gap: 15px; justify-content: flex-end;">
                <button onclick="document.getElementById('membershipModal').style.display='none'" class="close-btn">Cancel</button>
                <a href="/membership.html" class="unlock-btn">Unlock Membership</a>
            </div>
        </div>
    </div>
"""

new_modal = """
    <!-- SUBMIT BID MODAL -->
    <div class="modal-overlay" id="bidModal" onclick="if(event.target==this) this.style.display='none'">
        <div class="modal-content" style="max-width: 500px;">
            <h2 class="modal-title">Submit Your Quote</h2>
            <p style="color: #cbd5e1; margin-bottom: 20px; font-size: 0.95rem; line-height: 1.5;">Submit your best price for this Live Order. The buyer will receive your quote instantly.</p>
            
            <form action="mailto:sales@apdglobaltrade.com" method="GET" enctype="text/plain" style="display: flex; flex-direction: column; gap: 15px;">
                <input type="hidden" name="subject" value="New Bid Submitted via VIP Dashboard">
                <div>
                    <label style="color: #94a3b8; font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; display: block;">Your Company Name</label>
                    <input type="text" name="Company Name" required style="width: 100%; background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); padding: 12px; border-radius: 6px; color: #fff; outline: none; font-family: 'Plus Jakarta Sans', sans-serif;">
                </div>
                <div style="display: flex; gap: 15px;">
                    <div style="flex: 1;">
                        <label style="color: #94a3b8; font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; display: block;">Your Email</label>
                        <input type="email" name="Email" required style="width: 100%; background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); padding: 12px; border-radius: 6px; color: #fff; outline: none; font-family: 'Plus Jakarta Sans', sans-serif;">
                    </div>
                    <div style="flex: 1;">
                        <label style="color: #94a3b8; font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; display: block;">WhatsApp Number</label>
                        <input type="text" name="WhatsApp" required style="width: 100%; background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); padding: 12px; border-radius: 6px; color: #fff; outline: none; font-family: 'Plus Jakarta Sans', sans-serif;">
                    </div>
                </div>
                <div>
                    <label style="color: #facc15; font-size: 0.85rem; font-weight: 700; margin-bottom: 6px; display: block;">Your Price Quote (USD)</label>
                    <input type="text" name="Price Quote USD" placeholder="e.g. $450 / MT" required style="width: 100%; background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(250, 204, 21, 0.4); padding: 12px; border-radius: 6px; color: #facc15; outline: none; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700;">
                </div>
                <div>
                    <label style="color: #94a3b8; font-size: 0.85rem; font-weight: 600; margin-bottom: 6px; display: block;">Additional Details (Optional)</label>
                    <textarea name="Message" rows="3" style="width: 100%; background: rgba(2, 6, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); padding: 12px; border-radius: 6px; color: #fff; outline: none; font-family: 'Plus Jakarta Sans', sans-serif; resize: none;"></textarea>
                </div>
                <div style="display: flex; gap: 15px; justify-content: flex-end; margin-top: 10px;">
                    <button type="button" onclick="document.getElementById('bidModal').style.display='none'" class="close-btn">Cancel</button>
                    <button type="submit" class="unlock-btn" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: #fff; border: none; padding: 10px 24px; border-radius: 8px; font-weight: 700; cursor: pointer; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);">Send Quote</button>
                </div>
            </form>
        </div>
    </div>
"""

content = content.replace(old_modal, new_modal)

# Update the JS onclick function
old_js = """function showMembershipModal() {
        document.getElementById('membershipModal').style.display = 'flex';
    }"""
new_js = """function showMembershipModal() {
        document.getElementById('bidModal').style.display = 'flex';
    }"""
content = content.replace(old_js, new_js)

# Update page titles to VIP Dashboard
content = content.replace("<title>Live Buyer RFQs | APD Global Trade</title>", "<title>VIP Bidding Dashboard | APD Global Trade</title>")
content = content.replace("<h1>Live Global <span class=\"highlight\">Buyer Orders</span></h1>", "<h1>VIP <span class=\"highlight\">Bidding Dashboard</span></h1>")
content = content.replace("<p class=\"subtitle\">Browse active requirements from 500+ verified global institutional buyers. Unlock membership to bid directly.</p>", "<p class=\"subtitle\">Welcome to the VIP Member Dashboard. Submit your direct quotes to our 1,500+ verified global institutional buyers below.</p>")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated vip-dashboard.html')
