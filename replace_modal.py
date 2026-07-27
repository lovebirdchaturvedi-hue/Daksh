import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_modal_content_pattern = re.compile(r'<div onclick="document\.getElementById\(\'exitIntentModal\'\)\.style\.display=\'none\'".*?Claim My ₹5,000 Coupon\n      </button>', re.DOTALL)

new_modal_content = """<div onclick="document.getElementById('exitIntentModal').style.display='none'" style="position: absolute; top: 20px; right: 20px; cursor: pointer; color: #94a3b8; font-size: 24px; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%;">✕</div>
      
      <div style="font-size: 40px; margin-bottom: 10px;">🛑</div>
      <h3 style="font-family: 'Playfair Display', serif; font-size: 26px; color: #fff; margin-bottom: 10px; font-weight: 800;">Wait! Don’t leave empty-handed.</h3>
      <p style="color: #cbd5e1; font-size: 15px; margin-bottom: 25px; line-height: 1.6;">
        If you aren't ready to scale with a full 6-Month Unlimited Membership yet, don't walk away without testing our data quality.
      </p>
      
      <div style="background: rgba(37, 211, 102, 0.1); border: 2px dashed #25D366; padding: 20px; border-radius: 12px; margin-bottom: 25px; text-align: left;">
          <div style="font-size: 16px; font-weight: 700; color: white; margin-bottom: 15px; text-align: center;">Unlock just 1 active, 100% verified premium buyer contact right now for a one-time trial fee. See the data quality for yourself before making a bigger commitment.</div>
          <ul style="list-style: none; padding: 0; margin: 0; color: #cbd5e1; font-size: 14px; line-height: 1.8;">
              <li style="margin-bottom: 10px;">✅ Direct phone number & email address unlocked instantly.</li>
              <li style="margin-bottom: 10px;">✅ Zero long-term commitments or automatic recurring charges.</li>
              <li>✅ Full access to buyer requirements (Port, Volume, Payment terms).</li>
          </ul>
      </div>
      
      <button class="btn" style="margin-top: auto; background: #25D366; color: white; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%201%20Buyer%20Trial%20for%20%E2%82%B91,499.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
          Try 1 Verified Buyer Lead for ₹1,499
      </button>
      <div style="margin-top: 15px; font-size: 13px; color: #64748b; cursor: pointer; text-decoration: underline;" onclick="document.getElementById('exitIntentModal').style.display='none'">
          No thanks, I'll close my session
      </div>"""

if old_modal_content_pattern.search(html):
    html = old_modal_content_pattern.sub(new_modal_content, html)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Modal replaced")
else:
    print("Could not find old modal")
