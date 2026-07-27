import re
import os

html_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inject the Global Partners Scrolling Banner right after the hero section.
partners_banner = """
  <!-- GLOBAL MEDIA & PARTNERS SCROLLER -->
  <div style="width: 100%; background: #020617; border-top: 1px solid rgba(212, 175, 55, 0.1); border-bottom: 1px solid rgba(212, 175, 55, 0.1); padding: 25px 0; overflow: hidden; position: relative;">
      <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 100px; background: linear-gradient(90deg, #020617, transparent); z-index: 2;"></div>
      <div style="position: absolute; right: 0; top: 0; bottom: 0; width: 100px; background: linear-gradient(270deg, #020617, transparent); z-index: 2;"></div>
      <div style="display: flex; width: 200%; animation: scrollLogos 25s linear infinite;">
          <div style="flex: 1; display: flex; justify-content: space-around; align-items: center; opacity: 0.4; filter: grayscale(100%);">
              <span style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700;">BLOOMBERG</span>
              <span style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800; letter-spacing: -1px;">Forbes</span>
              <span style="font-family: 'Playfair Display', serif; font-size: 22px; font-style: italic;">The Wall Street Journal</span>
              <span style="font-family: 'Inter', sans-serif; font-size: 26px; font-weight: 900; letter-spacing: 2px;">REUTERS</span>
              <span style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700;">THE ECONOMIC TIMES</span>
          </div>
          <div style="flex: 1; display: flex; justify-content: space-around; align-items: center; opacity: 0.4; filter: grayscale(100%);">
              <span style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700;">BLOOMBERG</span>
              <span style="font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 800; letter-spacing: -1px;">Forbes</span>
              <span style="font-family: 'Playfair Display', serif; font-size: 22px; font-style: italic;">The Wall Street Journal</span>
              <span style="font-family: 'Inter', sans-serif; font-size: 26px; font-weight: 900; letter-spacing: 2px;">REUTERS</span>
              <span style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700;">THE ECONOMIC TIMES</span>
          </div>
      </div>
  </div>
  <style>
      @keyframes scrollLogos {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
      }
  </style>
"""

# Find the end of hero section to inject the banner
html = html.replace('</section>\n\n  <!-- INSTITUTIONAL AUTHORITY STATS -->', '</section>\n' + partners_banner + '\n  <!-- INSTITUTIONAL AUTHORITY STATS -->')


# 2. Inject Social Proof Live Trade Feed script at the bottom
social_proof_script = """
    /* SOCIAL PROOF PINGS */
    const socialProofMessages = [
        "Exporter from Rajkot just unlocked 7 UAE Grain Leads",
        "Verification cleared for Maharashtra Spices Exporter",
        "New 10,000 MT Rice RFQ matched with verified suppliers",
        "Payment received: 3-Month Premium Trial activated",
        "Bank Audit complete for active Buyer in Dubai",
        "Gujarat Exporter unlocked 5 Vietnam Oil Leads",
        "Tamil Nadu Export Co. just secured a South Korea contract",
        "Panipat Textile unit matched with European buyer",
        "Indore Seeds firm cleared 7-Day Power Pass",
        "Bengaluru Tech firm secured US Govt Logistics project",
        "Hyderabad Pharma unit activated Annual Elite Plan",
        "Lucknow Handicrafts matched with UK Home Decor brand",
        "Ludhiana Cycle unit unlocked 10 African trade leads",
        "Amritsar Rice mill finalized 5-day verification",
        "Surat Diamond trader matched with Antwerp buyer network",
        "Delhi-based Trader cleared for Elite Institutional access",
        "Jodhpur Furniture unit matched with Australian distributor",
        "Agra Leather works finalized Middle-East bulk order",
        "Kanpur Hides exporter cleared annual trade audit",
        "Coimbatore Engineering unit matched with Malaysia Govt"
    ];

    function showSocialProof() {
        const toast = document.createElement('div');
        toast.style = "position:fixed; bottom:30px; left:30px; background:rgba(15,23,42,0.95); border:1px solid var(--gold); padding:15px 25px; border-radius:15px; color:white; font-size:13px; box-shadow:0 10px 30px rgba(0,0,0,0.5); z-index:10004; transform:translateY(150px); transition:0.5s transform; display:flex; align-items:center; gap:12px;";
        const randomMsg = socialProofMessages[Math.floor(Math.random() * socialProofMessages.length)];
        toast.innerHTML = `<div style="width:10px; height:10px; background:#22c55e; border-radius:50%; box-shadow: 0 0 10px #22c55e;"></div> <strong>LIVE:</strong> ${randomMsg}`;
        document.body.appendChild(toast);
        
        setTimeout(() => toast.style.transform = "translateY(0px)", 100);
        setTimeout(() => {
            toast.style.transform = "translateY(200px)";
            setTimeout(() => toast.remove(), 500);
        }, 6000);
    }

    // High frequency: Every 15-30 seconds for the homepage to look VERY active
    setInterval(() => {
        showSocialProof();
    }, 15000 + Math.random() * 15000);

    // Show first one after 2 seconds
    setTimeout(showSocialProof, 2000);
"""

# Inject before </body>
html = html.replace('</body>', '<script>\n' + social_proof_script + '\n</script>\n</body>')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
