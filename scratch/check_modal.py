with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="rfqModal"')
print('Index:', idx)

# If it exists, let's print the modal's display style
if idx != -1:
    print(text[idx-20:idx+200])
