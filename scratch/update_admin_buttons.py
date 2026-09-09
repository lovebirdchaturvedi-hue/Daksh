with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_buttons = """            <button class="gold" onclick="upd('${d.id}',{plan:'trial_3m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Set 3-Mo Trial</button>
            <button class="platinum" onclick="upd('${d.id}',{plan:'pro_6m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Set 6-Mo Elite</button>
            <button class="premium" onclick="upd('${d.id}',{plan:'elite_12m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Set 12-Mo Elite</button>
            <button class="lifetime" onclick="upd('${d.id}',{plan:'lifetime', status:'approved', role:'buyer'})">Set Lifetime (Buyer)</button>"""

new_buttons = """            <button class="gold" onclick="upd('${d.id}',{plan:'trial_3m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Professional Pass</button>
            <button class="platinum" onclick="upd('${d.id}',{plan:'pro_6m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Institutional Elite</button>
            <button class="premium" onclick="upd('${d.id}',{plan:'elite_12m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Global Enterprise</button>
            <button class="premium" style="background:linear-gradient(135deg, #d97706, #fbbf24);" onclick="upd('${d.id}',{plan:'nexus', status:'approved', unlocksUsed:0, unlockedLeads:[]})">APD Global Trade Nexus™ 4999 USD Plan</button>
            <button class="lifetime" onclick="upd('${d.id}',{plan:'buyer_1yr', status:'approved', role:'buyer'})">1 Years Buyer Membership</button>"""

html = html.replace(old_buttons, new_buttons)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated admin.html buttons.")
