import codecs

with codecs.open('franchise.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change the hardcoded amount 11000 to 49000
text = text.replace('amount: 11000', 'amount: 49000')

with codecs.open('franchise.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated franchise payment amount to 49000")
