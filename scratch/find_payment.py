import re

with open('c:\\Users\\DELL\\.gemini\\antigravity\\playground\\vacant-ride\\daksh_repo\\membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Buttons calling initiatePayment:")
for i, line in enumerate(html.splitlines()):
    if 'initiatePayment' in line and '<a' in line:
        print(f"Line {i+1}: {line.strip()}")

print("\nPayment Modals or JS Scripts:")
# let's extract the JS that contains initiatePayment definition
script_matches = re.findall(r'<script>(.*?initiatePayment.*?)</script>', html, re.DOTALL)
for match in script_matches:
    print(match[:500] + "\n...[truncated]...")
