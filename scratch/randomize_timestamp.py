import os

directory = '.'
for root, dirs, files in os.walk(directory):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html') and ('buyer' in file or 'vip' in file):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            old_line = '<span style="position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.05); padding: 4px 10px; border-radius: 20px; font-size: 11px; color: #94a3b8;">${lead.posted}</span>'
            new_line = '<span style="position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.05); padding: 4px 10px; border-radius: 20px; font-size: 11px; color: #94a3b8;">${lead.posted.includes(\'LIVE\') ? \'🔴 LIVE (\' + Math.floor(Math.random() * 59 + 1) + \' mins ago)\' : lead.posted}</span>'
            
            if old_line in content:
                content = content.replace(old_line, new_line)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated {filepath}')
