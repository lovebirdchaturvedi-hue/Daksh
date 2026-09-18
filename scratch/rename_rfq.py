import re

def update_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace specific visible phrases
    text = text.replace('Post RFQ', 'Post Live Order')
    text = text.replace('Broadcast RFQ', 'Broadcast Live Order')
    text = text.replace('Recent RFQs', 'Recent Live Orders')
    text = text.replace('Live RFQs', 'Live Orders')
    text = text.replace('Submit RFQ', 'Submit Live Order')
    text = text.replace('RFQ Modal', 'Live Order Modal')
    text = text.replace('Quick RFQ', 'Quick Live Order')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

update_text('index.html')
update_text('buyer-rfqs.html')
update_text('vip-dashboard.html')
update_text('supplier-rfqs.html')
print("Updated RFQ to Live Order terminology across files.")
