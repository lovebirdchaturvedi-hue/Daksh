import codecs

with codecs.open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = 'const snap = await getDocs(q);'
new_code = '''const snap = await Promise.race([
        getDocs(q),
        new Promise((_, reject) => setTimeout(() => reject(new Error("Database connection blocked! Please turn off your Ad-Blocker (Brave Shields, uBlock) or try an Incognito window. Firestore cannot connect.")), 12000))
    ]);'''

text = text.replace(old_code, new_code)

with codecs.open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added ad-blocker timeout back.")
