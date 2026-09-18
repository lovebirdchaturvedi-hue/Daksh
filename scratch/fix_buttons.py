import glob
import codecs

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'index.html':
        continue
    
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        
        text = text.replace('href="#" onclick="document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;"',
                            'href="/create-rfq.html"')
        
        text = text.replace('href="#" onclick="toggleDrawer(); document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;"',
                            'href="/create-rfq.html"')
                            
        with codecs.open(file, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        print(f"Skipping {file}: {e}")

print("Fixed broken buttons on all non-index pages.")
