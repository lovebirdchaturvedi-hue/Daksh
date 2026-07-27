import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract the plans
# 1 UNLOCK PLAN
p1_match = re.search(r'<!-- 1 UNLOCK PLAN -->(.*?)<!-- 3 UNLOCKS PLAN -->', html, re.DOTALL)
p1 = p1_match.group(1).strip() if p1_match else ""

# 3 UNLOCKS PLAN
p3_match = re.search(r'<!-- 3 UNLOCKS PLAN -->(.*?)<!-- 5 UNLOCKS PLAN -->', html, re.DOTALL)
p3 = p3_match.group(1).strip() if p3_match else ""

# 3 MONTH PLAN
m3_match = re.search(r'<!-- 3 MONTH PLAN -->(.*?)(?=\n    </div>\n\n    <!-- UNLIMITED PLANS SECTION -->)', html, re.DOTALL)
m3 = m3_match.group(1).strip() if m3_match else ""

# 6 MONTH PLAN
m6_match = re.search(r'<!-- 6 MONTH PLAN -->(.*?)<!-- 12 MONTH PLAN -->', html, re.DOTALL)
m6 = m6_match.group(1).strip() if m6_match else ""

# 12 MONTH PLAN
m12_match = re.search(r'<!-- 12 MONTH PLAN -->(.*?)(?=\n    </div>\n\n    <!-- EXIT INTENT|    </div>\n\n    <div style="text-align: center;|<div class="testimonials")', html, re.DOTALL)
if not m12_match:
    # try another end boundary
    m12_match = re.search(r'<!-- 12 MONTH PLAN -->(.*?)\n    </div>\n', html, re.DOTALL)
m12 = m12_match.group(1).strip() if m12_match else ""

# 2. Modify 1 Unlock Plan
p1 = p1.replace('<div class="badge">STARTER</div>', '<div class="badge">CASUAL HOBBYIST</div>')
p1 = p1.replace('<s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹999</s> ₹399', '<s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹2,999</s> ₹1,499')
p1 = p1.replace('<s style="font-size: 1rem; color: #64748b; font-weight: 500;">$50</s> $25', '<s style="font-size: 1rem; color: #64748b; font-weight: 500;">$50</s> $19')
p1 = p1.replace('onclick="initiatePayment(\'1 Verified Buyer\', 25, 399)"', 'onclick="initiatePayment(\'1 Verified Buyer\', 19, 1499)"')
p1 = p1.replace('<li>✅ Perfect for Testing the Platform</li>', '<li>⚠️ 48-Hour Delay on Live RFQs</li>\n          <li>✅ Perfect for Testing the Platform</li>')

# 3. Modify 3 Unlocks Plan
p3 = p3.replace('<div class="badge" style="background: #d4af37; color: black;">⭐ MOST POPULAR</div>', '<div class="badge" style="background: #dc2626; color: white;">EMERGENCY UNLOCK</div>')
p3 = p3.replace('<s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹2,997</s> ₹999', '<s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹8,997</s> ₹3,499')
p3 = p3.replace('<s style="font-size: 1rem; color: #64748b; font-weight: 500;">$150</s> $50', '<s style="font-size: 1rem; color: #64748b; font-weight: 500;">$150</s> $49')
p3 = p3.replace('onclick="initiatePayment(\'3 Verified Buyers\', 50, 999)"', 'onclick="initiatePayment(\'3 Verified Buyers\', 49, 3499)"')
p3 = p3.replace('<li>✨ 66% Discount vs Single Unlock</li>', '<li>⚠️ 48-Hour Delay on Live RFQs</li>\n          <li>✨ Discount vs Single Unlock</li>')

# 4. Generate the new HTML structure for the plans section
tabs_css = """
    <style>
      .pricing-tabs {
          display: flex;
          justify-content: center;
          gap: 15px;
          margin-bottom: 50px;
      }
      .pricing-tab {
          padding: 15px 30px;
          border-radius: 50px;
          font-size: 16px;
          font-weight: 700;
          cursor: pointer;
          transition: all 0.3s;
          border: 2px solid var(--gold);
          background: transparent;
          color: var(--gold);
      }
      .pricing-tab.active {
          background: var(--gold);
          color: #000;
      }
      .tab-content {
          display: none;
      }
      .tab-content.active {
          display: block;
          animation: popIn 0.5s ease;
      }
    </style>
"""

new_structure = f"""
    {tabs_css}
    <div class="pricing-tabs">
        <div class="pricing-tab active" onclick="switchTab('memberships')">Active Memberships (Recommended)</div>
        <div class="pricing-tab" onclick="switchTab('trials')">One-Time Trials (Limited)</div>
    </div>

    <script>
        function switchTab(tab) {{
            document.querySelectorAll('.pricing-tab').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            
            if(tab === 'memberships') {{
                document.querySelectorAll('.pricing-tab')[0].classList.add('active');
                document.getElementById('tab-memberships').classList.add('active');
            }} else {{
                document.querySelectorAll('.pricing-tab')[1].classList.add('active');
                document.getElementById('tab-trials').classList.add('active');
            }}
        }}
    </script>

    <div id="tab-memberships" class="tab-content active">
        <div class="plans" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
            <!-- 3 MONTH PLAN -->
            {m3}
            <!-- 6 MONTH PLAN -->
            {m6}
            <!-- 12 MONTH PLAN -->
            {m12}
        </div>
    </div>

    <div id="tab-trials" class="tab-content">
        <div class="plans" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); max-width: 800px; margin: 0 auto;">
            <!-- 1 UNLOCK PLAN -->
            {p1}
            <!-- 3 UNLOCKS PLAN -->
            {p3}
        </div>
    </div>
"""

# Find the entire chunk to replace
start_idx = html.find('<div class="plans" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">')
# Find the end of the second plans div
end_idx = html.find('</div>\n\n    <!-- EXIT INTENT')
if end_idx == -1:
    # Try finding the close of the 12 month plan
    m12_pos = html.find('Get 12 Months Enterprise Access</button>')
    if m12_pos != -1:
        # find the next two </div>
        div1 = html.find('</div>', m12_pos)
        div2 = html.find('</div>', div1 + 6)
        end_idx = div2 + 6

# If we found both, replace!
if start_idx != -1 and end_idx != -1:
    old_block = html[start_idx:end_idx]
    
    # We also need to remove the "Unlimited Access Plans" heading since the tabs handle it
    unlimited_heading = html.find('<!-- UNLIMITED PLANS SECTION -->')
    if unlimited_heading != -1 and unlimited_heading < start_idx:
        # wait, the heading is between the two grids!
        pass

    # Actually let's just do a big regex replacement for everything from the first grid start to the end of the second grid.
    full_pattern = re.compile(r'<div class="plans" style="grid-template-columns: repeat\(auto-fit, minmax\(320px, 1fr\)\);">.*?Get 12 Months Enterprise Access</button>\s*</div>\s*</div>', re.DOTALL)
    
    # Wait, the first <div class="plans"> includes the blinking link! We shouldn't lose the blinking link.
    # We will just replace from <!-- 1 UNLOCK PLAN --> to the end of the 12 MONTH PLAN.
    
    start_replace = html.find('<!-- 1 UNLOCK PLAN -->')
    end_replace = html.find('</div>', html.find('Get 12 Months Enterprise Access</button>')) + 6
    end_replace = html.find('</div>', end_replace) + 6 # close the plans div
    
    if start_replace != -1 and end_replace != -1:
        html = html[:start_replace] + new_structure + html[end_replace:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Restructure complete")
