import os

mem_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"
with open(mem_path, "r", encoding="utf-8") as f:
    mem_html = f.read()

# 1. Update Trade Assurance to Money-Back Guarantee
mem_html = mem_html.replace(
    '<span style="font-size: 14px; font-weight: 600;">Trade Assurance Active</span>',
    '<span style="font-size: 14px; font-weight: 600;">14-Day Money-Back Guarantee</span>'
)

# 2. Update Unlimited Leads to High-Intent Leads
mem_html = mem_html.replace(
    '<li><span class="icon">∞</span> Unlimited institutional buyer contacts</li>',
    '<li><span class="icon">∞</span> Verified High-Intent Buyer Leads</li>'
)
mem_html = mem_html.replace(
    '<li><span class="icon">✅</span> Unlimited institutional buyer contacts</li>',
    '<li><span class="icon">✅</span> Verified High-Intent Buyer Leads</li>'
)

with open(mem_path, "w", encoding="utf-8") as f:
    f.write(mem_html)


dash_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\supplier-dashboard.html"
with open(dash_path, "r", encoding="utf-8") as f:
    dash_html = f.read()

verification_portal = """
<!-- KYC VERIFICATION PORTAL -->
<div class="card" style="margin-top: 20px; border: 1px solid #c9a44a; background: #faf9f6;">
  <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #c9a44a; padding-bottom: 10px; margin-bottom: 15px;">
      <h2 style="color: #071427; margin: 0;">KYC & Government Verification</h2>
      <span style="background: #e2e8f0; color: #475569; font-size: 12px; font-weight: bold; padding: 4px 10px; border-radius: 12px;">Unverified</span>
  </div>
  <p style="font-size: 14px; color: #475569;">To achieve the <strong>"APD Vetted Supplier"</strong> badge and unlock High-Intent Institutional Buyers, please upload your mandatory trade documents.</p>
  
  <div style="margin-top: 20px;">
    <div style="margin-bottom: 15px;">
      <label style="font-weight: 600; font-size: 14px; display: block; margin-bottom: 5px;">1. GST Registration Certificate</label>
      <input type="file" id="gstFile" style="padding: 10px; border: 1px dashed #cbd5e1; width: 100%; border-radius: 6px; box-sizing: border-box; background: #fff;">
    </div>
    <div style="margin-bottom: 15px;">
      <label style="font-weight: 600; font-size: 14px; display: block; margin-bottom: 5px;">2. IEC (Import Export Code)</label>
      <input type="file" id="iecFile" style="padding: 10px; border: 1px dashed #cbd5e1; width: 100%; border-radius: 6px; box-sizing: border-box; background: #fff;">
    </div>
    <div style="margin-bottom: 15px;">
      <label style="font-weight: 600; font-size: 14px; display: block; margin-bottom: 5px;">3. APEDA / FSSAI / RCMC (Optional)</label>
      <input type="file" id="apedaFile" style="padding: 10px; border: 1px dashed #cbd5e1; width: 100%; border-radius: 6px; box-sizing: border-box; background: #fff;">
    </div>
    
    <button onclick="alert('Verification Documents Submitted! Our compliance team will review them within 24-48 hours to grant your APD Vetted Badge.')" style="background: #071427; color: #c9a44a; border: 2px solid #c9a44a; padding: 12px 24px; font-weight: 600; font-size: 16px; border-radius: 6px; cursor: pointer; width: 100%; margin-top: 10px; transition: 0.3s;">Submit for Verification</button>
  </div>
</div>
"""
if "KYC VERIFICATION PORTAL" not in dash_html:
    dash_html = dash_html.replace('</div>\n\n<script type="module">', '</div>\n' + verification_portal + '\n<script type="module">')

with open(dash_path, "w", encoding="utf-8") as f:
    f.write(dash_html)
