import re

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We want to replace everything from the start of the pricing section until the end of the pricing area.
# Let's locate the main pricing grid container.
# In membership.html, the pricing grid starts around line 865: <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin-bottom: 50px;">
# And it goes all the way down.

# We will just rewrite membership.html using a clean split.
parts = text.split('<!-- MAIN PRICING TIERS -->')
if len(parts) > 1:
    before_pricing = parts[0]
    
    # Where does the pricing end? Let's say right before "<!-- WHY CHOOSE APD SECTION -->" or similar.
    parts2 = text.split('<!-- MANUAL PAYMENT SECTION -->')
    if len(parts2) > 1:
        after_pricing = '<!-- MANUAL PAYMENT SECTION -->' + parts2[1]
    else:
        after_pricing = '<!-- FOOTER -->' + text.split('<!-- FOOTER -->')[1]

    new_pricing_html = """<!-- MAIN PRICING TIERS -->
    <div style="max-width: 1300px; margin: 0 auto; padding: 60px 5%;">
        <div style="text-align: center; margin-bottom: 50px;">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 3.5rem; color: var(--gold); margin-bottom: 20px;">Choose Your Access Level</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 800px; margin: 0 auto;">Transparent, straightforward pricing to unlock verified international trade leads. No hidden fees.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin-bottom: 50px;">
            <!-- 3 MONTHS -->
            <div style="background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                <h3 style="font-size: 26px; margin-bottom: 10px; color: #6ab0f5;">3 Months Access</h3>
                <p style="color: #94a3b8; font-size: 15px; margin-bottom: 20px; line-height: 1.6;">Perfect for testing the waters and verifying institutional buyers.</p>
                <div style="margin-bottom: 25px;">
                    <span class="price-display usd-price" style="font-size: 48px; font-weight: 900; color: #fff;">$499</span>
                    <span class="price-display inr-price" style="font-size: 48px; font-weight: 900; color: #fff; display:none;">₹49,000</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0 0 30px; color: #e2e8f0; font-size: 15px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Full Access for 3 Months</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Direct WhatsApp & Email Unlocks</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Daily RFQ Notifications</span></li>
                </ul>
                <button class="btn" style="margin-top: auto; background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: #fff; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('3 Months Access', 499, 49000)">Get 3 Months Access</button>
            </div>

            <!-- 6 MONTHS -->
            <div style="background: linear-gradient(180deg, rgba(30,41,59,0.8), rgba(15,23,42,0.95)); border: 2px solid var(--gold); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; position: relative; box-shadow: 0 20px 50px rgba(212,175,55,0.15); transform: translateY(-10px);">
                <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); background: var(--gold); color: #000; font-weight: 800; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; padding: 6px 20px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;">Most Popular</div>
                <h3 style="font-size: 26px; margin-bottom: 5px; color: var(--gold);">6 Months Access</h3>
                <p style="color: #cbd5e1; font-size: 15px; margin-bottom: 20px; line-height: 1.6;">Ideal for serious exporters looking to build consistent trade relations.</p>
                <div style="margin-bottom: 25px;">
                    <span class="price-display usd-price" style="font-size: 48px; font-weight: 900; color: #fff;">$899</span>
                    <span class="price-display inr-price" style="font-size: 48px; font-weight: 900; color: #fff; display:none;">₹89,000</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0 0 30px; color: #e2e8f0; font-size: 15px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Full Access for 6 Months</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Direct WhatsApp & Email Unlocks</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Dedicated CRM Dashboard</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Priority Support</span></li>
                </ul>
                <button class="btn" style="margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s; margin-bottom: 15px;" onclick="initiatePayment('6 Months Access', 899, 89000)">Get 6 Months Access</button>
            </div>

            <!-- 12 MONTHS -->
            <div style="background: rgba(30, 41, 59, 0.4); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 40px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
                <h3 style="font-size: 26px; margin-bottom: 10px; color: #fff;">12 Months Access</h3>
                <p style="color: #94a3b8; font-size: 15px; margin-bottom: 20px; line-height: 1.6;">Maximum value for long-term export scaling and large-volume trading.</p>
                <div style="margin-bottom: 25px;">
                    <span class="price-display usd-price" style="font-size: 48px; font-weight: 900; color: #fff;">$1,499</span>
                    <span class="price-display inr-price" style="font-size: 48px; font-weight: 900; color: #fff; display:none;">₹149,000</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0 0 30px; color: #e2e8f0; font-size: 15px;">
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Full Access for 12 Months</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Direct WhatsApp & Email Unlocks</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Dedicated CRM Dashboard</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>Unlimited Live Order Access</span></li>
                    <li style="margin-bottom: 15px; display: flex; align-items: flex-start; gap: 10px;">✅ <span>1-on-1 Account Manager</span></li>
                </ul>
                <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #fff; color: #fff; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('12 Months Access', 1499, 149000)">Get 12 Months Access</button>
            </div>
        </div>
    </div>
    """
    
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(before_pricing + new_pricing_html + after_pricing)
    
    print("Successfully replaced pricing tiers in membership.html")
else:
    print("Could not split by MAIN PRICING TIERS")
