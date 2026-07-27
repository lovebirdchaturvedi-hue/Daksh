import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

pro_tip_html = """
    <div style="background: rgba(212, 175, 55, 0.1); border-left: 4px solid var(--gold); padding: 20px; border-radius: 0 12px 12px 0; margin-bottom: 40px; max-width: 800px; margin-left: auto; margin-right: auto; text-align: left;">
        <h4 style="color: var(--gold); margin-bottom: 10px; font-size: 16px;">💡 Pro-Tip for Agro-Exporters (Onions/Potatoes/Mangoes)</h4>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 0;">
            Agri-export relies heavily on timing. Trial users get buyer data with a <strong>48-hour delay</strong>. <span style="color: #4ade80; font-weight: 700;">Premium members get instant WhatsApp alerts the second an RFQ lands</span>—allowing you to close the deal before the market price shifts.
        </p>
    </div>
"""

# Find where to insert it: Right after the tabs div closes, before <div id="tab-memberships"
target = '</script>\n\n    <div id="tab-memberships"'
if target in html:
    html = html.replace(target, '</script>\n\n' + pro_tip_html + '\n    <div id="tab-memberships"')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Pro-tip added")
else:
    print("Target not found")
