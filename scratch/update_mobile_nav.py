import os

search_str = """      <div style="display: flex; flex-direction: column; gap: 10px; margin: 20px 0; padding: 0 10px;">
          <a href="#" onclick="toggleDrawer(); document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 12px 20px; font-weight: 800; font-size: 0.9rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 6px 18px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-align: center; text-decoration: none;">POST A QUICK RFQ</a>"""

replacement_str = """      <div style="display: flex; flex-direction: column; gap: 10px; margin: 20px 0; padding: 0 10px;">
          <a href="/buyer-rfqs.html" style="background: linear-gradient(90deg, #ef4444, #f97316); color: #fff !important; padding: 12px 20px; font-weight: 900 !important; font-size: 0.9rem !important; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; display: inline-flex; justify-content: center; align-items: center; gap: 8px; box-shadow: 0 0 20px rgba(239, 68, 68, 0.6); animation: glowingPulse 2s infinite; text-shadow: 0 1px 3px rgba(0,0,0,0.5); text-decoration: none;">
              <span style="width: 8px; height: 8px; background: #fff; border-radius: 50%; animation: pulse 1s infinite;"></span>
              🔥 LIVE ORDERS (1,500+)
          </a>
          <a href="#" onclick="toggleDrawer(); document.getElementById('rfqModal').style.display='flex'; return false;" style="background: linear-gradient(180deg, #22c55e, #166534); color: #fff; padding: 12px 20px; font-weight: 800; font-size: 0.9rem; border-radius: 50px; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 6px 18px rgba(34, 197, 94, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.4); text-align: center; text-decoration: none;">POST A QUICK RFQ</a>"""

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
                
                if search_str in content:
                    content = content.replace(search_str, replacement_str)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f'Updated mobile nav in {filepath}')
            except Exception as e:
                pass
