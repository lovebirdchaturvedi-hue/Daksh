import json
import random

commodities = [
    # Grains & Cereals
    "Non-Basmati Rice (IR64/Swarna)", "Basmati Rice (1121 Sella)", "Basmati Rice (Pusa 1121)", 
    "Basmati Rice (1509 Sella)", "Basmati Rice (Traditional)", "Non-Basmati Rice (PR14)", 
    "Non-Basmati Rice (Sona Masoori)", "Broken Rice (100%)", "Parboiled Rice",
    "Milling Wheat", "Yellow Maize (Animal Feed)", "White Maize (Human Consumption)",
    
    # Sugar
    "Refined Sugar (ICUMSA 45)", "Refined Sugar (ICUMSA 150)", "Raw Sugar (ICUMSA 600-1200)",
    
    # Spices
    "Turmeric Finger (Nizamabad)", "Cumin Seeds (Jeera)", "Green Cardamom (8mm)", 
    "Black Pepper (500 GL)", "Coriander Seeds", "Sesame Seeds (Hulled)",
    
    # Oils
    "Crude Palm Oil (CPO)", "Refined Palm Olein (CP10)", "Refined Sunflower Oil", 
    "Crude Sunflower Oil", "Refined Soybean Oil",
    
    # Pulses & Legumes
    "Red Lentils (Masoor Dal)", "Yellow Lentils (Moong Dal)", "Black Gram (Urad Dal)", 
    "Pigeon Peas (Toor Dal)", "Yellow Soybeans (Non-GMO)", "Peanuts (Bold 40/50)",
    
    # Coffee & Cocoa
    "Arabica Coffee Beans (Grade 1)", "Robusta Coffee Beans", "Raw Cocoa Beans", 
    "Cocoa Powder (Alkalized)", "Cocoa Butter", "CTC Black Tea",
    
    # Frozen Foods & Nonveg
    "Frozen Vannamei Shrimp", "Frozen Halal Beef (Quarter Carcass)", "Frozen Chicken Paws (Grade A)", 
    "Frozen Whole Chicken", "Frozen Atlantic Salmon", "Frozen Mackerel Fish",
    
    # Fresh Produce & Nuts
    "Onions (Red Nasik)", "Fresh Cavendish Bananas", "Mango Pulp (Alphonso)",
    "Raw Cashew Nuts (W320)", "Desiccated Coconut (Fine)",
    
    # Industrial & Metals
    "HMS 1&2 Scrap Metal", "Copper Cathodes (Grade A 99.99%)", "Aluminum Ingots (A7)", 
    "Urea Fertilizer 46% N", "Portland Cement (Grade 42.5)", "Bitumen (Grade 60/70)", 
    "PET Resin (Bottle Grade)", "TMT Steel Bars", "Polished Granite Slabs", "Ceramic Wall Tiles (300x600)",
    
    # Manufactured Goods
    "Raw Cotton (Shankar-6)", "Cotton T-Shirts (180 GSM)", "Denim Jeans (Men)", 
    "Solar Panels (Monocrystalline 550W)", "CNC Milling Machines", "Jute Bags",
    "Leather Safety Gloves", "Surgical Masks (3-Ply)", "Nitrile Examination Gloves",
    "Kraft Paper (120 GSM)", "Corrugated Boxes"
]

countries = [
    {"name": "USA", "flag": "🇺🇸", "code": "US"}, {"name": "UK", "flag": "🇬🇧", "code": "GB"},
    {"name": "UAE", "flag": "🇦🇪", "code": "AE"}, {"name": "Saudi Arabia", "flag": "🇸🇦", "code": "SA"},
    {"name": "Oman", "flag": "🇴🇲", "code": "OM"}, {"name": "Qatar", "flag": "🇶🇦", "code": "QA"},
    {"name": "Bahrain", "flag": "🇧🇭", "code": "BH"}, {"name": "Kuwait", "flag": "🇰🇼", "code": "KW"},
    {"name": "Singapore", "flag": "🇸🇬", "code": "SG"}, {"name": "Malaysia", "flag": "🇲🇾", "code": "MY"},
    {"name": "Vietnam", "flag": "🇻🇳", "code": "VN"}, {"name": "Thailand", "flag": "🇹🇭", "code": "TH"},
    {"name": "Australia", "flag": "🇦🇺", "code": "AU"}, {"name": "Canada", "flag": "🇨🇦", "code": "CA"},
    {"name": "Germany", "flag": "🇩🇪", "code": "DE"}, {"name": "France", "flag": "🇫🇷", "code": "FR"},
    {"name": "Italy", "flag": "🇮🇹", "code": "IT"}, {"name": "Spain", "flag": "🇪🇸", "code": "ES"},
    {"name": "Netherlands", "flag": "🇳🇱", "code": "NL"}, {"name": "South Africa", "flag": "🇿🇦", "code": "ZA"},
    {"name": "Egypt", "flag": "🇪🇬", "code": "EG"}, {"name": "Nigeria", "flag": "🇳🇬", "code": "NG"},
    {"name": "Kenya", "flag": "🇰🇪", "code": "KE"}, {"name": "Japan", "flag": "🇯🇵", "code": "JP"},
    {"name": "South Korea", "flag": "🇰🇷", "code": "KR"}, {"name": "Bangladesh", "flag": "🇧🇩", "code": "BD"},
    {"name": "Sri Lanka", "flag": "🇱🇰", "code": "LK"}, {"name": "Mexico", "flag": "🇲🇽", "code": "MX"}
]

first_names = ["John", "Ahmed", "Mohammed", "David", "Michael", "Sarah", "Fatima", "Carlos", "Ali", "Hassan", 
               "Omar", "Maria", "Laura", "James", "Robert", "William", "Daniel", "Thomas", "Tariq", "Zainab", 
               "Yusuf", "Ibrahim", "Elena", "Lucas", "Sophie", "Kevin", "Oliver", "Emma", "Isabella", "Amir"]

last_names = ["Smith", "Al-Fayed", "Muller", "Garcia", "Silva", "Johnson", "Brown", "Williams", "Jones", "Davis",
              "Al-Maktoum", "Khan", "Rahman", "Chen", "Lee", "Kim", "Nguyen", "Patel", "Sharma", "Singh",
              "Rossi", "Costa", "Martinez", "Gonzalez", "Rodriguez", "Fernandez", "Lopez", "Perez", "Gomez"]

# Generate 1500 leads
leads = []
for i in range(1500):
    rfq_id = f"RFQ-{random.randint(100000, 999999)}"
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    obfuscated_name = f"{fname} {lname[0]}***"
    country = random.choice(countries)
    commodity = random.choice(commodities)
    
    # Determine quantity and metric based on commodity
    if "Machine" in commodity or "Panel" in commodity:
        metric = "Units"
        qty = random.randint(10, 500)
        target_price = f"${random.randint(50, 5000)} / Unit"
    elif "Garments" in commodity or "T-Shirts" in commodity or "Jeans" in commodity or "Gloves" in commodity or "Masks" in commodity:
        metric = "Pieces"
        qty = random.randint(5000, 100000)
        target_price = f"${round(random.uniform(0.5, 15.0), 2)} / Pc"
    else:
        metric = "MT"
        qty = random.randint(20, 5000)
        if "Rice" in commodity or "Maize" in commodity or "Wheat" in commodity:
            target_price = f"${random.randint(250, 600)} / MT"
        elif "Sugar" in commodity:
            target_price = f"${random.randint(450, 650)} / MT"
        elif "Oil" in commodity:
            target_price = f"${random.randint(800, 1400)} / MT"
        elif "Frozen" in commodity:
            target_price = f"${random.randint(1500, 4500)} / MT"
        elif "Coffee" in commodity or "Cocoa" in commodity:
            target_price = f"${random.randint(2500, 5500)} / MT"
        else:
            target_price = f"${random.randint(300, 1500)} / MT"
        
    gender = random.choice(["men", "women"])
    avatar_num = random.randint(1, 99)
    avatar_url = f"https://randomuser.me/api/portraits/{gender}/{avatar_num}.jpg"
    
    lead = {
        "id": rfq_id,
        "name": obfuscated_name,
        "country": country["name"],
        "flag": country["flag"],
        "commodity": commodity,
        "quantity": f"{qty:,} {metric}",
        "target_price": target_price,
        "avatar": avatar_url,
        "posted": f"{random.randint(1, 48)} hours ago"
    }
    leads.append(lead)

js_content = f"const liveRfqsData = {json.dumps(leads, indent=2)};"

with open('assets/js/live_rfqs_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Generated 1500 leads in assets/js/live_rfqs_data.js")
