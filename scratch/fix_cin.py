import os
import re

def fix_cin():
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root: continue
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                if 'U72900MH1995PLC095642' in content:
                    # Replace the specific CIN with something safe
                    content = content.replace('U72900MH1995PLC095642', 'Application in Process')
                    
                    with open(path, 'w', encoding='utf-8', errors='ignore') as f:
                        f.write(content)
                    print(f'Fixed CIN in: {path}')

fix_cin()
