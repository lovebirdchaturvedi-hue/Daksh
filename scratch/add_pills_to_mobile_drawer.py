import os

drawer_pills_html = """
      <!-- MOBILE DRAWER TOP 4 EXECUTIVE 3D PILL BUTTONS -->
      <div style="display: flex; flex-direction: column; gap: 10px; margin: 20px 0; padding: 0 10px;">
          <a href="#" onclick="toggleDrawer(); document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 12px 20px; font-weight: 800; font-size: 0.9rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 6px 18px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-align: center; text-decoration: none;">POST A QUICK RFQ</a>
          <a href="/membership.html" style="background: linear-gradient(180deg, #facc15, #8B6508); color: #000; padding: 12px 20px; font-weight: 800; font-size: 0.9rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 6px 18px rgba(212, 175, 55, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.6); text-align: center; text-decoration: none;">GET INSTANT BUYER</a>
          <a href="/register-supplier.html" style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(212, 175, 55, 0.4); color: #fff; padding: 12px 20px; font-weight: 700; font-size: 0.9rem; border-radius: 50px; letter-spacing: 0.5px; box-shadow: 0 6px 18px rgba(0, 0, 0, 0.5); text-align: center; text-decoration: none;">Create Free Profile</a>
          <a href="/register-buyer.html" style="background: linear-gradient(135deg, #1e293b, #0f172a); border: 1px solid rgba(148, 163, 184, 0.4); color: #fff; padding: 12px 20px; font-weight: 700; font-size: 0.9rem; border-radius: 50px; letter-spacing: 0.5px; box-shadow: 0 6px 18px rgba(0, 0, 0, 0.5); text-align: center; text-decoration: none; text-transform: uppercase;"><span style="color:#60a5fa; margin-right: 4px;">✦</span> BECOME A VERIFIED BUYER</a>
      </div>
"""

repo_dir = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

for fname in ["index.html", "membership.html"]:
    fpath = os.path.join(repo_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        target = '<div class="side-drawer" id="sideDrawer"'
        if target in content and "MOBILE DRAWER TOP 4 EXECUTIVE 3D PILL BUTTONS" not in content:
            parts = content.split(target)
            drawer_head, drawer_rest = parts[1].split('">', 1)
            new_content = parts[0] + target + drawer_head + '">' + drawer_pills_html + drawer_rest
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Added mobile drawer top pills to {fname}!")
