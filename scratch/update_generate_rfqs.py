import os

filepath = 'scratch/generate_rfqs.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_commodities = """    # Spices
    "Turmeric Finger (Nizamabad)", "Cumin Seeds (Jeera)", "Green Cardamom (8mm)", 
    "Black Pepper (500 GL)", "Coriander Seeds", "Sesame Seeds (Hulled)",
    
    # Dry Fruits & Nuts
    "Cashew Nuts (W320/W240)", "Almonds (Nonpareil/Carmel)", "Walnuts (Light Halves)",
    "Pistachios (Roasted & Salted)", "Raisins (Golden/Black)", "Dried Figs", 
    "Dried Dates (Khadrawi/Zahidi)", "Macadamia Nuts",
    
    # Egyptian Herbs & Botanicals
    "Dried Hibiscus Flower (Roselle)", "Sweet Basil Leaves (Crushed)", "Peppermint Leaves",
    "Chamomile Flowers (Premium grade)", "Marjoram Leaves", "Lemongrass Cut", 
    "Dried Parsley Leaves", "Dried Dill Weed", "Calendula Petals", "Thyme Leaves",
"""

content = content.replace('    # Spices\n    "Turmeric Finger (Nizamabad)", "Cumin Seeds (Jeera)", "Green Cardamom (8mm)", \n    "Black Pepper (500 GL)", "Coriander Seeds", "Sesame Seeds (Hulled)",\n', new_commodities)

old_time = '"posted": f"{random.randint(1, 48)} hours ago"'
new_time = '"posted": f"🔴 LIVE ({random.randint(1, 59)} mins ago)"'
content = content.replace(old_time, new_time)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated generate_rfqs.py')
