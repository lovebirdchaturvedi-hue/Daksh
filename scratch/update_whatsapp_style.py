import os

directory = '.'
search_str = '<a href="https://wa.me/919266418868" target="_blank" style="color: #25D366; font-weight: 700; text-decoration: none; display: flex; align-items: center; gap: 4px;">💬 WhatsApp: +919266418868</a>'
replacement_str = '<a href="https://wa.me/919266418868" target="_blank" style="background: linear-gradient(90deg, #128C7E, #25D366); color: #fff; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-decoration: none; display: flex; align-items: center; gap: 6px; box-shadow: 0 0 10px rgba(37, 211, 102, 0.4); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s ease;">💬 WhatsApp: +91 92664 18868</a>'

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
                    print(f'Applied premium WhatsApp style to {filepath}')
            except Exception as e:
                pass
