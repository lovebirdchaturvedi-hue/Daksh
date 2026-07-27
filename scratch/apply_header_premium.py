import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Update Top-Notch Navigation CSS & Globe Mobile Fix
premium_nav_css = """
        /* TOP-NOTCH NAVIGATION BUTTONS */
        header nav a {
            position: relative;
            padding-bottom: 5px;
            font-weight: 700 !important;
            font-size: 0.85rem !important;
            letter-spacing: 2px !important;
            color: #cbd5e1 !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }
        header nav a:hover {
            color: #fff !important;
            text-shadow: 0 0 10px rgba(255,255,255,0.8);
        }
        header nav a::after {
            content: '';
            position: absolute;
            width: 0; height: 2px;
            bottom: 0; left: 0;
            background: var(--gold);
            transition: width 0.3s ease;
            box-shadow: 0 0 10px var(--gold);
        }
        header nav a:hover::after {
            width: 100%;
        }
        header nav a[href="/membership.html"] {
            background: linear-gradient(135deg, var(--gold), #8B6508) !important;
            color: #000 !important;
            padding: 10px 24px !important;
            border-radius: 50px !important;
            font-weight: 800 !important;
            box-shadow: 0 5px 20px rgba(212, 175, 55, 0.4) !important;
            border: 1px solid rgba(255,255,255,0.4) !important;
            margin-left: 20px;
        }
        header nav a[href="/membership.html"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(212, 175, 55, 0.8) !important;
        }
        header nav a[href="/membership.html"]::after {
            display: none;
        }
        
        /* MOBILE GLOBE FIX */
        @media (max-width: 768px) {
            #globe-container {
                width: 100% !important;
                left: 0 !important;
                opacity: 0.8 !important;
            }
        }
    </style>
"""
index_html = index_html.replace('</style>', premium_nav_css)

# 2. Update the Logo HTML
old_logo = """<div class="logo premium-logo" style="display: flex; flex-direction: column; line-height: 1;">
          <span style="font-family: 'Playfair Display', serif; font-weight: 700; font-size: 22px; letter-spacing: 1px;">APD <span style="color: var(--gold);">Global</span> Trade</span>
          <div style="display: inline-flex; align-items: center; gap: 8px; margin-left: 15px; padding: 3px 8px; background: rgba(201,164,74,0.1); border: 1px solid var(--gold); border-radius: 4px; vertical-align: middle;">
              <div class="pulse-green" style="width: 5px; height: 5px;"></div>
              <span style="font-size: 8px; font-weight: 800; color: var(--gold); letter-spacing: 1px; text-transform: uppercase;">Verified Institutional Gateway</span>
          </div>
          <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: var(--gold); margin-top: 5px; font-weight: 700;">Institutional Trust. Global Reach.</span>
        </div>"""

new_logo = """<a href="/" class="logo premium-logo" style="display: flex; align-items: center; gap: 15px; text-decoration: none;">
          <div style="width: 45px; height: 45px; background: linear-gradient(135deg, var(--gold), #8B6508); border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); border: 1px solid rgba(255,255,255,0.2);">
              <span style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 900; color: #020617; letter-spacing: -1px;">A<span style="color: #fff; font-size: 22px;">P</span></span>
          </div>
          <div style="display: flex; flex-direction: column; line-height: 1.2;">
              <span style="font-family: 'Playfair Display', serif; font-weight: 800; font-size: 24px; letter-spacing: 1px; color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">APD <span style="color: var(--gold);">Global</span></span>
              <span style="font-size: 10px; font-weight: 800; letter-spacing: 3px; color: #94a3b8; text-transform: uppercase;">Trade Institution</span>
          </div>
        </a>"""

index_html = index_html.replace(old_logo, new_logo)

# 3. Inject toggleDrawer JS logic at the bottom so the 3-line menu works
js_logic = """
  <script>
    function toggleDrawer() {
        const drawer = document.getElementById('sideDrawer');
        const overlay = document.getElementById('drawerOverlay');
        if(drawer && overlay) {
            drawer.classList.toggle('active');
            overlay.classList.toggle('active');
        }
    }
  </script>
</body>
"""
if "function toggleDrawer()" not in index_html:
    index_html = index_html.replace('</body>', js_logic)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
