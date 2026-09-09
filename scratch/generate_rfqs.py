import json
import random

commodities = [
    "Non-Basmati Rice (IR64/Swarna)", "Basmati Rice (1121 Sella)", "Turmeric Finger (Nizamabad)", 
    "Cumin Seeds (Jeera)", "Green Cardamom (8mm)", "Milling Wheat", "Refined Sugar (ICUMSA 45)",
    "Raw Cotton (Shankar-6)", "HMS 1&2 Scrap Metal", "Copper Cathodes (Grade A 99.99%)",
    "Aluminum Ingots (A7)", "Solar Panels (Monocrystalline 550W)", "CNC Milling Machines",
    "Cotton T-Shirts (180 GSM)", "Denim Jeans (Men)", "Frozen Vannamei Shrimp",
    "Arabica Coffee Beans", "CTC Black Tea", "Raw Cashew Nuts (W320)",
    "Red Lentils (Masoor Dal)", "Yellow Soybeans (Non-GMO)", "Urea Fertilizer 46% N",
    "Portland Cement (Grade 42.5)", "Bitumen (Grade 60/70)", "Crude Palm Oil (CPO)",
    "Refined Sunflower Oil", "Soybean Meal", "Yellow Corn (Animal Feed)", 
    "Onions (Red Nasik)", "Fresh Cavendish Bananas", "Mango Pulp (Alphonso)",
    "Black Pepper (500 GL)", "Coriander Seeds", "Sesame Seeds (Hulled)",
    "Peanuts (Bold 40/50)", "Desiccated Coconut (Fine)", "Jute Bags",
    "Leather Safety Gloves", "Surgical Masks (3-Ply)", "Nitrile Examination Gloves",
    "Ceramic Wall Tiles (300x600)", "Polished Granite Slabs", "TMT Steel Bars",
    "Kraft Paper (120 GSM)", "Corrugated Boxes", "PET Resin (Bottle Grade)"
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

# Generate 512 leads
leads = []
for i in range(512):
    # Random ID
    rfq_id = f"RFQ-{random.randint(100000, 999999)}"
    
    # Name obfuscation
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    obfuscated_name = f"{fname} {lname[0]}***"
    
    # Select country
    country = random.choice(countries)
    
    # Select commodity
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
        target_price = f"${random.randint(300, 1500)} / MT"
        
    # Generate a random face using UI Faces / Random User generic avatars based on random numbers
    # We use a mix of male and female avatars from randomuser.me
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

print("Generated 512 leads in assets/js/live_rfqs_data.js")
