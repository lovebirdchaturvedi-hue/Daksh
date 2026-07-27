import os

html_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Insert the banner HTML after <body>
banner_html = """
  <div id="flash-sale-banner" class="flash-sale-bar" style="display: none;">
      ⚠️ MONTH-END FLASH SALE: 50% OFF ALL PLANS ENDS IN <div class="countdown-box" id="sale-timer"></div>
  </div>
"""
html = html.replace('<body>', '<body>\n' + banner_html)

# 2. Add the flash sale JS logic right after let selectedPlan
js_injection = """
    const saleEndTime = new Date("2026-04-30T23:59:59+05:30").getTime();
    let isSaleActive = false;

    function updateFlashSale() {
        const now = new Date().getTime();
        const distance = saleEndTime - now;

        if (distance > 0) {
            isSaleActive = true;
            document.getElementById("flash-sale-banner").style.display = "block";
            
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            document.getElementById("sale-timer").innerHTML = 
                hours.toString().padStart(2, '0') + "h : " + 
                minutes.toString().padStart(2, '0') + "m : " + 
                seconds.toString().padStart(2, '0') + "s";
        } else {
            isSaleActive = false;
            document.getElementById("flash-sale-banner").style.display = "none";
        }
    }

    setInterval(updateFlashSale, 1000);
    updateFlashSale();
"""
html = html.replace("let selectedPlan = { name: '', usd: 0, inr: 0 };", "let selectedPlan = { name: '', usd: 0, inr: 0 };\n" + js_injection)

# 3. Patch toggleCurrency to handle isSaleActive
old_toggle = """            // Update Prices
            document.getElementById('price-trial').innerHTML = '₹59,000';
            document.getElementById('price-pro').innerText = '₹1,68,000';
            document.getElementById('price-elite').innerText = '₹2,94,000';"""

new_toggle_inr = """            // Update Prices
            if (isSaleActive) {
                document.getElementById('price-trial').innerHTML = '<span class="old-price" style="font-size:1.5rem;">₹59,000</span> ₹29,500';
                document.getElementById('price-pro').innerHTML = '<span class="old-price" style="font-size:1.5rem;">₹1,68,000</span> ₹84,000';
                document.getElementById('price-elite').innerHTML = '<span class="old-price" style="font-size:1.5rem;">₹2,94,000</span> ₹1,47,000';
            } else {
                document.getElementById('price-trial').innerHTML = '₹59,000';
                document.getElementById('price-pro').innerText = '₹1,68,000';
                document.getElementById('price-elite').innerText = '₹2,94,000';
            }"""
html = html.replace(old_toggle, new_toggle_inr)

old_toggle_usd = """            // Update Prices
            document.getElementById('price-trial').innerHTML = '$499';
            document.getElementById('price-pro').innerText = '$2,000';
            document.getElementById('price-elite').innerText = '$3,500';"""

new_toggle_usd = """            // Update Prices
            if (isSaleActive) {
                document.getElementById('price-trial').innerHTML = '<span class="old-price" style="font-size:1.5rem;">$499</span> $249';
                document.getElementById('price-pro').innerHTML = '<span class="old-price" style="font-size:1.5rem;">$2,000</span> $1,000';
                document.getElementById('price-elite').innerHTML = '<span class="old-price" style="font-size:1.5rem;">$3,500</span> $1,750';
            } else {
                document.getElementById('price-trial').innerHTML = '$499';
                document.getElementById('price-pro').innerText = '$2,000';
                document.getElementById('price-elite').innerText = '$3,500';
            }"""
html = html.replace(old_toggle_usd, new_toggle_usd)

# 4. Patch initiatePayment
old_initiate = """    function initiatePayment(planName, usd, inr) {
        selectedPlan = { name: planName, usd, inr };"""
new_initiate = """    function initiatePayment(planName, usd, inr) {
        if (isSaleActive) {
            usd = Math.floor(usd / 2);
            inr = Math.floor(inr / 2);
        }
        selectedPlan = { name: planName, usd, inr };"""
html = html.replace(old_initiate, new_initiate)

# 5. Call toggleCurrency ON LOAD so it initializes the 50% display right away (since default is USD)
old_script_start = "setInterval(function(){}, 1000);"
new_script_start = "setInterval(function(){}, 1000);\n    // Force render on load\n    setTimeout(() => { currentCurrency = 'INR'; toggleCurrency(); }, 100);"
html = html.replace(old_script_start, new_script_start)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
