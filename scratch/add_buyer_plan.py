with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = """    <!-- ============================================================ -->
    <!-- APD GLOBAL TRADE NEXUS™ — ULTRA-PREMIUM SOVEREIGN PASS -->"""

buyer_section = """
    <!-- ============================================================ -->
    <!-- VERIFIED BUYER MEMBERSHIP -->
    <!-- ============================================================ -->
    <section id="buyer-plan" style="padding: 60px 20px; max-width: 1200px; margin: 0 auto;">
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 2px solid #ef4444; border-radius: 24px; padding: 40px; position: relative; overflow: hidden; margin-bottom: 50px;">
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start; gap: 25px; margin-bottom: 35px;">
                <div>
                    <div style="display: inline-block; background: linear-gradient(90deg, #ef4444, #b91c1c); color: #fff; font-size: 11px; font-weight: 800; padding: 6px 18px; border-radius: 30px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">Dedicated Buyer Tier</div>
                    <h3 style="font-size: 30px; color: #fff; margin: 0 0 8px 0; font-weight: 800; letter-spacing: -0.5px;">Verified Buyer Membership</h3>
                    <p style="color: #94a3b8; font-size: 15px; margin: 0; max-width: 600px;">Want to become our verified Buyer and Contact Exporters Directly? 1 Year Validity.</p>
                </div>
                <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); padding: 20px 28px; border-radius: 16px; text-align: right; min-width: 210px; flex-shrink: 0;">
                    <div style="font-size: 38px; font-weight: 900; color: #f87171; line-height: 1;">$2,500 <span style="font-size: 16px; color: #94a3b8; font-weight: 400;">/ Year</span></div>
                    <div style="font-size: 22px; font-weight: 700; color: #e2e8f0; margin-top: 6px;">₹2,10,000 <span style="font-size: 12px; color: #94a3b8; font-weight: 400;">INR</span></div>
                </div>
            </div>

            <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.08); margin-bottom: 35px;">

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 30px; margin-bottom: 40px;">
                <div>
                    <h4 style="color: #f87171; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 15px 0;">Buyer Privileges</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; font-size: 14px; color: #cbd5e1; line-height: 2.2;">
                        <li>✅ Direct Access to Exporters</li>
                        <li>✅ Dedicated Procurement Support</li>
                        <li>✅ Trade Specialist Assigned</li>
                        <li>✅ Global Market Intel</li>
                    </ul>
                </div>
                <div style="background: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; padding: 20px; border-radius: 8px;">
                    <h4 style="color: #ef4444; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 15px 0;">Important Disclaimer</h4>
                    <p style="font-size: 13px; color: #e2e8f0; line-height: 1.6; margin: 0;">
                        We do not guarantee that you will get the exact product or close a trade. Our task is strictly to provide verified supplier contacts. 
                        <strong>Amount is strictly non-refundable.</strong> By proceeding, you agree to our buyer terms.
                    </p>
                    <div style="margin-top: 15px; display: flex; gap: 15px;">
                        <a href="buyer-agreement.html" target="_blank" style="color: #60a5fa; font-size: 12px; text-decoration: underline;">Read Buyer Agreement</a>
                        <a href="buyer-consent.html" target="_blank" style="color: #60a5fa; font-size: 12px; text-decoration: underline;">Read Buyer Consent</a>
                    </div>
                </div>
            </div>

            <div style="text-align: center;">
                <a href="#" onclick="initiatePayment('Verified Buyer Membership (1 Year)', 2500, 210000); return false;" style="display: inline-block; background: #ef4444; color: #fff; padding: 16px 40px; border-radius: 50px; font-weight: 800; font-size: 16px; text-decoration: none; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; box-shadow: 0 10px 25px rgba(239, 68, 68, 0.4);">Pay Now to Become a Verified Buyer</a>
            </div>
        </div>
    </section>

    <!-- ============================================================ -->
    <!-- APD GLOBAL TRADE NEXUS™ — ULTRA-PREMIUM SOVEREIGN PASS -->"""

html = html.replace(target, buyer_section)

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added Verified Buyer section to membership.html")
