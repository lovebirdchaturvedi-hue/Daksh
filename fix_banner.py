import re

def fix_banner():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

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
    
    html = re.sub(
        r'<!-- PREMIUM TRIAL BANNER -->.*?<!-- FOOTER START -->',
        new_banner + '\n  <!-- FOOTER START -->',
        html,
        flags=re.DOTALL
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Banner replaced!")

fix_banner()
