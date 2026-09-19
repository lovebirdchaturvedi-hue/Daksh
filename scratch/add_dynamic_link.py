import codecs

with codecs.open('membership.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Add dynamic amount handler
js_insert = """
        } else if (urlParams.has('amount')) {
            const customAmount = parseFloat(urlParams.get('amount'));
            const customTitle = urlParams.get('title') || 'Custom Invoice';
            const inrEquivalent = customAmount * 84; // Approx conversion
            
            setTimeout(() => {
                initiatePayment(customTitle, customAmount, inrEquivalent);
                const hdr1 = document.querySelector('.membership-header h1');
                const hdrp = document.querySelector('.membership-header p');
                if(hdr1) hdr1.innerHTML = "Secure Payment: <span style='color: #facc15;'>" + customAmount + " USD</span>";
                if(hdrp) hdrp.innerHTML = customTitle;
            }, 500);
"""

# Inject right before the custom799 block or alongside it
if "urlParams.has('amount')" not in text:
    text = text.replace("} else if (plan === 'custom799') {", js_insert + "} else if (plan === 'custom799') {")
    with codecs.open('membership.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added dynamic amount URL logic to membership.html")
else:
    print("Dynamic logic already exists")
