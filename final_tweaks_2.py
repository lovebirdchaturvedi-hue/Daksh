import re

def tweaks():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update logo tagline
    html = re.sub(
        r'<span style="font-size: 10px; font-weight: 800; letter-spacing: 2px; color: #94a3b8; text-transform:\s*uppercase;">Connecting India To Global Markets</span>',
        '<span style="font-size: 10px; font-weight: 800; letter-spacing: 2px; color: var(--gold); text-transform: uppercase;">YOUR ONE-STOP GLOBAL TRADE SOLUTION</span>',
        html,
        flags=re.IGNORECASE
    )
    # Also in case it's one line
    html = re.sub(
        r'Connecting India To Global Markets',
        'YOUR ONE-STOP GLOBAL TRADE SOLUTION',
        html,
        flags=re.IGNORECASE
    )

    # 2. Fix the search functionality by wrapping them in <form>
    # Hero Search
    if 'id="heroSearchForm"' not in html:
        html = html.replace(
            '<div class="hero-search-inner"',
            '<form id="heroSearchForm" action="/buyer-rfqs.html" method="GET" class="hero-search-inner"'
        )
        # Change the closing div of hero-search-inner to </form>
        # The hero-search-inner div ends right before <div style="margin-top: 12px;
        html = html.replace(
            '</button>\n              </div>\n              <div style="margin-top: 12px;',
            '</button>\n              </form>\n              <div style="margin-top: 12px;'
        )
        # Give the input a name attribute so it goes to ?q=
        html = re.sub(
            r'(<input type="text" placeholder="Search bulk commodities.*?)(/>|>)',
            r'\1 name="q"\2',
            html
        )
        # Mini Search
        html = html.replace(
            '<div id="mini-search"',
            '<form id="mini-search" action="/buyer-rfqs.html" method="GET"'
        )
        html = html.replace(
            '<button style="background: var(--gold); border: none; padding: 8px 15px; cursor: pointer; font-weight: \n800; font-size: 0.85rem; color: #000;" onclick="window.location.href=\'/buyer-rfqs.html\'">dY"Z</button>\n        </div>',
            '<button type="submit" style="background: var(--gold); border: none; padding: 8px 15px; cursor: pointer; font-weight: \n800; font-size: 0.85rem; color: #000;">🔎</button>\n        </form>'
        )
        html = html.replace(
            '<button style="background: var(--gold); border: none; padding: 8px 15px; cursor: pointer; font-weight: 800; font-size: 0.85rem; color: #000;" onclick="window.location.href=\'/buyer-rfqs.html\'">🔎</button>\n        </div>',
            '<button type="submit" style="background: var(--gold); border: none; padding: 8px 15px; cursor: pointer; font-weight: 800; font-size: 0.85rem; color: #000;">🔎</button>\n        </form>'
        )
        html = re.sub(
            r'(<input type="text" placeholder="Search\.\.\." style=".*?width: 140px;")>',
            r'\1 name="q">',
            html
        )

    # 3. Founder name
    html = html.replace('Aashish S Chaturvedi', 'Ash Chaturvedi')

    # 4. Make 3 Days Trial banner 3D top notch
    old_banner = """
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
    new_banner = """
  <!-- PREMIUM 3D TRIAL BANNER -->
  <section style="padding: 80px 20px; background: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80') center/cover no-repeat; position: relative;">
      <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(2, 6, 23, 0.85); backdrop-filter: blur(8px);"></div>
      <div style="position: relative; max-width: 900px; margin: 0 auto; background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01)); border: 1px solid rgba(212,175,55,0.4); border-radius: 24px; padding: 50px; text-align: center; box-shadow: 0 30px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1); transform-style: preserve-3d; transform: perspective(1000px) rotateX(2deg);">
          <div style="position: absolute; top: -20px; left: 50%; transform: translateX(-50%); background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; font-size: 12px; letter-spacing: 2px; text-transform: uppercase; padding: 8px 24px; border-radius: 20px; box-shadow: 0 10px 20px rgba(212,175,55,0.4);">Limited Time</div>
          <h2 style="font-family: 'Playfair Display', serif; font-size: 42px; color: #fff; margin-bottom: 20px; text-shadow: 0 10px 20px rgba(0,0,0,0.5);">Unlock Your <span style="background: linear-gradient(90deg, #d4af37, #facc15); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Premium 3-Day Trial</span></h2>
          <p style="color: #cbd5e1; font-size: 18px; max-width: 700px; margin: 0 auto 40px auto; line-height: 1.6;">
              Experience the absolute pinnacle of global B2B trade. Get exactly 3 free unlocks to view verified institutional buyer details, shipping destinations, and direct executive contact numbers—completely risk-free.
          </p>
          <a href="/membership.html" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(90deg, var(--gold), #facc15); color: #000; font-weight: 900; font-size: 18px; padding: 18px 50px; border-radius: 50px; text-decoration: none; box-shadow: 0 15px 35px rgba(212,175,55,0.4), inset 0 2px 0 rgba(255,255,255,0.5); transition: all 0.3s; transform: translateZ(20px);">
              START YOUR FREE TRIAL
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>
      </div>
  </section>
  """
    if old_banner in html:
        html = html.replace(old_banner, new_banner)
    elif 'PREMIUM 3D TRIAL BANNER' not in html:
        # If we can't find it exactly, just append before FOOTER START again, but this shouldn't happen unless spacing changed
        # We can also do a regex replace if spacing is weird
        pass

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Tweaks applied!")

tweaks()
