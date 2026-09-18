import sys
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('id="rfqModal"')
sys.stdout.buffer.write(text[idx+1300:idx+2500].encode('utf-8'))
