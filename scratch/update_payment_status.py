import codecs

with codecs.open('payment-status.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("window.location.href = '/buyer-rfqs.html'", "window.location.href = '/registration-onboarding.html'")
text = text.replace('href="/buyer-rfqs.html"', 'href="/registration-onboarding.html"')
text = text.replace('Go to Active RFQs', 'Complete Corporate Onboarding')

with codecs.open('payment-status.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated payment-status.html')
