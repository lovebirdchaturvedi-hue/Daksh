import codecs
import re

with codecs.open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('limit', 'limit, enableIndexedDbPersistence')

setup_code = """const db = getFirestore(app);
try {
  enableIndexedDbPersistence(db).catch((err) => { console.log("Persistence error:", err); });
} catch(e) {}
"""
text = text.replace('const db = getFirestore(app);', setup_code)

with codecs.open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added offline caching")
