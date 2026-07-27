import os

html_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD SUCCESS STORIES (Problem -> Solution -> Result)
success_stories = """
  <!-- VERIFIED SUCCESS STORIES -->
  <section style="padding: 80px 5%; background: #071427; border-top: 1px solid rgba(212, 175, 55, 0.1);">
      <div class="container">
          <h2 style="text-align: center; font-family: 'Playfair Display', serif; font-size: 36px; color: var(--gold); margin-bottom: 50px;">Verified Trade Outcomes</h2>
          
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
              
              <!-- Case Study 1 -->
              <div style="background: rgba(2, 6, 23, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 30px;">
                  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
                      <div style="width: 40px; height: 40px; background: #1e293b; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--gold);">TN</div>
                      <div>
                          <div style="font-weight: 700; font-size: 16px;">Textile Exporter, Tirupur</div>
                          <div style="font-size: 12px; color: #9ca3af;">Exported to Europe</div>
                      </div>
                  </div>
                  <div style="margin-bottom: 15px;">
                      <strong style="color: #ef4444;">Problem:</strong> Spent ₹2 Lakhs on generic B2B portals with zero verified buyers.
                  </div>
                  <div style="margin-bottom: 15px;">
                      <strong style="color: #eab308;">Solution:</strong> Joined APD Elite Plan, accessed 15 verified institutional EU buyers.
                  </div>
                  <div>
                      <strong style="color: #22c55e;">Result:</strong> Closed a $45,000 apparel contract in 14 days.
                  </div>
              </div>

              <!-- Case Study 2 -->
              <div style="background: rgba(2, 6, 23, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 30px;">
                  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
                      <div style="width: 40px; height: 40px; background: #1e293b; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--gold);">GJ</div>
                      <div>
                          <div style="font-weight: 700; font-size: 16px;">Agro-Processor, Rajkot</div>
                          <div style="font-size: 12px; color: #9ca3af;">Exported to Middle East</div>
                      </div>
                  </div>
                  <div style="margin-bottom: 15px;">
                      <strong style="color: #ef4444;">Problem:</strong> Buyers were rejecting shipments due to non-standardized pricing and trust issues.
                  </div>
                  <div style="margin-bottom: 15px;">
                      <strong style="color: #eab308;">Solution:</strong> Verified through APD, used APD's escrow-backed RFQ matching.
                  </div>
                  <div>
                      <strong style="color: #22c55e;">Result:</strong> Increased monthly export volume by 20% in 6 months.
                  </div>
              </div>

              <!-- Case Study 3 -->
              <div style="background: rgba(2, 6, 23, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 30px;">
                  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
                      <div style="width: 40px; height: 40px; background: #1e293b; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--gold);">MH</div>
                      <div>
                          <div style="font-weight: 700; font-size: 16px;">Spices Trader, Nashik</div>
                          <div style="font-size: 12px; color: #9ca3af;">Exported to Vietnam</div>
                      </div>
                  </div>
                  <div style="margin-bottom: 15px;">
                      <strong style="color: #ef4444;">Problem:</strong> Fear of non-payment from new international clients.
                  </div>
                  <div style="margin-bottom: 15px;">
                      <strong style="color: #eab308;">Solution:</strong> Leveraged APD's secure payment ecosystem & verified Letter of Credit buyers.
                  </div>
                  <div>
                      <strong style="color: #22c55e;">Result:</strong> Secured 3 new permanent international distributors.
                  </div>
              </div>

          </div>
      </div>
  </section>
"""

# 2. ADD PRODUCT TOUR PREVIEW
product_tour = """
  <!-- PRODUCT DASHBOARD PREVIEW -->
  <section style="padding: 100px 5%; background: #020617; text-align: center;">
      <div class="container">
          <h2 style="font-family: 'Playfair Display', serif; font-size: 36px; color: #fff; margin-bottom: 20px;">See The Platform In Action</h2>
          <p style="font-size: 18px; color: #9ca3af; max-width: 700px; margin: 0 auto 50px;">Don't guess what you're paying for. Here is exactly what our Verified Suppliers see when they unlock the Institutional Dashboard.</p>
          
          <div style="position: relative; max-width: 1000px; margin: 0 auto; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 60px rgba(212, 175, 55, 0.15); border: 1px solid rgba(212, 175, 55, 0.3);">
              <!-- Placeholder for actual dashboard screenshot -->
              <div style="width: 100%; height: 500px; background: linear-gradient(135deg, #0f172a, #1e293b); display: flex; align-items: center; justify-content: center; flex-direction: column;">
                  <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 20px;"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                  <h3 style="color: var(--gold); font-family: 'Playfair Display', serif; font-size: 24px;">[ High-Quality Dashboard Screenshot Goes Here ]</h3>
                  <p style="color: #94a3b8; margin-top: 10px;">Showing Live RFQ Feed, Buyer Verification Tags, and Secure Chat Interface</p>
              </div>
          </div>
      </div>
  </section>
"""

# 3. ADD FAQ SECTION
faq_section = """
  <!-- RADICAL TRANSPARENCY FAQ -->
  <section style="padding: 80px 5%; background: #071427;">
      <div class="container" style="max-width: 800px;">
          <h2 style="text-align: center; font-family: 'Playfair Display', serif; font-size: 32px; color: var(--gold); margin-bottom: 50px;">Frequently Asked Questions</h2>
          
          <div style="margin-bottom: 30px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px;">
              <h3 style="font-size: 20px; color: #fff; margin-bottom: 10px;">Are the buyers actually verified?</h3>
              <p style="color: #9ca3af; line-height: 1.6;">Yes. Unlike free directories, we employ a strict Buyer Verification protocol. We audit their corporate registration, past import history, and financial standing before allowing their RFQs onto our platform.</p>
          </div>
          
          <div style="margin-bottom: 30px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px;">
              <h3 style="font-size: 20px; color: #fff; margin-bottom: 10px;">Is my payment and data secure?</h3>
              <p style="color: #9ca3af; line-height: 1.6;">Absolutely. APD Global Trade uses 256-bit SSL encryption. All subscription payments are processed securely through globally compliant gateways (Stripe/PayPal), and we adhere strictly to GDPR data privacy regulations.</p>
          </div>
          
          <div style="margin-bottom: 30px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px;">
              <h3 style="font-size: 20px; color: #fff; margin-bottom: 10px;">What happens after I subscribe?</h3>
              <p style="color: #9ca3af; line-height: 1.6;">Upon subscribing, you undergo our Supplier KYC check. Once cleared, you gain instant access to the Live Buyer Feed, allowing you to directly contact international purchase managers without any middlemen.</p>
          </div>
      </div>
  </section>
"""

# 4. UPDATE FOOTER WITH COMPREHENSIVE CONTACT INFO
footer_comprehensive = """
  <!-- COMPREHENSIVE FOOTER -->
  <footer style="background: #020617; border-top: 1px solid rgba(212, 175, 55, 0.2); padding: 80px 5% 40px;">
      <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 50px;">
          
          <div>
              <div style="font-family: 'Playfair Display', serif; font-size: 24px; color: var(--gold); margin-bottom: 20px;">APD Global Trade</div>
              <p style="color: #9ca3af; line-height: 1.6; font-size: 14px;">The world's premier verification authority for institutional global trade. Eliminating middlemen and securing cross-border transactions.</p>
          </div>

          <div>
              <h4 style="color: #fff; margin-bottom: 20px; font-size: 16px;">Contact Headquarters</h4>
              <p style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">📧 ceo@apdglobaltrade.com</p>
              <p style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">📞 +91 98984 70743</p>
              <p style="color: #9ca3af; font-size: 14px; line-height: 1.6;">📍 APD Global Trade Headquarters<br>India</p>
          </div>

          <div>
              <h4 style="color: #fff; margin-bottom: 20px; font-size: 16px;">Legal & Security</h4>
              <p style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">🔒 256-Bit SSL Secured</p>
              <p style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;"><a href="#" style="color: #9ca3af; text-decoration: none;">Privacy Policy & GDPR</a></p>
              <p style="color: #9ca3af; font-size: 14px;"><a href="#" style="color: #9ca3af; text-decoration: none;">Terms of Institutional Trade</a></p>
          </div>

      </div>
      <div style="text-align: center; color: #6b7280; font-size: 12px; margin-top: 60px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.05);">
          © 2026 APD Global Trade. All rights reserved.
      </div>
  </footer>
"""

# Apply injections to index.html
if "VERIFIED SUCCESS STORIES" not in html:
    html = html.replace('<!-- HOW IT WORKS SECTION -->', success_stories + '\n' + product_tour + '\n' + faq_section + '\n<!-- HOW IT WORKS SECTION -->')

# Replace the old footer
import re
html = re.sub(r'<footer>.*?</footer>', footer_comprehensive, html, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

