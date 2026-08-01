import os, re

# HTML snippet for the 4 Executive 3D Pill Action Buttons
top_pill_buttons_html = """
      <!-- TOP EXECUTIVE 3D PILL ACTION BUTTONS -->
      <div class="top-pill-actions-container" style="display: flex; align-items: center; gap: 8px; margin-left: 15px; margin-right: 15px; flex-wrap: nowrap;">
          <a href="#" onclick="document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 7px 16px; font-weight: 800; font-size: 0.75rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-shadow: 0 1px 2px rgba(0,0,0,0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">POST A QUICK RFQ</a>
          <a href="/membership.html" style="background: linear-gradient(180deg, #facc15, #8B6508); color: #000; padding: 7px 16px; font-weight: 800; font-size: 0.75rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.6); text-shadow: 0 1px 2px rgba(255,255,255,0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">GET INSTANT BUYER</a>
          <a href="/register-supplier.html" style="background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(212, 175, 55, 0.4); color: #fff; padding: 7px 16px; font-weight: 700; font-size: 0.75rem; border-radius: 50px; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">Create Free Profile</a>
          <a href="/register-buyer.html" style="background: linear-gradient(135deg, #1e293b, #0f172a); border: 1px solid rgba(148, 163, 184, 0.4); color: #fff; padding: 7px 16px; font-weight: 700; font-size: 0.75rem; border-radius: 50px; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); text-decoration: none; text-transform: uppercase; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'"><span style="color:#60a5fa; margin-right: 3px;">✦</span> BECOME A VERIFIED BUYER</a>
      </div>
"""

repo_dir = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

html_files = [
    "index.html",
    "membership.html",
    "suppliers.html",
    "buyer-rfqs.html",
    "learn-exporting.html",
    "franchise.html",
    "contact.html",
    "create-rfq.html",
    "register-supplier.html",
    "register-buyer.html",
    "admin.html"
]

for filename in html_files:
    fpath = os.path.join(repo_dir, filename)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Don't add duplicate if already present
        if "top-pill-actions-container" in content:
            continue
            
        # Target place: inside <nav> before <form id="mini-search"> or before Google translate
        if '<div id="google_translate_element"' in content:
            content = content.replace('<div id="google_translate_element"', top_pill_buttons_html + '\n      <div id="google_translate_element"')
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added top 4 3D pill action buttons to {filename}!")
        elif '</nav>' in content:
            content = content.replace('</nav>', top_pill_buttons_html + '\n    </nav>')
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added top 4 3D pill action buttons before </nav> in {filename}!")

print("All top header bars updated successfully!")
