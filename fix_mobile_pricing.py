import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Pricing Updates
content = content.replace('₹59,000', '₹51,000')
content = content.replace('₹1,68,000', '₹99,000')
content = content.replace('₹2,94,000', '₹1,75,000')

# Fix 2: Mobile Overlap fixes
# Replace the CSS rule for floating buttons inside @media (max-width: 768px)
old_css = '''            /* Fix Overlapping Floating Buttons */
            #suhana-bot-container, .float.whatsapp, [style*="position: fixed; bottom: 30px; right: 30px;"] {
                bottom: 100px !important;
            }'''

new_css = '''            /* Fix Overlapping Floating Buttons & Padding */
            body {
                padding-bottom: 90px !important;
            }
            #suhana-bot-container, .float-wa, .float.whatsapp, [style*="position: fixed; bottom: 30px; right: 30px;"] {
                bottom: 100px !important;
            }'''

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Could not find the exact old_css to replace.")

# If the first mobile-action-bar is redundant, let's remove it.
# Wait, I won't remove it just in case, I'll just rely on the padding.
# But wait, looking at the user screenshot, there's only one mobile action bar visible.
# And they specifically complained about the "top stuff are hidden" (meaning the content underneath the sticky bar is hidden when scrolled all the way).

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
