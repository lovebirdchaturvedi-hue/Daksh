import os

for fname in ['index.html', 'membership.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the transform: scale(1.15); from the 4 new videos
    new_content = content.replace("transform: scale(1.15);", "")
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed CSS transform from {fname}")
