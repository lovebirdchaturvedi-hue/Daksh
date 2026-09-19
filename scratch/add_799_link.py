import codecs

with codecs.open('membership.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

js_insert = """
        } else if (plan === 'custom799') {
            setTimeout(() => {
                initiatePayment('Premium Membership', 799, 67000);
                const hdr1 = document.querySelector('.membership-header h1');
                const hdrp = document.querySelector('.membership-header p');
                if(hdr1) hdr1.innerHTML = "Secure Payment: <span style='color: #facc15;'>799 USD</span>";
                if(hdrp) hdrp.innerHTML = "Please complete your secure payment below.";
            }, 500);
"""

text = text.replace("} else if (plan === '5buyers') {", js_insert + "} else if (plan === '5buyers') {")

with codecs.open('membership.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated membership.html for 799 USD link')
