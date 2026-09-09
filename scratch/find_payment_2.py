import re
with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

out = []
out.append("Buttons calling initiatePayment:")
for i, line in enumerate(html.splitlines()):
    if 'initiatePayment' in line and '<a' in line:
        out.append(f"Line {i+1}: {line.strip()}")

out.append("\nPayment Modals or JS Scripts:")
script_matches = re.findall(r'<script>(.*?initiatePayment.*?)</script>', html, re.DOTALL)
for match in script_matches:
    out.append(match[:1000] + "\n...[truncated]...")

with open('scratch/payment_info_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
