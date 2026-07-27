import re

def fix_hero_and_banner():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. First, let's remove the banner from wherever it currently is (footer)
    banner_pattern = r'<!-- PREMIUM 3D TRIAL BANNER -->.*?</section>'
    html = re.sub(banner_pattern, '', html, flags=re.DOTALL)
    
    # Let's recreate the banner snippet but slightly scaled down for hero integration
    new_banner = """
  <!-- PREMIUM 3D TRIAL BANNER -->
  <section style="padding: 20px; position: relative; max-width: 900px; margin: 40px auto 20px auto; z-index: 20;">
      <div style="position: relative; background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01)); border: 1px solid rgba(212,175,55,0.6); border-radius: 24px; padding: 40px 30px; text-align: center; box-shadow: 0 30px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1); transform-style: preserve-3d; transform: perspective(1000px) rotateX(2deg); backdrop-filter: blur(15px);">
          <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; font-size: 11px; letter-spacing: 2px; text-transform: uppercase; padding: 6px 20px; border-radius: 20px; box-shadow: 0 10px 20px rgba(212,175,55,0.4);">Limited Time</div>
          <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: #fff; margin-bottom: 15px; text-shadow: 0 10px 20px rgba(0,0,0,0.5); line-height:1.2;">Unlock Your <span style="background: linear-gradient(90deg, #d4af37, #facc15); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Premium 3-Day Trial</span></h2>
          <p style="color: #cbd5e1; font-size: 15px; max-width: 600px; margin: 0 auto 25px auto; line-height: 1.5;">
              Experience the pinnacle of global B2B trade. Get exactly 3 free unlocks to view verified institutional buyer details, shipping destinations, and direct executive contact numbers—completely risk-free.
          </p>
          <a href="/membership.html" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; font-size: 16px; padding: 15px 40px; border-radius: 50px; text-decoration: none; box-shadow: 0 15px 35px rgba(212,175,55,0.4), inset 0 2px 0 rgba(255,255,255,0.5); transition: all 0.3s; transform: translateZ(20px);">
              START YOUR FREE TRIAL
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>
      </div>
  </section>
  """
    
    # Place it right before the hero-buttons
    html = html.replace('<div class="hero-buttons', new_banner + '\n          <div class="hero-buttons')

    # 2. Fix the search bar visibility and placement
    # First, make the search input text and placeholder Gold, and move it lower (margin-top)
    html = re.sub(
        r'<input type="text" name="q" placeholder="Search bulk commodities, verified exporters, or global destination ports..." style="(.*?)">',
        r'<input type="text" name="q" placeholder="Search bulk commodities, verified exporters, or global destination ports..." style="\1 color: #facc15 !important;">',
        html
    )
    
    # Make sure we add a specific CSS style for the placeholder to be gold
    if '::placeholder { color: #facc15 !important;' not in html:
        css_addition = """
        <style>
            #heroSearchForm input::placeholder {
                color: #facc15 !important;
                opacity: 0.8;
                font-weight: 600;
            }
            #heroSearchForm input {
                color: #facc15 !important;
                font-weight: 700;
            }
        </style>
        """
        html = html.replace('<!-- MARKETPLACE SEARCH BAR -->', css_addition + '\n          <!-- MARKETPLACE SEARCH BAR -->')

    # Increase the top margin of the marketplace search bar wrapper to move it lower
    html = html.replace(
        '<div class="fade-in" style="width: 100%; max-width: 800px; margin: 0 auto 15px auto; position: relative;">',
        '<div class="fade-in" style="width: 100%; max-width: 800px; margin: 60px auto 15px auto; position: relative; z-index: 20;">'
    )
    
    # If the above replacement didn't work because it had different spacing, try regex:
    html = re.sub(
        r'<div class="fade-in" style="width: 100%; max-width: 800px; margin: 0 auto 15px auto; position: relative;">',
        '<div class="fade-in" style="width: 100%; max-width: 800px; margin: 60px auto 15px auto; position: relative; z-index: 20;">',
        html
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed hero styling and banner")

fix_hero_and_banner()
