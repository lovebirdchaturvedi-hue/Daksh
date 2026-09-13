import os

with open('custom-payment.html', 'r', encoding='utf-8') as f:
    text = f.read()

script_to_add = '''
    <script>
        // Auto-fill from URL parameters
        document.addEventListener("DOMContentLoaded", function() {
            const urlParams = new URLSearchParams(window.location.search);
            if(urlParams.has('amount')) {
                document.getElementById('payAmount').value = urlParams.get('amount');
            }
            if(urlParams.has('ref')) {
                document.getElementById('refName').value = urlParams.get('ref');
            }
            if(urlParams.has('currency')) {
                document.getElementById('currencySelect').value = urlParams.get('currency');
            }
        });
    </script>
'''

if 'URLSearchParams' not in text:
    text = text.replace('</body>', script_to_add + '\n</body>')

with open('custom-payment.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated custom-payment.html with URL auto-fill')
