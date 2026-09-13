import os

files_to_update = ['buyer-rfqs.html', 'vip-dashboard.html']

for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_target = '''                        <div class="req-row">
                            <span class="req-label">Target Price</span>
                            <span class="price-highlight">${lead.target_price}</span>
                        </div>
                    </div>'''
    
    new_target = '''                        <div class="req-row">
                            <span class="req-label">Target Price</span>
                            <span class="price-highlight">${lead.target_price}</span>
                        </div>
                        <div class="req-row">
                            <span class="req-label">Status</span>
                            <span class="req-value" style="color:#facc15; font-weight:600; font-size: 11px;">⏳ ${Math.floor(Math.random() * 8) + 2} Suppliers Quoting</span>
                        </div>
                    </div>'''
    
    content = content.replace(old_target, new_target)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated UI in buyer-rfqs.html and vip-dashboard.html with spacing')
