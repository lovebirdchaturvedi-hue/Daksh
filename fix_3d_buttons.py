import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the first redundant action bar
redundant_bar_pattern = r'<!-- ELITE MOBILE ACTION BAR -->\s*<div class="mobile-action-bar">\s*<a href="/buyer-rfqs\.html" class="mobile-action-btn btn-outline">View RFQs</a>\s*<a href="/membership\.html" class="mobile-action-btn btn-gold">Elite Access</a>\s*</div>'
content = re.sub(redundant_bar_pattern, '', content)

# 2. Replace the second action bar with 3D styles
# Using regex to find the second action bar since emojis might have encoding differences
old_bottom_bar_pattern = r'<!-- MOBILE STICKY BOTTOM CTA BAR -->\s*<!-- ============================================================ -->\s*<div class="mobile-action-bar" id="mobileActionBar">.*?</div>'

new_3d_bar_html = '''<!-- MOBILE STICKY BOTTOM CTA BAR (3D WOW VERSION) -->
  <!-- ============================================================ -->
  <style>
    /* WOW 3D PREMIUM MOBILE BAR */
    .mobile-action-bar.premium-3d-bar {
        background: rgba(15, 23, 42, 0.85) !important;
        backdrop-filter: blur(20px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 -10px 40px rgba(0,0,0,0.6) !important;
        padding: 15px 5% 25px 5% !important; /* iPhone bottom safe area */
        gap: 12px !important;
    }

    .btn-3d-gold {
        flex: 1;
        padding: 16px 10px;
        text-align: center;
        font-weight: 900;
        border-radius: 14px;
        font-size: 13px;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        letter-spacing: 1px;
        background: linear-gradient(180deg, #facc15 0%, #c9a44a 100%);
        box-shadow: 0 6px 0 #9c7b16, 0 15px 25px rgba(201,164,74,0.4), inset 0 2px 0 rgba(255,255,255,0.5);
        color: #000 !important;
        text-shadow: 0 1px 0 rgba(255,255,255,0.4);
        border: none;
        transition: all 0.15s ease;
        transform: translateY(0);
        text-transform: uppercase;
    }
    .btn-3d-gold:active {
        box-shadow: 0 2px 0 #9c7b16, 0 5px 10px rgba(201,164,74,0.4), inset 0 2px 0 rgba(255,255,255,0.5);
        transform: translateY(4px);
    }

    .btn-3d-green {
        flex: 1;
        padding: 16px 10px;
        text-align: center;
        font-weight: 900;
        border-radius: 14px;
        font-size: 13px;
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        letter-spacing: 1px;
        background: linear-gradient(180deg, #4ade80 0%, #16a34a 100%);
        box-shadow: 0 6px 0 #15803d, 0 15px 25px rgba(37,211,102,0.4), inset 0 2px 0 rgba(255,255,255,0.4);
        color: #fff !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        border: none;
        transition: all 0.15s ease;
        transform: translateY(0);
        text-transform: uppercase;
    }
    .btn-3d-green:active {
        box-shadow: 0 2px 0 #15803d, 0 5px 10px rgba(37,211,102,0.4), inset 0 2px 0 rgba(255,255,255,0.4);
        transform: translateY(4px);
    }
  </style>

  <div class="mobile-action-bar premium-3d-bar" id="mobileActionBar">
    <a href="/membership.html" class="mobile-action-btn btn-3d-gold">
      ✨ ELITE ACCESS
    </a>
    <a href="https://wa.me/919718173015?text=I%20want%20to%20know%20more%20about%20APD%20Global%20Trade%20Membership" target="_blank" class="mobile-action-btn btn-3d-green">
      💬 WHATSAPP
    </a>
  </div>'''

content = re.sub(old_bottom_bar_pattern, new_3d_bar_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html to have WOW 3D buttons.")
