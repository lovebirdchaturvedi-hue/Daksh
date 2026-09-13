import os
import random
import json

filepath = 'scratch/generate_rfqs.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the quantity generation logic
old_qty_logic = """    else:
        metric = "MT"
        qty = random.randint(20, 5000)
        if "Rice" in commodity or "Maize" in commodity or "Wheat" in commodity:"""

new_qty_logic = """    else:
        if random.random() < 0.5:
            qty_val = random.randint(1, 25) * 22
            qty_str = f"{qty_val:,} MT"
        else:
            container_type = random.choice(["20ft FCL", "40ft FCL"])
            qty_val = random.randint(2, 20)
            qty_str = f"{qty_val}x {container_type}"
        
        if "Rice" in commodity or "Maize" in commodity or "Wheat" in commodity:"""

content = content.replace(old_qty_logic, new_qty_logic)
content = content.replace('"quantity": f"{qty:,} {metric}",', '"quantity": qty_str if \'qty_str\' in locals() else f"{qty:,} {metric}",')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated generate_rfqs.py with container/MT logic")
