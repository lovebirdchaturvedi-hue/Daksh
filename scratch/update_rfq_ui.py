import os

files_to_update = ['buyer-rfqs.html', 'vip-dashboard.html']

for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change RFQ to Order
    content = content.replace('Global RFQs', 'Global Orders')
    content = content.replace('Global Buyer RFQs', 'Global Buyer Orders')
    content = content.replace('Search RFQs', 'Search Orders')
    content = content.replace('1,500+ Live RFQs', '1,500+ Live Orders')
    content = content.replace('No RFQs found', 'No Orders found')
    content = content.replace('Post a Quick RFQ', 'Post Requirement')
    content = content.replace('POST A QUICK RFQ', 'POST REQUIREMENT')
    
    # Update Card Template in JS
    old_target = '<span class="price-highlight">${lead.target_price}</span>\n</div>\n</div>'
    new_target = '<span class="price-highlight">${lead.target_price}</span>\n</div>\n<div class="req-row">\n<span class="req-label">Status</span>\n<span class="req-value" style="color:#facc15; font-weight:600; font-size: 11px;">⏳ ${Math.floor(Math.random() * 8) + 2} Suppliers Quoting</span>\n</div>\n</div>'
    
    content = content.replace(old_target, new_target)
    
    # Change button text
    content = content.replace('Offer Your Price', 'Submit Quote')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated UI in buyer-rfqs.html and vip-dashboard.html')
