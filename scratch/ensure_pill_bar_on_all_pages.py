import os

repo_dir = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

dedicated_pill_bar_html = """  <!-- ============================================================ -->
  <!-- EXECUTIVE 3D PILL ACTION BAR (ZERO OVERLAP) -->
  <!-- ============================================================ -->
  <div style="background: rgba(2, 6, 23, 0.98); border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding: 8px 5%; display: flex; justify-content: center; align-items: center; gap: 12px; flex-wrap: wrap; z-index: 99998; position: relative;">
      <a href="#" onclick="document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 8px 20px; font-weight: 800; font-size: 0.8rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-shadow: 0 1px 2px rgba(0,0,0,0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">POST A QUICK RFQ</a>
      <a href="/membership.html" style="background: linear-gradient(180deg, #facc15, #8B6508); color: #000; padding: 8px 20px; font-weight: 800; font-size: 0.8rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.6); text-shadow: 0 1px 2px rgba(255,255,255,0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">GET INSTANT BUYER</a>
      <a href="/register-supplier.html" style="background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(212, 175, 55, 0.4); color: #fff; padding: 8px 20px; font-weight: 700; font-size: 0.8rem; border-radius: 50px; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">Create Free Profile</a>
      <a href="/register-buyer.html" style="background: linear-gradient(135deg, #1e293b, #0f172a); border: 1px solid rgba(148, 163, 184, 0.4); color: #fff; padding: 8px 20px; font-weight: 700; font-size: 0.8rem; border-radius: 50px; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); text-decoration: none; text-transform: uppercase; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"><span style="color:#60a5fa; margin-right: 4px;">✦</span> BECOME A VERIFIED BUYER</a>
  </div>
"""

html_files = [
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
        
        if "EXECUTIVE 3D PILL ACTION BAR" not in content and '<header id="main-header"' in content:
            content = content.replace('<header id="main-header"', dedicated_pill_bar_html + '\n  <header id="main-header"')
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added dedicated pill action bar to {filename}!")
        elif "EXECUTIVE 3D PILL ACTION BAR" not in content and '<header' in content:
            content = content.replace('<header', dedicated_pill_bar_html + '\n  <header')
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added dedicated pill action bar before <header in {filename}!")

print("Guaranteed 3D Pill Action Bar across all key pages!")
