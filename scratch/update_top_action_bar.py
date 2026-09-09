import os

search_str = """      <a href="#" onclick="document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 8px 20px; font-weight: 800; font-size: 0.8rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-shadow: 0 1px 2px rgba(0,0,0,0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">POST A QUICK RFQ</a>"""

replacement_str = """      <a href="/buyer-rfqs.html" style="background: linear-gradient(90deg, #ef4444, #f97316); color: #fff !important; padding: 8px 20px; font-weight: 900 !important; font-size: 0.8rem !important; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; display: inline-flex; justify-content: center; align-items: center; gap: 6px; box-shadow: 0 0 20px rgba(239, 68, 68, 0.6); animation: glowingPulse 2s infinite; text-shadow: 0 1px 3px rgba(0,0,0,0.5); text-decoration: none; white-space: nowrap;">
          <span style="width: 8px; height: 8px; background: #fff; border-radius: 50%; animation: pulse 1s infinite;"></span>
          🔥 LIVE ORDERS (1,500+)
      </a>
      <a href="#" onclick="document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 8px 20px; font-weight: 800; font-size: 0.8rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-shadow: 0 1px 2px rgba(0,0,0,0.5); text-decoration: none; white-space: nowrap; transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">POST A QUICK RFQ</a>"""

directory = '.'

for root, dirs, files in os.walk(directory):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it's already there to avoid duplicates
                if search_str in content and '🔥 LIVE ORDERS (1,500+)' not in content.split(search_str)[0][-500:]:
                    content = content.replace(search_str, replacement_str)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Updated top action bar in {filepath}')
            except Exception as e:
                pass
