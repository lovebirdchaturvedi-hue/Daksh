import glob
import codecs
import re

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            
        # Replace the broken popup links with a direct link to the huge form page
        text = text.replace('href="#" onclick="document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;"',
                            'href="/create-rfq.html"')
        text = text.replace("href='#' onclick=\"document.getElementById('rfqModal').style.display='flex'; return false;\"",
                            'href="/create-rfq.html"')
        text = text.replace('href="#" onclick="toggleDrawer(); document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;"',
                            'href="/create-rfq.html"')
                            
        with codecs.open(file, 'w', encoding='utf-8') as f:
            f.write(text)
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("All buttons now link to the huge form at /create-rfq.html")
