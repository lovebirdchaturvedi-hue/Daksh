import codecs
import re

with codecs.open('membership.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add a "Generate Proforma Invoice" button to the manual section
invoice_btn_html = """
          <hr style="border-color: rgba(255,255,255,0.1); margin: 30px 0;">
          <h3 style="color: #fff; font-size: 1.2rem; margin-bottom: 15px;">Paying via International SWIFT Wire?</h3>
          <p style="font-size: 0.9rem; color: #94a3b8; margin-bottom: 20px;">Download a formal corporate Proforma Invoice containing all our Tier-1 global banking details (US, UK, EUR, CAD, AUD) for your accounting department.</p>
          <button class="btn" style="background: linear-gradient(135deg, #1e293b, #0f172a); color: #fff; border: 1px solid var(--gold);" onclick="generateInvoice()">Generate Proforma Invoice (PDF)</button>
"""

# Let's insert this before the end of manualSection
idx = text.find('id="manualSection"')
end = text.find('</div>', text.find('</div>', idx) + 1)
# Actually, let's just use replace on a known string in manualSection
old_string = "<p style=\"font-size: 0.95rem; color: #cbd5e1; margin-bottom: 20px;\"><b>Payable to: APD GLOBAL TRADE</b><br>Accepting Google Pay, PhonePe, Paytm & BHIM.</p>"
new_string = old_string + invoice_btn_html

text = text.replace(old_string, new_string)

# Now we need to add the generateInvoice() JS function
js_logic = """
    function generateInvoice() {
        if (!selectedPlan) { alert('Please select a plan first'); return; }
        const usdAmt = selectedPlan.usd;
        const planName = encodeURIComponent(selectedPlan.name);
        window.open(`/invoice.html?amount=${usdAmt}&plan=${planName}`, '_blank');
    }
"""
text = text.replace('function initiatePayment', js_logic + '\n    function initiatePayment')

with codecs.open('membership.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Injected Proforma Invoice button and logic into membership.html')
