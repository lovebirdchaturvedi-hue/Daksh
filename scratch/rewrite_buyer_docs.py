import re

def rewrite_doc(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Simple replacements
    html = html.replace('Supplier', 'Buyer')
    html = html.replace('supplier', 'buyer')
    html = html.replace('Exporter', 'Importer')
    html = html.replace('exporter', 'importer')
    html = html.replace('SUPPLIER', 'BUYER')
    html = html.replace('EXPORTER', 'IMPORTER')

    # Add the specific disclaimer block at the top of the content area
    disclaimer_html = """
        <div style="background: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; padding: 20px; margin: 30px 0; border-radius: 4px;">
            <h4 style="color: #ef4444; margin-top: 0; font-size: 16px;">Verified Buyer Membership Terms</h4>
            <ul style="color: #cbd5e1; margin-bottom: 0; padding-left: 20px; line-height: 1.6;">
                <li><strong>Validity:</strong> This membership is strictly valid for <strong>1 Year</strong> from the date of onboarding.</li>
                <li><strong>Fixed Price:</strong> The membership is offered at a fixed price of <strong>$2,500 USD</strong> (or equivalent local currency).</li>
                <li><strong>Strictly Non-Refundable:</strong> All payments made towards the Verified Buyer Membership are final and non-refundable under any circumstances.</li>
                <li><strong>No Guarantee of Closure:</strong> APD Global Trade’s obligation is to provide you with verified exporter contacts and facilitate introductions. We do <strong>not</strong> guarantee that you will secure the exact product, price, or successfully close a trade.</li>
                <li><strong>Dual Privileges:</strong> If you wish to operate as both a Buyer and a Seller, you must upgrade to the <strong>APD Global Trade Nexus™ Plan</strong>.</li>
            </ul>
        </div>
    """

    # Inject the disclaimer right after the first paragraph or after the <h1>
    if '</h1>' in html:
        parts = html.split('</h1>', 1)
        html = parts[0] + '</h1>' + disclaimer_html + parts[1]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

rewrite_doc('buyer-agreement.html')
rewrite_doc('buyer-consent.html')
print("Successfully created buyer documents.")
