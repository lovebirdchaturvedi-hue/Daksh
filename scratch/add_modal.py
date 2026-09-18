import os
import re

modal_html = """
    <!-- QUOTE MODAL -->
    <div id="quoteModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:100000; align-items:center; justify-content:center; backdrop-filter: blur(5px);">
        <div class="modal-content" style="background:#0f172a; padding:40px; border-radius:20px; max-width:450px; text-align:center; border: 1px solid rgba(212,175,55,0.3); position:relative; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
            <span class="close-modal" onclick="document.getElementById('quoteModal').style.display='none'" style="position:absolute; top:15px; right:20px; font-size:28px; cursor:pointer; color:#94a3b8; transition:0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">&times;</span>
            <div class="modal-icon" style="font-size:48px; margin-bottom:20px;">✉️</div>
            <h3 style="color:#fff; font-size:24px; margin-bottom:15px; font-family:'Playfair Display', serif;">Submit Your Quote</h3>
            <p style="color:#94a3b8; font-size:15px; margin-bottom:30px; line-height:1.6;">Your complete verified profile and contact details will be securely sent directly to this buyer. They will contact you immediately to finalize the deal.</p>
            <button id="payQuoteBtn" style="background:linear-gradient(90deg, #d4af37, #facc15); color:#000; width:100%; padding:15px; border-radius:50px; font-weight:800; border:none; cursor:pointer; font-size:16px; transition:0.3s; box-shadow: 0 5px 15px rgba(212,175,55,0.3);">Pay $49 USD to Submit Quote</button>
        </div>
    </div>
    
    <script>
    function openQuoteModal(leadId) {
        document.getElementById('quoteModal').style.display = 'flex';
        document.getElementById('payQuoteBtn').onclick = function() {
            window.location.href = '/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_' + leadId;
        };
    }
    </script>
"""

def update_file(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Inject modal if not present
    if 'id="quoteModal"' not in text:
        text = text.replace('</body>', modal_html + '\n</body>')
        
    # 2. Change the onclick in buyer-rfqs/vip-dashboard/supplier-rfqs
    text = re.sub(
        r'onclick=\"window\.location\.href=\'/custom-payment\.html\?amount=49&currency=USD&ref=UnlockLead_\$\{lead\.id\}\'\"',
        r'onclick="openQuoteModal(\'${lead.id}\')"',
        text
    )
    
    # 3. Change supplier-dashboard.html
    # We replace: <a href="/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_${lead.id}" ...>⭐ Unlock Buyer Now</a>
    text = re.sub(
        r'<a href=\"/custom-payment\.html\?amount=49&currency=USD&ref=UnlockLead_\$\{lead\.id\}\"([^>]+)>(\s*)⭐ Unlock Buyer Now(\s*)</a>',
        r'<a href="#" onclick="openQuoteModal(\'${lead.id}\'); return false;"\1>\2⭐ Unlock Buyer Now\3</a>',
        text
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {filename}')

for f in ['buyer-rfqs.html', 'vip-dashboard.html', 'supplier-rfqs.html', 'supplier-dashboard.html']:
    update_file(f)
