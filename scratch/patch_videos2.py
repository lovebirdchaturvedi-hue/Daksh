import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

overlay = """
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 75px; background: linear-gradient(to bottom, rgba(2, 6, 23, 1) 10%, rgba(2, 6, 23, 0.8) 60%, transparent 100%); z-index: 5; pointer-events: none; display: flex; align-items: flex-start; justify-content: center; padding-top: 12px; box-sizing: border-box;">
    <span style="color: #4ade80; font-size: 11px; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; text-shadow: 0 2px 4px rgba(0,0,0,0.8);"><span style="margin-right: 5px;">✅</span> Verified Global Member</span>
</div>
"""

# Replace all <video ...> with <video ...> + overlay
pattern = re.compile(r'(<video.*?style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; ?".*?>\s*(?:<source.*?>)?\s*</video>)', re.DOTALL)

matches = pattern.findall(content)
if not matches:
    print("Could not find video tags to patch (with full tags). Trying simpler replace.")
    # Try just inserting after the video tag start if it doesn't have closing tag right away
    pass
else:
    new_content = pattern.sub(r'\1\n' + overlay, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched {len(matches)} videos on index.html with header overlay.")
