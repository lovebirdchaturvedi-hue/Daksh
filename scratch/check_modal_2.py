import sys
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('id="rfqModal"')
sys.stdout.buffer.write(text[idx:idx+1500].encode('utf-8'))
