import os

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div id="tab-memberships"')
end_idx = text.find('<!-- PAYMENT PARTNERS SECTION -->')

if end_idx == -1: 
    end_idx = text.find('<!-- FOOTER')

if start_idx != -1 and end_idx != -1:
    new_pricing = '''<div id="tab-memberships" class="tab-content active">
        <div class="plans" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
            
            <!-- 3 MONTH PLAN -->
            <div class="plan" style="display: flex; flex-direction: column; background: #111827; border: 1px solid rgba(255,255,255,0.05); padding: 40px; border-radius: 20px; text-align: left;">
                <h3 style="font-size: 26px; margin-bottom: 10px; color: #6ab0f5;">3 Months Access</h3>
                <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">Perfect for testing the institutional network.</p>
                <div class="price" style="font-size: 42px; color: #fff; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                    <span class="show-usd">$499</span>
                    <span class="show-inr">₹49,000</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 30px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">
                    <li style="margin-bottom: 15px;">✅ Full Access for 3 Months</li>
                    <li style="margin-bottom: 15px;">✅ Direct WhatsApp & Email Unlocks</li>
                    <li style="margin-bottom: 15px;">✅ Daily RFQ Notifications</li>
                </ul>
                <button class="btn" style="margin-top: auto; background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: #fff; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('3 Months Access', 499, 49000)">Get 3 Months Access</button>
            </div>

            <!-- 6 MONTH PLAN -->
            <div class="plan highlight" style="display: flex; flex-direction: column; background: #111827; border: 1px solid var(--gold); padding: 40px; border-radius: 20px; text-align: left; position: relative; box-shadow: 0 0 20px rgba(212,175,55,0.1);">
                <div class="badge" style="background: #facc15; color: #000; font-weight: 800; font-size: 11px; margin-bottom: 20px; display: inline-block; padding: 4px 12px; border-radius: 50px; align-self: flex-start;">⭐ MOST POPULAR</div>
                <h3 style="font-size: 26px; margin-bottom: 5px; color: var(--gold);">6 Months Access</h3>
                <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">Ideal for serious exporters scaling operations.</p>
                <div class="price" style="font-size: 42px; color: #fff; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                    <span class="show-usd">$899</span>
                    <span class="show-inr">₹89,000</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 30px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">
                    <li style="margin-bottom: 15px; color: #4ade80; font-weight: 600;">✅ Full Access for 6 Months</li>
                    <li style="margin-bottom: 15px;">✅ Direct WhatsApp & Email Unlocks</li>
                    <li style="margin-bottom: 15px;">✅ Dedicated CRM Dashboard</li>
                    <li style="margin-bottom: 15px;">✨ Priority Support</li>
                </ul>
                <button class="btn" style="margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('6 Months Access', 899, 89000)">Get 6 Months Access</button>
            </div>

            <!-- 12 MONTH PLAN -->
            <div class="plan" style="display: flex; flex-direction: column; background: #111827; border: 1px solid rgba(255,255,255,0.05); padding: 40px; border-radius: 20px; text-align: left;">
                <div class="badge" style="background: #f59e0b; color: #000; font-weight: 800; font-size: 11px; margin-bottom: 20px; display: inline-block; padding: 4px 12px; border-radius: 50px;">BEST VALUE</div>
                <h3 style="font-size: 26px; margin-bottom: 10px; color: #fff;">12 Months Access</h3>
                <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">Maximum value for long-term export growth.</p>
                <div class="price" style="font-size: 42px; color: #fff; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                    <span class="show-usd">$1,499</span>
                    <span class="show-inr">₹149,000</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0; margin-bottom: 30px; flex-grow: 1; color: #cbd5e1; font-size: 14px; line-height: 1.8;">
                    <li style="margin-bottom: 15px; color: #facc15; font-weight: 600;">✅ Full Access for 12 Months</li>
                    <li style="margin-bottom: 15px;">✅ Unlimited Live Order Access</li>
                    <li style="margin-bottom: 15px;">✨ 1-on-1 Account Manager</li>
                    <li style="margin-bottom: 15px;">✨ Priority Deal Matching</li>
                </ul>
                <button class="btn" style="margin-top: auto; background: linear-gradient(135deg, #d97706, #f59e0b, #fbbf24); color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('12 Months Access', 1499, 149000)">Get 12 Months Access</button>
            </div>
        </div>
    </div>
    
    <div style="height: 80px;"></div>
    '''
    
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(text[:start_idx] + new_pricing + text[end_idx:])
    print('Updated membership.html successfully')
else:
    print('Could not find start/end indices', start_idx, end_idx)
