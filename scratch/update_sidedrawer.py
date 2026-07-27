import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Let's find the side drawer block
start_drawer = index_html.find('<div class="side-drawer" id="sideDrawer">')
if start_drawer != -1:
    end_drawer = index_html.find('</div>', start_drawer)
    # Actually the side drawer contains multiple </a> and <hr> and finally a closing </div>.
    # It's better to just replace the whole block by finding the start of the next section, e.g., <section class="hero-premium">
    end_drawer = index_html.find('<section class="hero-premium">')
    
    if end_drawer != -1:
        # Extract the old drawer completely
        old_drawer_block = index_html[start_drawer:end_drawer]
        
        new_drawer_block = """<div class="side-drawer" id="sideDrawer">
      <!-- PREMIUM LOGO IN DRAWER -->
      <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
          <div style="width: 40px; height: 40px; background: linear-gradient(135deg, var(--gold), #8B6508); border-radius: 8px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(212, 175, 55, 0.4); border: 1px solid rgba(255,255,255,0.2);">
              <span style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 900; color: #020617; letter-spacing: -1px;">A<span style="color: #fff; font-size: 18px;">P</span></span>
          </div>
          <div style="display: flex; flex-direction: column; line-height: 1.2;">
              <span style="font-family: 'Playfair Display', serif; font-weight: 800; font-size: 20px; letter-spacing: 1px; color: #fff;">APD <span style="color: var(--gold);">Global</span></span>
          </div>
      </div>
      
      <!-- LUCRATIVE WELCOME MESSAGE -->
      <div style="margin-bottom: 30px; padding: 15px; background: rgba(201, 164, 74, 0.05); border: 1px solid rgba(201, 164, 74, 0.2); border-radius: 8px;">
          <span style="font-size: 12px; font-weight: 600; color: var(--gold); text-transform: uppercase; letter-spacing: 1px;">Welcome to APD Global Trade</span>
          <p style="font-size: 13px; color: #cbd5e1; margin-top: 8px; line-height: 1.5; font-style: italic;">We have everything you need for lucrative global expansion. Secure buyers, instant RFQs, and zero middlemen.</p>
      </div>

      <div style="font-weight: 800; color: var(--gold); letter-spacing: 3px; margin-bottom: 20px; font-size: 12px;">ALL PLATFORM OPTIONS</div>
      <a href="/index.html">🏠 Home Dashboard</a>
      <a href="/how-to-export.html">📚 How to Export</a>
      <a href="/buyer-rfqs.html">🌍 Verified Buyer RFQs</a>
      <a href="/suppliers.html">🏢 Verified Suppliers</a>
      <a href="/verification-process.html">🛡️ Trade Security & KYC</a>
      <a href="/membership.html" style="color: var(--gold); background: rgba(201, 164, 74, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(201, 164, 74, 0.3);">💎 Global Membership</a>
      <a href="/contact.html">📞 Institutional Support</a>
      
      <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.05); margin: 25px 0;">
      
      <div style="font-weight: 800; color: var(--gold); letter-spacing: 3px; margin-bottom: 20px; font-size: 12px;">SUPPLIER PORTAL</div>
      <a href="/supplier-login.html" style="font-size: 14px;">Supplier Login</a>
      <a href="/register-supplier.html" style="font-size: 14px;">Apply as Supplier</a>
      
      <hr style="border: none; border-top: 1px solid rgba(255,255,255,0.05); margin: 25px 0;">
      <a href="/brochure.html" style="font-size: 0.8rem; opacity: 0.6;">📄 Download Brochure</a>
  </div>
  
  """
        index_html = index_html.replace(old_drawer_block, new_drawer_block)

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_html)
        print("Updated side drawer successfully.")
    else:
        print("Could not find hero-premium section.")
else:
    print("Could not find sideDrawer.")
