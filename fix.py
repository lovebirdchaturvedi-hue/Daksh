import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS rules
if '.show-inr' not in html:
    css = '''
    <style>
      .show-inr, .show-inr-block { display: none !important; }
      .show-usd, .show-usd-block { display: inline !important; }
      div.show-usd-block, li.show-usd-block { display: block !important; }
      
      body.currency-inr .show-inr { display: inline !important; }
      body.currency-inr .show-inr-block { display: block !important; }
      body.currency-inr .show-usd, body.currency-inr .show-usd-block { display: none !important; }
    </style>
'''
    html = html.replace('</head>', css + '</head>')

# 2. Fix Grid Alignment
# First grid was 280px, second was 320px. Let's make them both 320px for consistency.
html = html.replace('grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));', 'grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));')

# 3. Micro plans replacements
p1_old = '<div class="price" id="price-plan1"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹999</s> ₹399</div>'
p1_new = '<div class="price" id="price-plan1"><span class="show-inr"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹999</s> ₹399</span><span class="show-usd"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">$50</s> $25</span></div>'

p2_old = '<div class="price" id="price-plan2"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹2,997</s> ₹999</div>'
p2_new = '<div class="price" id="price-plan2"><span class="show-inr"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹2,997</s> ₹999</span><span class="show-usd"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">$150</s> $50</span></div>'

p3_old = '<div class="price" id="price-plan3"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹4,995</s> ₹1,499</div>'
p3_new = '<div class="price" id="price-plan3"><span class="show-inr"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹4,995</s> ₹1,499</span><span class="show-usd"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">$225</s> $75</span></div>'

p4_old = '<div class="price" id="price-plan4"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹7,992</s> ₹1,999</div>'
p4_new = '<div class="price" id="price-plan4"><span class="show-inr"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">₹7,992</s> ₹1,999</span><span class="show-usd"><s style="font-size: 1rem; color: #64748b; font-weight: 500;">$300</s> $100</span></div>'

html = html.replace(p1_old, p1_new)
html = html.replace(p2_old, p2_new)
html = html.replace(p3_old, p3_new)
html = html.replace(p4_old, p4_new)

# 4. High-ticket plans replacements
t1_old = '''<div class="price" style="font-size: 42px; color: #fff; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                <s style="font-size: 18px; color: #64748b; font-weight: 500;">$599</s> 
                $249
            </div>
            <div style="color: #22c55e; font-weight: 700; margin-bottom: 20px;">Or ₹19,999 INR</div>'''
t1_new = '''<div class="price" style="font-size: 42px; color: #fff; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                <span class="show-usd"><s style="font-size: 18px; color: #64748b; font-weight: 500;">$599</s> $249</span>
                <span class="show-inr"><s style="font-size: 18px; color: #64748b; font-weight: 500;">₹51,000</s> ₹19,999</span>
            </div>'''

t2_old = '''<div class="price" style="font-size: 42px; color: #fff; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                <s style="font-size: 18px; color: #64748b; font-weight: 500;">$1,199</s> 
                $599
            </div>
            <div style="color: #22c55e; font-weight: 700; margin-bottom: 20px;">Or ₹51,000 INR</div>'''
t2_new = '''<div class="price" style="font-size: 42px; color: #fff; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                <span class="show-usd"><s style="font-size: 18px; color: #64748b; font-weight: 500;">$1,199</s> $599</span>
                <span class="show-inr"><s style="font-size: 18px; color: #64748b; font-weight: 500;">₹1,19,000</s> ₹51,000</span>
            </div>'''

t3_old = '''<div class="price" style="font-size: 42px; color: #fff; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                <s style="font-size: 18px; color: #64748b; font-weight: 500;">$1,999</s> 
                $999
            </div>
            <div style="color: #22c55e; font-weight: 700; margin-bottom: 20px;">Or ₹1,19,000 INR</div>'''
t3_new = '''<div class="price" style="font-size: 42px; color: #fff; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                <span class="show-usd"><s style="font-size: 18px; color: #64748b; font-weight: 500;">$1,999</s> $999</span>
                <span class="show-inr"><s style="font-size: 18px; color: #64748b; font-weight: 500;">₹2,50,000</s> ₹1,19,000</span>
            </div>'''

html = html.replace(t1_old, t1_new)
html = html.replace(t2_old, t2_new)
html = html.replace(t3_old, t3_new)

# 5. Make sure the toggle script isn't undoing our CSS by removing the JS assignments
html = re.sub(r"document\.getElementById\('price-(trial|pro|elite)'\)\.innerHTML = [^;]+;", "", html)

# 6. Also update tax text with CSS
tax_inr_1 = "Inclusive of 18% GST"
tax_usd_1 = "No tax on export services"
tax_inr_trial = "Inclusive of 18% GST & Verification"
tax_usd_trial = "For exporters ready to explore"
tax_inr_pro = "Inclusive of 18% GST"
tax_usd_pro = "For serious exporters ready to scale"
tax_inr_elite = "Inclusive of 18% GST"
tax_usd_elite = "Maximum authority package"

# 7. Add height 100% to plans to align buttons at bottom if we use flex
# I will make all plan divs use flex and flex-direction column, and buttons margin-top auto.
html = re.sub(r'class="plan"', r'class="plan" style="display: flex; flex-direction: column;"', html)
html = re.sub(r'class="plan highlight"', r'class="plan highlight" style="display: flex; flex-direction: column;"', html)
html = re.sub(r'(<ul[^>]*>)', r'\1\n<div style="flex-grow: 1;"></div>', html) # This is a bit risky.
# Better way for buttons:
html = html.replace('<button class="btn"', '<button class="btn" style="margin-top: auto;"')
# Wait, some buttons already have style.
# Let's use a simpler regex for buttons inside plan:
# We just rely on flex-grow 1 on ul which I already added for the new plans.
# Let's fix the old plans ul to have flex-grow: 1
html = html.replace('<ul class="features">', '<ul class="features" style="flex-grow: 1;">')
html = html.replace('<ul>', '<ul style="flex-grow: 1;">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML fixed.")
