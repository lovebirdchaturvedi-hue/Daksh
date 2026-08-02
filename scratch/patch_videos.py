import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the video containers and add an overlay.
# The container is: <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000; overflow: hidden; border-bottom: 2px solid #FFD700;">
# I will just do a regex replace to insert the overlay right after the video tag.

overlay = """
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 60px; background: linear-gradient(to bottom, rgba(15, 23, 42, 1) 0%, rgba(15, 23, 42, 0.8) 50%, transparent 100%); z-index: 5; pointer-events: none; display: flex; align-items: flex-start; justify-content: center; padding-top: 10px;">
    <span style="color: #FFD700; font-size: 11px; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">VERIFIED GLOBAL MEMBER</span>
</div>
"""

# Replace all <video ...></video> with <video ...></video> + overlay
# But only for the testimonial videos. 
# They have playsinline webkit-playsinline preload="metadata"
pattern = re.compile(r'(<video.*?style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;".*?></video>)', re.DOTALL)

# Check if there are matches
matches = pattern.findall(content)
if not matches:
    print("Could not find video tags to patch.")
else:
    new_content = pattern.sub(r'\1' + overlay, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched {len(matches)} videos on index.html with header overlay.")
