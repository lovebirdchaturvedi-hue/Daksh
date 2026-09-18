import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

buttons_html = """
        <!-- I AM SUPPLIER / BUYER BUTTONS -->
        <div class="fade-in" style="display: flex; gap: 20px; justify-content: center; margin: 30px auto 40px auto; flex-wrap: wrap; z-index: 20; position: relative;">
            <a href="supplier-dashboard.html" style="background: #2563eb; color: white; padding: 15px 40px; border-radius: 40px; font-weight: 700; text-decoration: none; display: flex; align-items: center; gap: 10px; font-size: 16px; font-family: 'Outfit', sans-serif; box-shadow: 0 10px 25px rgba(37,99,235,0.3); transition: 0.3s; border: 1px solid #3b82f6;">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                I am Supplier
            </a>
            <a href="buyer-dashboard.html" style="background: rgba(255,255,255,0.05); color: white; padding: 15px 40px; border-radius: 40px; font-weight: 700; text-decoration: none; display: flex; align-items: center; gap: 10px; font-size: 16px; font-family: 'Outfit', sans-serif; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); transition: 0.3s;">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
                I am Buyer
            </a>
        </div>
"""

idx = text.find('<!-- MARKETPLACE SEARCH BAR -->')
if idx != -1:
    text = text[:idx] + buttons_html + '\n        ' + text[idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected supplier/buyer buttons!")
else:
    print("Marketplace search bar not found.")
