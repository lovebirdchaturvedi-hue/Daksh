import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the Live Orders button huge
old_btn = r'<a href="/buyer-rfqs\.html" style="background: linear-gradient\(90deg, #ef4444, #f97316\).*?LIVE ORDERS.*?</a>'
new_btn = '''<a href="/buyer-rfqs.html" style="background: linear-gradient(90deg, #ef4444, #b91c1c); color: #fff !important; padding: 15px 30px !important; border-radius: 50px; font-weight: 900 !important; font-size: 20px !important; display: inline-flex; align-items: center; gap: 10px; border: 2px solid #fff; box-shadow: 0 0 30px rgba(239, 68, 68, 1); animation: heavyBlink 1.5s infinite; text-shadow: 0 2px 5px rgba(0,0,0,0.8); text-transform: uppercase;">
          <span style="width: 12px; height: 12px; background: #fff; border-radius: 50%; animation: pulse 0.5s infinite;"></span>
          🚨 LIVE BUYER ORDERS (1,500+) 🚨
      </a>'''

# Add heavyBlink keyframes if not exists
if 'heavyBlink' not in text:
    style_insert = '<style>\n@keyframes heavyBlink {\n  0% { transform: scale(1); opacity: 1; box-shadow: 0 0 20px #ef4444; }\n  50% { transform: scale(1.08); opacity: 0.8; box-shadow: 0 0 40px #f97316; }\n  100% { transform: scale(1); opacity: 1; box-shadow: 0 0 20px #ef4444; }\n}\n</style>\n</head>'
    text = text.replace('</head>', style_insert)

text = re.sub(old_btn, new_btn, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated index.html desktop button.')
