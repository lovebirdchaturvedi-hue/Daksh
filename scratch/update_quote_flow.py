import re

new_modal_html = """
    <!-- QUOTE MODAL -->
    <div id="quoteModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:100000; align-items:center; justify-content:center; backdrop-filter: blur(5px); overflow-y: auto; padding: 20px 0;">
        <div class="modal-content" style="background:#0f172a; padding:40px; border-radius:20px; width:90%; max-width:600px; text-align:left; border: 1px solid rgba(212,175,55,0.3); position:relative; box-shadow: 0 20px 40px rgba(0,0,0,0.5); margin: auto;">
            <span class="close-modal" onclick="document.getElementById('quoteModal').style.display='none'" style="position:absolute; top:15px; right:20px; font-size:28px; cursor:pointer; color:#94a3b8; transition:0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">&times;</span>
            
            <div id="quoteFormSection">
                <div style="display:flex; align-items:center; gap: 15px; margin-bottom: 25px;">
                    <div style="font-size:32px;">📝</div>
                    <h3 style="color:#fff; font-size:24px; font-family:'Playfair Display', serif; margin:0;">Submit Official Quote</h3>
                </div>
                <p style="color:#94a3b8; font-size:14px; margin-bottom:25px;">Please provide your most competitive terms. Buyers review multiple quotes, so ensure your specifications and pricing are accurate.</p>
                
                <form id="supplierQuoteForm" onsubmit="event.preventDefault(); showPaymentPrompt();">
                    <div style="margin-bottom: 15px;">
                        <label style="display:block; color:#cbd5e1; margin-bottom:8px; font-size:13px; font-weight:600;">Your Unit Price (USD) *</label>
                        <input type="text" required placeholder="e.g. $450 / MT" style="width:100%; padding:12px; border-radius:8px; border:1px solid #334155; background:#1e293b; color:#fff; font-size:14px;">
                    </div>
                    
                    <div style="margin-bottom: 15px;">
                        <label style="display:block; color:#cbd5e1; margin-bottom:8px; font-size:13px; font-weight:600;">Available Quantity & MOQ *</label>
                        <input type="text" required placeholder="e.g. 500 MT Available, MOQ 20 MT" style="width:100%; padding:12px; border-radius:8px; border:1px solid #334155; background:#1e293b; color:#fff; font-size:14px;">
                    </div>
                    
                    <div style="margin-bottom: 15px;">
                        <label style="display:block; color:#cbd5e1; margin-bottom:8px; font-size:13px; font-weight:600;">Quality / Grade Specifications *</label>
                        <input type="text" required placeholder="e.g. Grade A, Max Moisture 12%" style="width:100%; padding:12px; border-radius:8px; border:1px solid #334155; background:#1e293b; color:#fff; font-size:14px;">
                    </div>
                    
                    <div style="margin-bottom: 15px;">
                        <label style="display:block; color:#cbd5e1; margin-bottom:8px; font-size:13px; font-weight:600;">Preferred Payment Terms *</label>
                        <select required style="width:100%; padding:12px; border-radius:8px; border:1px solid #334155; background:#1e293b; color:#fff; font-size:14px;">
                            <option value="">Select Payment Term</option>
                            <option value="LC">100% Irrevocable L/C at Sight</option>
                            <option value="TT">T/T (30% Advance, 70% against BL)</option>
                            <option value="DP">Documents Against Payment (D/P)</option>
                            <option value="CAD">Cash Against Documents (CAD)</option>
                            <option value="Other">Other (Specify in comments)</option>
                        </select>
                    </div>
                    
                    <div style="margin-bottom: 15px;">
                        <label style="display:block; color:#cbd5e1; margin-bottom:8px; font-size:13px; font-weight:600;">Country of Origin / Exporting From *</label>
                        <input type="text" required placeholder="e.g. India, Brazil, Vietnam" style="width:100%; padding:12px; border-radius:8px; border:1px solid #334155; background:#1e293b; color:#fff; font-size:14px;">
                    </div>
                    
                    <div style="margin-bottom: 25px;">
                        <label style="display:block; color:#cbd5e1; margin-bottom:8px; font-size:13px; font-weight:600;">Additional Comments / Certifications</label>
                        <textarea rows="3" placeholder="SGS Inspection included, ISO Certified..." style="width:100%; padding:12px; border-radius:8px; border:1px solid #334155; background:#1e293b; color:#fff; font-size:14px; resize:vertical;"></textarea>
                    </div>
                    
                    <button type="submit" style="background:#2563eb; color:#fff; width:100%; padding:15px; border-radius:50px; font-weight:800; border:none; cursor:pointer; font-size:16px; transition:0.3s; box-shadow: 0 5px 15px rgba(37, 99, 235, 0.3);">Review & Submit Quote</button>
                </form>
            </div>
            
            <div id="paymentPromptSection" style="display:none; text-align:center; padding: 20px 0;">
                <div style="font-size:48px; margin-bottom:20px; color:#22c55e;">✅</div>
                <h3 style="color:#fff; font-size:24px; margin-bottom:15px; font-family:'Playfair Display', serif;">Quote Looks Competitive!</h3>
                <p style="color:#94a3b8; font-size:15px; margin-bottom:30px; line-height:1.6;">Your quote meets the buyer's criteria. To instantly deliver your quote and unlock the buyer's direct contact details (Email/WhatsApp) for final negotiation, please pay the standard lead fee.</p>
                
                <div style="background: rgba(212, 175, 55, 0.1); border: 1px dashed #d4af37; padding: 15px; border-radius: 10px; margin-bottom: 25px;">
                    <span style="color:#d4af37; font-weight: 800; font-size: 18px;">Lead Delivery Fee: $49 USD</span>
                </div>
                
                <button id="payQuoteBtn" style="background:linear-gradient(90deg, #d4af37, #facc15); color:#000; width:100%; padding:15px; border-radius:50px; font-weight:800; border:none; cursor:pointer; font-size:16px; transition:0.3s; box-shadow: 0 5px 15px rgba(212,175,55,0.3);">Pay $49 USD to Submit Quote</button>
                <p style="color:#64748b; font-size:12px; margin-top: 15px;">Secure 256-bit Encrypted Checkout</p>
            </div>
        </div>
    </div>
    
    <script>
    let currentLeadId = '';
    function openQuoteModal(leadId) {
        currentLeadId = leadId;
        document.getElementById('quoteModal').style.display = 'flex';
        document.getElementById('quoteFormSection').style.display = 'block';
        document.getElementById('paymentPromptSection').style.display = 'none';
        document.getElementById('supplierQuoteForm').reset();
    }
    
    function showPaymentPrompt() {
        document.getElementById('quoteFormSection').style.display = 'none';
        document.getElementById('paymentPromptSection').style.display = 'block';
        
        document.getElementById('payQuoteBtn').onclick = function() {
            window.location.href = '/custom-payment.html?amount=49&currency=USD&ref=UnlockLead_' + currentLeadId;
        };
    }
    </script>
"""

import os
files_to_update = ['buyer-rfqs.html', 'vip-dashboard.html', 'supplier-rfqs.html', 'supplier-dashboard.html']

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the old quoteModal and replace it entirely
    pattern = r'<!-- QUOTE MODAL -->.*?</script>'
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, new_modal_html, content, flags=re.DOTALL)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find quoteModal in {filename}")

