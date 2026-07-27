import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
mem_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"

# --- UPDATE INDEX.HTML ---
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Add Micro-Proof near the CTA button
micro_proof = """
        <div style="margin-top: 15px; display: flex; align-items: center; justify-content: center; gap: 10px; opacity: 0.8;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            <span style="font-size: 12px; color: #fff; letter-spacing: 1px;">256-Bit SSL Encrypted & Verified by APD Legal</span>
        </div>
"""
if "Browse Live Market</a>" in index_html and "256-Bit SSL" not in index_html:
    index_html = index_html.replace('Browse Live Market</a>\n        </div>', 'Browse Live Market</a>\n        </div>\n' + micro_proof)

# 2. Update Headline to be perfectly outcome-focused
index_html = index_html.replace(
    '<h1 style="margin-bottom: 20px; text-shadow: 0 0 30px rgba(255,255,255,0.2); font-size: clamp(2rem, 5vw, 4rem);">Direct Access to Institutional Global Trade</h1>',
    '<h1 style="margin-bottom: 20px; text-shadow: 0 0 30px rgba(255,255,255,0.2); font-size: clamp(2rem, 5vw, 4rem);">Eliminate Export Risk. Secure Institutional Buyers.</h1>'
)

# 3. Add Floating WhatsApp Button
wa_button = """
  <!-- FLOATING WHATSAPP BUTTON -->
  <a href="https://wa.me/919898470743?text=Hi%20APD%20Global%20Trade,%20I%20am%20interested%20in%20connecting%20with%20Verified%20Buyers." target="_blank" style="position: fixed; bottom: 30px; right: 30px; background: #25D366; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(37, 211, 102, 0.4); z-index: 10000; transition: 0.3s transform;">
      <svg width="35" height="35" viewBox="0 0 24 24" fill="white"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-3.825 3.113-6.937 6.937-6.937 3.825 0 6.938 3.112 6.938 6.938 0 3.825-3.113 6.938-6.938 6.938z"/></svg>
  </a>
"""
if "<!-- FLOATING WHATSAPP BUTTON -->" not in index_html:
    index_html = index_html.replace('</body>', wa_button + '\n</body>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# --- UPDATE MEMBERSHIP.HTML ---
with open(mem_path, "r", encoding="utf-8") as f:
    mem_html = f.read()

# Add Secure Payment Logos below the checkout area
payment_logos = """
    <!-- SECURE PAYMENT LOGOS -->
    <div style="text-align: center; margin-top: 40px; padding: 20px; background: rgba(255,255,255,0.02); border-radius: 15px; border: 1px solid rgba(255,255,255,0.05);">
        <p style="font-size: 14px; color: #9ca3af; margin-bottom: 15px;">Transactions secured by International Escrow & Payment Partners</p>
        <div style="display: flex; justify-content: center; gap: 30px; align-items: center; opacity: 0.7;">
            <span style="font-family: sans-serif; font-size: 24px; font-weight: 800; color: #003087;"><i>PayPal</i></span>
            <span style="font-family: sans-serif; font-size: 24px; font-weight: 800; color: #6366f1;">stripe</span>
            <span style="font-family: sans-serif; font-size: 20px; font-weight: 700; color: #0f172a;">Razorpay</span>
            <div style="display: flex; align-items: center; gap: 5px; color: #22c55e;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                <span style="font-size: 14px; font-weight: 600;">Trade Assurance Active</span>
            </div>
        </div>
    </div>
"""
if "<!-- SECURE PAYMENT LOGOS -->" not in mem_html:
    mem_html = mem_html.replace('id="paypal-button-container"></div>', 'id="paypal-button-container"></div>\n' + payment_logos)

if "<!-- FLOATING WHATSAPP BUTTON -->" not in mem_html:
    mem_html = mem_html.replace('</body>', wa_button + '\n</body>')

with open(mem_path, "w", encoding="utf-8") as f:
    f.write(mem_html)

