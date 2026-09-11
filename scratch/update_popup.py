import os

filepath = 'membership.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Using regex or exact split to find the modal block
start_str = '<!-- EXIT INTENT POPUP (WHATSAPP COUPON) -->'
end_str = '<!-- EXIT INTENT JS -->'

if start_str in content:
    parts1 = content.split(start_str)
    # the end string might not exist, let's look for `<style>` after the modal
    if '<style>' in parts1[1]:
        parts2 = parts1[1].split('<style>', 1)
        old_modal = parts2[0]
    else:
        print("Couldn't find the end of the modal.")
        exit(1)

new_modal = """
  <div id="exitIntentModal" style="
    display:none;
    position:fixed;
    inset:0;
    background:rgba(2, 6, 23, 0.95);
    backdrop-filter: blur(10px);
    align-items:center;
    justify-content:center;
    z-index:100000;
    padding: 20px;">
    
    <div style="background: linear-gradient(135deg, #111827, #0f172a); color:#fff; padding:40px; border-radius:24px; width:100%; max-width:450px; border: 2px solid var(--gold); position: relative; box-shadow: 0 30px 80px rgba(212, 175, 55, 0.3); text-align: center; animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
      
      <div onclick="document.getElementById('exitIntentModal').style.display='none'" style="position: absolute; top: 20px; right: 20px; cursor: pointer; color: #94a3b8; font-size: 24px; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border-radius: 50%;">✕</div>
      
      <div style="font-size: 40px; margin-bottom: 10px;">🛑</div>
      <h3 style="font-family: 'Playfair Display', serif; font-size: 26px; color: #fff; margin-bottom: 10px; font-weight: 800;">Wait! Don’t leave empty-handed.</h3>
      <p style="color: #cbd5e1; font-size: 15px; margin-bottom: 25px; line-height: 1.6;">
        If you aren't ready to scale with a full 6-Month Unlimited Membership yet, don't walk away without testing our data quality.
      </p>
      
      <div style="background: rgba(59, 130, 246, 0.1); border: 2px dashed #3b82f6; padding: 20px; border-radius: 12px; margin-bottom: 25px; text-align: center;">
          <div style="background: #facc15; color: #000; font-size: 10px; font-weight: 800; padding: 4px 10px; border-radius: 20px; display: inline-block; margin-bottom: 10px; letter-spacing: 1px;">MOST POPULAR</div>
          <div style="font-size: 22px; font-weight: 800; color: white; margin-bottom: 10px;">Get 5 Verified Buyers</div>
          <div class="show-inr" style="font-size: 24px; font-weight: 800; color: #22c55e; margin-bottom: 15px;">₹14,900 INR</div>
          <div class="show-usd" style="font-size: 24px; font-weight: 800; color: #22c55e; margin-bottom: 15px;">$199 USD</div>
          
          <ul style="list-style: none; padding: 0; margin: 0; color: #cbd5e1; font-size: 13.5px; line-height: 1.6; text-align: left;">
              <li style="margin-bottom: 8px;">✅ Direct phone number & email address unlocked.</li>
              <li style="margin-bottom: 8px;">✅ Zero long-term commitments or automatic recurring charges.</li>
              <li>✅ Full access to buyer requirements (Port, Volume, Payment terms).</li>
          </ul>
      </div>
      
      <button class="btn show-inr-block" style="margin-top: auto; background: #3b82f6; color: white; display: block; align-items: center; justify-content: center; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%205%20Buyer%20Trial%20for%20%E2%82%B914,900.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
          Try 5 Verified Buyer Leads (₹14,900)
      </button>

      <button class="btn show-usd-block" style="margin-top: auto; background: #3b82f6; color: white; display: none; align-items: center; justify-content: center; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%205%20Buyer%20Trial%20for%20$199.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
          Try 5 Verified Buyer Leads ($199)
      </button>

      <div style="margin-top: 15px; font-size: 13px; color: #64748b; cursor: pointer; text-decoration: underline;" onclick="document.getElementById('exitIntentModal').style.display='none'">
          No thanks, I'll close my session
      </div>
    </div>
  </div>

  """

content = parts1[0] + start_str + '\n' + new_modal + '<style>' + parts2[1]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated exit intent popup!')
