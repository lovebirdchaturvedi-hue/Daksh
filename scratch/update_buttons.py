with open('membership.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace for Nexus
old_nexus_cta = """                <a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20APD%20Global%20Trade%20Nexus%20Sovereign%20Pass%20at%20%244%2C999%2FYear.%20Please%20initiate%20my%20verification." target="_blank" style="background: #fff; color: #0f172a; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; white-space: nowrap; transition: transform 0.2s; box-shadow: 0 4px 20px rgba(255,255,255,0.15);">Apply for Nexus Pass →</a>"""

new_nexus_cta = """                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; white-space: nowrap; transition: transform 0.2s; box-shadow: 0 4px 20px rgba(16,185,129,0.3); display: flex; align-items: center; gap: 8px;">
                        Pay Now <span style="font-size: 11px; background: rgba(0,0,0,0.2); padding: 3px 8px; border-radius: 4px;">PayPal / BHIM</span>
                    </a>
                    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20APD%20Global%20Trade%20Nexus%20Sovereign%20Pass." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; white-space: nowrap; transition: background 0.2s;">
                        Contact Trade Specialist
                    </a>
                </div>"""

content = content.replace(old_nexus_cta, new_nexus_cta)

# Replace for Matrix Row 1
old_row1 = """<a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%205-20%20Crore." target="_blank" style="color: #facc15; text-decoration: none; font-weight: 700; font-size: 13px;">Request Quote →</a>"""
new_row1 = """<div style="display: flex; gap: 10px;">
    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%205-20%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div>"""
content = content.replace(old_row1, new_row1)

# Replace for Matrix Row 2
old_row2 = """<a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%2020-100%20Crore." target="_blank" style="color: #facc15; text-decoration: none; font-weight: 700; font-size: 13px;">Request Quote →</a>"""
new_row2 = """<div style="display: flex; gap: 10px;">
    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%2020-100%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div>"""
content = content.replace(old_row2, new_row2)

# Replace for Matrix Row 3
old_row3 = """<a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%20above%20100%20Crore." target="_blank" style="color: #facc15; text-decoration: none; font-weight: 700; font-size: 13px;">Request Quote →</a>"""
new_row3 = """<div style="display: flex; gap: 10px;">
    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%20above%20100%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div>"""
content = content.replace(old_row3, new_row3)


with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated membership.html successfully!")
