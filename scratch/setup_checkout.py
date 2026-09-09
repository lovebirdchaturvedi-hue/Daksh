with open('checkout-institutional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the amount field readonly and styled
html = html.replace('<input type="number" id="payAmount" placeholder="0.00">', 
                    '<input type="number" id="payAmount" placeholder="0.00" readonly style="background: rgba(255,255,255,0.05); color: #d4af37; cursor: not-allowed;">')

# Update title and header
html = html.replace('<title>Institutional Custom Payment | APD Global Trade</title>', '<title>Institutional Checkout | APD Global Trade</title>')
html = html.replace('<h1>Elite Settlement</h1>', '<h1 id="planTitle">Checkout</h1>')
html = html.replace('<p class="subtitle">Secure processing for institutional memberships and discounted bulk packages.</p>', '<p class="subtitle" id="planSubtitle">Secure processing for your selected institutional plan.</p>')

# Replace the script block with URL parameter handling
old_script = """    <script>
        async function initiateCustomPayment() {
            const amount = document.getElementById('payAmount').value;
            const refName = document.getElementById('refName').value;
            const btn = document.getElementById('payBtn');
            const status = document.getElementById('statusMsg');

            if (!amount || amount <= 0) {
                status.innerText = "Error: Please enter a valid negotiated amount.";
                status.style.display = "block";
                return;
            }

            if (!refName) {
                status.innerText = "Error: Please enter your Registered Entity Name.";
                status.style.display = "block";
                return;
            }

            btn.innerText = "Securing Channel...";
            btn.disabled = true;
            status.style.display = "none";

            try {
                const response = await fetch('/api/phonepe-init', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        amount: parseInt(amount),
                        planName: "Elite Custom: " + refName
                    })
                });

                const data = await response.json();

                if (data.success && data.url) {
                    window.location.href = data.url;
                } else {
                    throw new Error(data.error || "Gateway Initialization Failed");
                }
            } catch (err) {
                console.error(err);
                btn.innerText = "Authorize Payment";
                btn.disabled = false;
                status.innerText = err.message;
                status.style.display = "block";
            }
        }
    </script>"""

new_script = """    <script>
        const plans = {
            'nexus': { name: 'Nexus Sovereign Pass', amount: 450000, desc: 'Unlimited Lifetime Sourcing & Institutional Market Access' },
            'bespoke1': { name: 'Bespoke Enterprise (5-20 Cr)', amount: 150000, desc: 'Custom Procurement Setup & Dedicated Agent' },
            'bespoke2': { name: 'Bespoke Enterprise (20-100 Cr)', amount: 250000, desc: 'Priority Logistics & Deep Integration' },
            'bespoke3': { name: 'Bespoke Enterprise (100+ Cr)', amount: 500000, desc: 'Full Stack Sovereign Supply Chain Architecture' }
        };

        let selectedPlan = null;

        window.onload = () => {
            const params = new URLSearchParams(window.location.search);
            const planKey = params.get('plan');
            if (plans[planKey]) {
                selectedPlan = plans[planKey];
                document.getElementById('planTitle').innerText = selectedPlan.name;
                document.getElementById('planSubtitle').innerText = selectedPlan.desc;
                document.getElementById('payAmount').value = selectedPlan.amount;
            } else {
                document.getElementById('planTitle').innerText = "Invalid Plan Selected";
                document.getElementById('payBtn').disabled = true;
                document.getElementById('payBtn').style.opacity = 0.5;
            }
        };

        async function initiateCustomPayment() {
            const amount = document.getElementById('payAmount').value;
            const refName = document.getElementById('refName').value;
            const btn = document.getElementById('payBtn');
            const status = document.getElementById('statusMsg');

            if (!selectedPlan) {
                status.innerText = "Error: Invalid plan selection.";
                status.style.display = "block";
                return;
            }

            if (!refName) {
                status.innerText = "Error: Please enter your Registered Entity Name.";
                status.style.display = "block";
                return;
            }

            btn.innerText = "Securing Channel...";
            btn.disabled = true;
            status.style.display = "none";

            try {
                const response = await fetch('/api/phonepe-init', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        amount: parseInt(amount),
                        planName: selectedPlan.name + " - " + refName
                    })
                });

                const data = await response.json();

                if (data.success && data.url) {
                    window.location.href = data.url;
                } else {
                    throw new Error(data.error || "Gateway Initialization Failed");
                }
            } catch (err) {
                console.error(err);
                btn.innerText = "Authorize Payment";
                btn.disabled = false;
                status.innerText = err.message;
                status.style.display = "block";
            }
        }
    </script>"""

html = html.replace(old_script, new_script)

with open('checkout-institutional.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated checkout-institutional.html")
