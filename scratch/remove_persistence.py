import codecs
import re

with codecs.open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the persistence try-catch block
pattern = r'try \{\s*enableIndexedDbPersistence\(db\).*?\} catch\(e\) \{\}\s*'
text = re.sub(pattern, '', text, flags=re.DOTALL)

with codecs.open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed indexeddb persistence")
