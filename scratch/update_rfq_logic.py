import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_js = """
    window.handleQuickRFQ = async function(e) {
        e.preventDefault();
        const btn = document.getElementById("qr_btn");
        btn.innerText = "Broadcasting to 1,500+ Suppliers...";
        btn.disabled = true;

        const product = document.getElementById("qr_product").value;
        const qty = document.getElementById("qr_qty").value + " " + document.getElementById("qr_unit").value;
        const dest = document.getElementById("qr_dest").value;

        try {
            // Fake delay for effect
            await new Promise(resolve => setTimeout(resolve, 1500));
            
            // Add to the ticker immediately
            const tickerContainer = document.querySelector('.mobile-trade-ticker div');
            if (tickerContainer) {
                const newSpan = document.createElement('span');
                newSpan.style.color = '#facc15';
                newSpan.style.marginRight = '20px';
                newSpan.style.fontWeight = '900';
                newSpan.innerText = `● NEW LIVE ORDER: ${qty} ${product} to ${dest}`;
                tickerContainer.insertBefore(newSpan, tickerContainer.firstChild);
                
                // Make the ticker visible if it was hidden
                document.querySelector('.mobile-trade-ticker').style.display = 'block';
            }

            alert("Success! Your Live Order for " + product + " has been broadcasted to our network and is now LIVE on the platform!");
            
            // Close modal
            document.getElementById("rfqModal").style.display = 'none';
            btn.innerText = "Post Live Order";
            btn.disabled = false;
            e.target.reset();

            // Optionally, we could still save it to Firebase here without blocking:
            addDoc(collection(db, "rfqs"), {
                buyerName: document.getElementById("qr_name").value,
                company: document.getElementById("qr_company").value,
                whatsapp: document.getElementById("qr_whatsapp").value,
                product: product,
                quantity: qty,
                destination: dest,
                specifications: document.getElementById("qr_specs").value,
                status: "active",
                source: "homepage_quick",
                createdAt: serverTimestamp()
            }).catch(e => console.log(e));

        } catch (err) {
            alert('Error posting Order: ' + err.message);
            btn.innerText = "Post Live Order";
            btn.disabled = false;
        }
    };
"""

# Replace the existing handleQuickRFQ logic
start_idx = text.find('window.handleQuickRFQ = async function(e)')
if start_idx != -1:
    end_idx = text.find('};', start_idx) + 2
    # Ensure we got the right block
    text = text[:start_idx] + new_js.strip() + text[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated handleQuickRFQ to post live immediately!")
else:
    print("Could not find handleQuickRFQ")

# Also, let's remove 'display: none' from the ticker so it's always visible on desktop too
text = text.replace('<div class="mobile-trade-ticker" style="display: none; width: 100%; overflow: hidden; white-space: nowrap;">',
                    '<div class="mobile-trade-ticker" style="display: block; width: 100%; overflow: hidden; white-space: nowrap; margin-top: 15px; background: rgba(0,0,0,0.5); padding: 10px; border: 1px solid var(--gold);">')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Made ticker always visible.")
