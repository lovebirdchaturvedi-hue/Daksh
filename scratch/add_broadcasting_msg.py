import re
import codecs

with codecs.open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update the JS to change button text to "Broadcasting to 1,500+ Suppliers..." when clicked
js_search = """document.getElementById('rfqForm').addEventListener('submit', async (e) => {
  e.preventDefault();"""

js_replace = """document.getElementById('rfqForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const submitBtn = document.getElementById('submitBtn');
  submitBtn.innerText = "Broadcasting to 1,500+ Suppliers...";
  submitBtn.disabled = true;"""

if js_search in text:
    text = text.replace(js_search, js_replace)

with codecs.open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added broadcasting loading text.")
