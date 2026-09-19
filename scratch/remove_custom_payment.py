import glob
import codecs
import re

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            
        if 'custom-payment.html' in text:
            # Replace all occurrences
            text = re.sub(r'[/]?custom-payment\.html[^\'"`\s]*', '/membership.html', text)
            
            with codecs.open(file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Updated {file}")
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("All custom-payment.html links replaced with /membership.html")
