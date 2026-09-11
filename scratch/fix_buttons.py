import os

filepath = 'membership.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the button wrapping for CSS compatibility
old_buttons = """      <button class="btn show-inr-block" style="margin-top: auto; background: #3b82f6; color: white; display: block; align-items: center; justify-content: center; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%205%20Buyer%20Trial%20for%20%E2%82%B914,900.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
          Try 5 Verified Buyer Leads (₹14,900)
      </button>

      <button class="btn show-usd-block" style="margin-top: auto; background: #3b82f6; color: white; display: none; align-items: center; justify-content: center; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%205%20Buyer%20Trial%20for%20$199.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
          Try 5 Verified Buyer Leads ($199)
      </button>"""

new_buttons = """      <div class="show-inr-block">
          <button class="btn" style="background: #3b82f6; color: white; display: block; align-items: center; justify-content: center; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%205%20Buyer%20Trial%20for%20%E2%82%B914,900.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
              Try 5 Verified Buyer Leads (₹14,900)
          </button>
      </div>

      <div class="show-usd-block">
          <button class="btn" style="background: #3b82f6; color: white; display: block; align-items: center; justify-content: center; font-size: 15px; width: 100%; border: none; padding: 15px; border-radius: 50px; font-weight: 700; cursor: pointer;" onclick="window.open('https://wa.me/919266418868?text=Hi%20APD%20Team,%20I%20want%20to%20claim%20the%20Exit%20Intent%205%20Buyer%20Trial%20for%20$199.', '_blank'); document.getElementById('exitIntentModal').style.display='none';">
              Try 5 Verified Buyer Leads ($199)
          </button>
      </div>"""

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed CSS button wrapper')
else:
    print('Could not find old buttons to replace')
