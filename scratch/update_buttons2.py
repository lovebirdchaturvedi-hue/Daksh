with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Nexus Button
old_nexus = '<a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; white-space: nowrap; transition: transform 0.2s; box-shadow: 0 4px 20px rgba(16,185,129,0.3); display: flex; align-items: center; gap: 8px;">'
new_nexus = '<a href="#" onclick="initiatePayment(\'APD Global Trade Nexus\', 4999, 450000); return false;" style="background: #10b981; color: #fff; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; white-space: nowrap; transition: transform 0.2s; box-shadow: 0 4px 20px rgba(16,185,129,0.3); display: flex; align-items: center; gap: 8px;">'
html = html.replace(old_nexus, new_nexus)

# Fix Matrix Row 1
old_row1 = """<td style="padding: 16px 20px;"><div style="display: flex; gap: 10px;">
    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%205-20%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div></td>"""
new_row1 = """<td style="padding: 16px 20px;"><div style="display: flex; gap: 10px;">
    <a href="#" onclick="initiatePayment('Custom Enterprise Plan (5-20 Crore)', 1800, 150000); return false;" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%205-20%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div></td>"""
html = html.replace(old_row1, new_row1)

# Fix Matrix Row 2
old_row2 = """<td style="padding: 16px 20px;"><div style="display: flex; gap: 10px;">
    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%2020-100%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div></td>"""
new_row2 = """<td style="padding: 16px 20px;"><div style="display: flex; gap: 10px;">
    <a href="#" onclick="initiatePayment('Custom Enterprise Plan (20-100 Crore)', 4200, 350000); return false;" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%2020-100%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div></td>"""
html = html.replace(old_row2, new_row2)

# Fix Matrix Row 3
old_row3 = """<td style="padding: 16px 20px;"><div style="display: flex; gap: 10px;">
    <a href="custom-payment.html" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%20above%20100%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div></td>"""
new_row3 = """<td style="padding: 16px 20px;"><div style="display: flex; gap: 10px;">
    <a href="#" onclick="initiatePayment('Custom Enterprise Plan (Above 100 Crore)', 8500, 700000); return false;" style="background: #10b981; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Pay Now (PayPal/BHIM)</a>
    <a href="https://wa.me/919266418868?text=I%20want%20to%20know%20more%20about%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%20above%20100%20Crore." target="_blank" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 12px; text-decoration: none;">Know More</a>
</div></td>"""
html = html.replace(old_row3, new_row3)

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated membership.html successfully with initiatePayment")
