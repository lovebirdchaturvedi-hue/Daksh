import re

with open("supplier-rfqs.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the buttons
old_buttons = """<button onclick="openBidModal('${rId}', '${displayProduct}')" style="background:#2563eb; color:#fff; border:none; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer; flex:1;">
                    Submit Quote / Bid
                 </button>
                 <button onclick="unlockRfq('${rId}', '${sId}')" style="background:#071427; color:#c9a44a; border:1px solid #c9a44a; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer; flex:1;">
                    Unlock Contact
                 </button>"""

new_buttons = """<button onclick="openBidModal('${rId}', '${displayProduct}', '${sId}')" style="background:linear-gradient(135deg, #071427, #1a365d); color:#c9a44a; border:2px solid #c9a44a; padding:15px; border-radius:8px; font-weight:800; cursor:pointer; width:100%; text-transform:uppercase; letter-spacing:1px; box-shadow:0 4px 15px rgba(201, 164, 74, 0.2);">
                    Submit Quote & Unlock Contact (1 Credit)
                 </button>"""

content = content.replace(old_buttons, new_buttons)

# 2. Add copy whatsapp template button to the unlocked div
old_contact_html = """${r.email ? `<p><b>Email:</b> <a href="mailto:${r.email}" style="color:#2563eb; font-weight:bold;">${r.email}</a></p>` : ''}
            </div>"""

new_contact_html = """${r.email ? `<p><b>Email:</b> <a href="mailto:${r.email}" style="color:#2563eb; font-weight:bold;">${r.email}</a></p>` : ''}
              <button onclick="copyWhatsappTemplate('${r.company || r.buyerName || "Verified Buyer"}', '${displayProduct}')" style="margin-top:10px; background:#128C7E; color:white; border:none; padding:8px 15px; border-radius:6px; cursor:pointer; font-weight:bold; font-size:12px; display:flex; align-items:center; gap:5px; width:100%; justify-content:center;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
                Copy WhatsApp Message Template
              </button>
            </div>"""

content = content.replace(old_contact_html, new_contact_html)

# 3. Replace openBidModal signature
content = content.replace("window.openBidModal = (rfqId, productName) => {", "window.openBidModal = (rfqId, productName, supplierId) => {")

# 4. Replace submitBid logic completely to integrate unlockRfq logic
old_submit_bid_start = "window.submitBid = async () => {"
old_submit_bid_end = "};\n</script>"

submit_bid_index = content.find(old_submit_bid_start)
submit_bid_end_index = content.find(old_submit_bid_end, submit_bid_index)

if submit_bid_index != -1 and submit_bid_end_index != -1:
    new_submit_logic = """window.submitBid = async () => {
  const price = document.getElementById('bidPrice').value;
  const incoterms = document.getElementById('bidIncoterms').value;
  const delivery = document.getElementById('bidDelivery').value;
  const notes = document.getElementById('bidNotes').value;

  if(!price || !delivery) {
    alert("Please enter Price and Delivery Timeline.");
    return;
  }

  try {
    const sRef = doc(db, "suppliers", currentBidSupplierId);
    const sSnap = await getDoc(sRef);
    const s = sSnap.data();

    // 1-Credit-Per-Day Logic for 3_day_trial
    if (s.plan === "3_day_trial") {
      const today = new Date().toISOString().split('T')[0];
      if ((s.unlocksUsed || 0) >= 3) {
        if(confirm("You have used all 3 credits of your Trial Pass. Please upgrade for more access. View Plans?")) { window.location.href = '/membership.html'; }
        return;
      }
      if (s.lastUnlockDate === today) {
        alert("Daily Limit Reached! You have already used 1 credit today. You can submit another quote tomorrow.");
        return;
      }
      if (!confirm("Submit quote and unlock this buyer contact using 1 credit? (1 used per day)")) return;
      await updateDoc(sRef, { unlockedLeads: arrayUnion(currentBidRfqId), unlocksUsed: increment(1), lastUnlockDate: today });
    } else if (s.plan === "custom_credits") {
      const maxCredits = s.totalCredits || 0;
      if ((s.unlocksUsed || 0) >= maxCredits) {
        if(confirm("You don't have enough credits. Upgrade now to get instant credits. View Plans?")) { window.location.href = '/membership.html'; }
        return;
      }
      if (!confirm(`Submit quote and unlock this buyer contact? You have used ${s.unlocksUsed || 0} / ${maxCredits} credits.`)) return;
      await updateDoc(sRef, { unlockedLeads: arrayUnion(currentBidRfqId), unlocksUsed: increment(1) });
    } else if (["trial_3m", "premium", "gold"].includes(s.plan)) {
      if ((s.unlocksUsed || 0) >= 25) {
        if(confirm("You have reached your 25 buyer limit for the Professional Pass. Upgrade to Institutional Elite for unlimited access. Upgrade now?")) { window.location.href = '/membership.html'; }
        return;
      }
      if (!confirm(`Submit quote and unlock this buyer contact? You have used ${s.unlocksUsed || 0} / 25 credits.`)) return;
      await updateDoc(sRef, { unlockedLeads: arrayUnion(currentBidRfqId), unlocksUsed: increment(1) });
    } else {
      if ((s.unlocksUsed || 0) >= (s.totalCredits || 0) && !["pro_6m", "elite_12m", "platinum", "premium_trial"].includes(s.plan)) {
         if(confirm("You do not have enough credits to unlock this buyer. Upgrade now?")) { window.location.href = '/membership.html'; }
         return;
      }
      if (!confirm("Submit quote and unlock this buyer contact using 1 credit?")) return;
      await updateDoc(sRef, { unlockedLeads: arrayUnion(currentBidRfqId), unlocksUsed: increment(1) });
    }

    // Now write the bid
    await addDoc(collection(db, "bids"), {
      rfqId: currentBidRfqId,
      supplierId: currentBidSupplierId,
      price: Number(price),
      incoterms: incoterms,
      deliveryDays: Number(delivery),
      notes: notes,
      status: "pending",
      createdAt: serverTimestamp()
    });
    
    alert("✅ Official Quote Submitted! The buyer's direct contact details are now unlocked on your dashboard.");
    closeBidModal();
    
    // Attempt notification
    try {
        const msg = `💰 Quote & Unlock!\\nRFQ ID: ${currentBidRfqId}\\nSupplier: ${s.companyName || 'Supplier'}\\nPrice: $${price} ${incoterms}`;
        await fetch('/api/send', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ instance: "instance168990", token: "yx9xaxy5k1nbqjat", to: "+919266418868", body: msg }) });
    } catch(e) {}

    location.reload();

  } catch (e) {
    console.error("Error submitting bid: ", e);
    alert("Error submitting quote. Please try again.");
  }
};

window.copyWhatsappTemplate = (buyerName, product) => {
    const price = prompt("Enter the price you quoted (e.g. $550):");
    if(!price) return;
    const msg = `Hello ${buyerName},\\n\\nWe are an institutional supplier registered with APD Global Trade. We saw your verified RFQ for ${product}.\\n\\nOur official quote is ${price} CIF. Please let me know when you are available to discuss shipping and payment terms.\\n\\nBest Regards,`;
    navigator.clipboard.writeText(msg);
    alert("✅ Template copied to clipboard! You can now paste it into WhatsApp.");
};
"""
    content = content[:submit_bid_index] + new_submit_logic + "\n" + content[submit_bid_end_index:]

# 5. Add social proof ticker at the bottom
social_proof_html = """
<!-- Social Proof Ticker -->
<div id="biddingTicker" style="position: fixed; bottom: 0; left: 0; width: 100%; background: #071427; color: #fff; padding: 10px 0; overflow: hidden; white-space: nowrap; z-index: 999; border-top: 2px solid #c9a44a; box-shadow: 0 -5px 15px rgba(0,0,0,0.5);">
    <div id="tickerContent" style="display: inline-block; padding-left: 100%; animation: scrollTicker 25s linear infinite; font-weight: bold; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">
        <span style="color:#c9a44a;">⚡ LIVE MARKET FEED:</span> 
        <span class="ticker-item" style="margin: 0 30px;">• Supplier from India just quoted $480/MT for Sesame Seeds</span>
        <span class="ticker-item" style="margin: 0 30px;">• Supplier from Vietnam unlocked buyer for Robusta Coffee</span>
        <span class="ticker-item" style="margin: 0 30px;">• Supplier from USA quoted $920/MT for Almonds</span>
        <span class="ticker-item" style="margin: 0 30px;">• Supplier from UAE unlocked buyer for Dates (Khajoor)</span>
        <span class="ticker-item" style="margin: 0 30px;">• Supplier from Turkey quoted $1100/MT for Black Pepper</span>
    </div>
</div>
<style>
@keyframes scrollTicker {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}
</style>
"""

content = content.replace("</body>", social_proof_html + "\n</body>")

with open("supplier-rfqs.html", "w", encoding="utf-8") as f:
    f.write(content)

print("supplier-rfqs.html updated successfully!")
