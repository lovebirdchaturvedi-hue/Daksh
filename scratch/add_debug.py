import codecs

with codecs.open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('tbody.innerHTML = "<tr><td colspan=\'13\'>Loading suppliers</td></tr>";', '''
  tbody.innerHTML = "<tr><td colspan='13'>[DEBUG] 1. Starting loadSuppliers...</td></tr>";
  console.log("[DEBUG] 1. loadSuppliers called");
''')

text = text.replace('const q = query(collection(db, "suppliers"), limit(50));', '''
    console.log("[DEBUG] 2. Query built");
    tbody.innerHTML = "<tr><td colspan='13'>[DEBUG] 2. Requesting data from Firebase...</td></tr>";
    const q = query(collection(db, "suppliers"), limit(50));
''')

text = text.replace('const snap = await getDocs(q);', '''
    const snap = await getDocs(q);
    console.log("[DEBUG] 3. Data received, docs count:", snap.size);
    tbody.innerHTML = "<tr><td colspan='13'>[DEBUG] 3. Data received! Processing " + snap.size + " rows...</td></tr>";
''')

with codecs.open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added debug tracing to UI")
