import re

with open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extract the Global Banking Partners section
banking_match = re.search(r'<section[^>]*>.*?Global Banking Partners.*?</section>', text, re.DOTALL)
if not banking_match:
    print("Could not find banking section")
    exit(1)

banking_html = banking_match.group(0)

# 2. Remove the banking section from its current location at the bottom
text = text.replace(banking_html, '')

# 3. Lower the padding to make it smaller
banking_html = banking_html.replace('padding: 120px 8%', 'padding: 60px 5%')
banking_html = banking_html.replace('padding-top: 45vh', 'padding-top: 40px') # just in case

# 4. Find the end of the pricing plans. 
# The pricing plans end around the text "Most domestic manufacturers start with the"
# Or right after the PhonePe/PayPal logos.
# Let's find: <div id="tab-trials" class="tab-content">...</div>...<!-- PAYMENT PARTNERS SECTION -->...</div>
# We can just inject it before: <!-- EXPORT COMPLIANCE & DIGITAL SETUP SERVICES -->
target = '<!-- EXPORT COMPLIANCE & DIGITAL SETUP SERVICES -->'
if target in text:
    # Inject banking_html before target
    text = text.replace(target, banking_html + '\n\n    ' + target)
    
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully moved banking partners below plans and scaled it down!")
else:
    print("Could not find target insertion point")
