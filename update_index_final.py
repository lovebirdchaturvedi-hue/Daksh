import re

def run_fixes():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update image URLs for product grid
    html = re.sub(
        r'<img\s+src="https://images\.unsplash\.com/photo-1586201375761.*?"',
        '<img src="/assets/img/basmati_rice.png"',
        html
    )
    html = re.sub(
        r'<img\s+src="https://images\.unsplash\.com/photo-1596647413665.*?"',
        '<img src="/assets/img/refined_sugar.png"',
        html
    )
    html = re.sub(
        r'<img\s+src="https://images\.unsplash\.com/photo-1621213076722.*?"',
        '<img src="/assets/img/cumin_seeds.png"',
        html
    )
    html = re.sub(
        r'<img\s+src="https://images\.unsplash\.com/photo-1595187127453.*?"',
        '<img src="/assets/img/husk_powder.png"',
        html
    )

    # 2. Inject Chatbot
    if '/assets/js/ai-chatbot.js' not in html:
        html = html.replace('</body>', '  <script src="/assets/js/ai-chatbot.js"></script>\n</body>')

    # 3. Make Search Buttons Redirect
    # Hero Search Button
    html = html.replace(
        '<button style="border-bottom: none !important; padding: 15px !important; background: linear-gradient(90deg, var(--gold), #8B6508); border: none; color: #000; font-weight: 900; padding: 0 30px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s;">Search</button>',
        '<button onclick="window.location.href=\'/buyer-rfqs.html\'" style="border-bottom: none !important; padding: 15px !important; background: linear-gradient(90deg, var(--gold), #8B6508); border: none; color: #000; font-weight: 900; padding: 0 30px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s;">Search</button>'
    )
    # Wait, the inline style might have changed. Let's just use regex for the button tag in hero-search-inner.
    pattern_hero_btn = r'<button([^>]*)>Search</button>'
    html = re.sub(pattern_hero_btn, r'<button\1 onclick="window.location.href=\'/buyer-rfqs.html\'">Search</button>', html)

    # Mini Search Button
    pattern_mini_btn = r'<button([^>]*)>🔎</button>'
    html = re.sub(pattern_mini_btn, r'<button\1 onclick="window.location.href=\'/buyer-rfqs.html\'">🔎</button>', html)

    # 4. Add "Premium 3 Days Trial" banner
    if 'Premium 3-Day Institutional Trial' not in html:
        trial_banner = """
  <!-- PREMIUM TRIAL BANNER -->
  <section style="padding: 60px 20px; background: linear-gradient(90deg, #0f172a, #020617); border-top: 1px solid rgba(212,175,55,0.2); border-bottom: 1px solid rgba(212,175,55,0.2); text-align: center;">
      <h2 style="font-family: 'Playfair Display', serif; font-size: 36px; color: #fff; margin-bottom: 15px;">Activate Your <span style="color: var(--gold);">Premium 3-Day Institutional Trial</span></h2>
      <p style="color: #94a3b8; font-size: 18px; max-width: 800px; margin: 0 auto 30px auto; line-height: 1.6;">
          Experience top-tier global B2B trade. Get exactly 3 free unlocks to view verified buyer details, shipping destinations, and direct contact numbers—absolutely free for 3 days.
      </p>
      <a href="/membership.html" style="display: inline-block; background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; font-size: 18px; padding: 15px 40px; border-radius: 50px; text-decoration: none; box-shadow: 0 10px 30px rgba(212,175,55,0.3); transition: transform 0.3s;">
          Start Your Free Trial Now
      </a>
  </section>
  """
        # Insert before footer
        html = html.replace('<!-- FOOTER START -->', trial_banner + '\n  <!-- FOOTER START -->')
        # If footer comment not found, insert before <footer> tag
        if '<!-- FOOTER START -->' not in html:
            html = html.replace('<footer>', trial_banner + '\n  <footer>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixes applied to index.html")

run_fixes()
