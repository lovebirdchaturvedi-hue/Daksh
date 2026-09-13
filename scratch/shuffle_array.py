import os

files_to_update = ['buyer-rfqs.html', 'vip-dashboard.html']

for filepath in files_to_update:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Shuffle array on load
    content = content.replace('let allData = liveRfqsData;', 'let allData = liveRfqsData.sort(() => 0.5 - Math.random());')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Added shuffle logic to buyer-rfqs.html and vip-dashboard.html')
