import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

footer_idx = text.find('<!-- FOOTER -->')
if footer_idx == -1:
    footer_idx = text.find('<footer')

newsletter_html = """
    <!-- ========================================== -->
    <!-- TRUST BADGES & NEWSLETTER SECTION -->
    <!-- ========================================== -->
    <section style="background: #020617; padding: 60px 20px; border-top: 1px solid rgba(255,255,255,0.05);">
        <div style="max-width: 1200px; margin: 0 auto; text-align: center;">
            
            <!-- Trust Badges -->
            <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 30px; margin-bottom: 50px; filter: grayscale(100%) opacity(0.7);">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">🛡️</span>
                    <span style="color: #fff; font-weight: 700; font-size: 14px; letter-spacing: 1px;">AES-256 SECURE</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">🤝</span>
                    <span style="color: #fff; font-weight: 700; font-size: 14px; letter-spacing: 1px;">ESCROW PROTECTION</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">🌐</span>
                    <span style="color: #fff; font-weight: 700; font-size: 14px; letter-spacing: 1px;">TRADOLOGIE VERIFIED PARTNER</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">🏦</span>
                    <span style="color: #fff; font-weight: 700; font-size: 14px; letter-spacing: 1px;">RAZORPAY TRUSTED</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 24px;">📜</span>
                    <span style="color: #fff; font-weight: 700; font-size: 14px; letter-spacing: 1px;">FIEO MEMBER ALIGNED</span>
                </div>
            </div>

            <!-- Newsletter Box -->
            <div style="background: linear-gradient(135deg, #0f172a, #1e293b); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; padding: 50px 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); max-width: 800px; margin: 0 auto; position: relative; overflow: hidden;">
                <div style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(212,175,55,0.1) 0%, transparent 70%); border-radius: 50%;"></div>
                
                <h3 style="font-family: 'Playfair Display', serif; font-size: 32px; color: var(--gold); margin: 0 0 15px 0;">Global Trade Market Intelligence</h3>
                <p style="color: #94a3b8; font-size: 15px; margin: 0 0 30px 0; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.6;">
                    Join 14,000+ top-tier exporters and institutional buyers. Get weekly commodity price trends, international tender alerts, and geopolitical trade shifts delivered straight to your inbox.
                </p>
                
                <form action="https://formspree.io/f/xgogjdll" method="POST" style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: center;">
                    <input type="hidden" name="_subject" value="New Newsletter Subscriber - APD Global Trade">
                    <input type="email" name="email" required placeholder="Enter your corporate email address" style="flex: 1; min-width: 250px; max-width: 400px; padding: 16px 20px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: #fff; font-size: 15px; outline: none; transition: 0.3s;" onfocus="this.style.borderColor='var(--gold)'" onblur="this.style.borderColor='rgba(255,255,255,0.1)'">
                    <button type="submit" style="padding: 16px 35px; border-radius: 50px; border: none; background: linear-gradient(90deg, #d4af37, #facc15); color: #000; font-weight: 800; font-size: 15px; cursor: pointer; transition: 0.3s; box-shadow: 0 4px 15px rgba(212,175,55,0.3);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Subscribe Now</button>
                </form>
                
                <div style="color: #64748b; font-size: 11px; margin-top: 20px; text-transform: uppercase; letter-spacing: 1px;">
                    No spam. Unsubscribe anytime. 100% Data Privacy Guaranteed.
                </div>
            </div>
            
        </div>
    </section>
"""

if footer_idx != -1:
    new_text = text[:footer_idx] + newsletter_html + text[footer_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Newsletter and trust badges added to index.html successfully.')
else:
    print('Failed to find footer.')
