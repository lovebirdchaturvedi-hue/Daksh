import requests
import random
from datetime import datetime, timezone
import time

PROJECT_ID = "apd-globaltrade-prod"
URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/rfqs"

synthetic_companies = [
    "Global Trade Hub LLC", "AgriCorp International", "SpiceRoutes Trading", 
    "MegaFoods Ltd", "Desert Oasis General Trading", "Prime Spices & Pulses", 
    "Gulf Traders Group", "EuroFood Importers", "African Agri Supply", 
    "Nile Valley General Trading", "Cocoa Import & Dist. Group", "Global Confectionery Supply"
]

commodities = [
    "Black Pepper 500 GL", "Green Cardamom 8mm", "Cumin Seeds (Singapore Quality)", 
    "Sesame Seeds (Hulled)", "Robusta Coffee Screen 18", "Almonds Nonpareil", 
    "Cashew Nuts W320", "Long Grain White Rice", "Basmati Rice 1121", 
    "Refined Sunflower Oil", "Wheat Flour", "Milk Powder (Full Cream)", "Cocoa Powder"
]

destinations = [
    "Jebel Ali Port, UAE", "Dakar Port, Senegal", "Mombasa Port, Kenya", 
    "Nhava Sheva, India", "Rotterdam, Netherlands", "Singapore Port",
    "Port of Salalah, Oman", "Alexandria Port, Egypt", "Durban, South Africa"
]

print("Starting generation of new Synthetic RFQs...")

for i in range(20):
    buyer_name = random.choice(synthetic_companies) + f" (Trade_ID: {random.randint(1000,9999)})"
    
    # Force some Cocoa Powder leads
    if i < 10:
        chosen_product = "Cocoa Powder"
    else:
        chosen_product = random.choice(commodities)
        
    if chosen_product == "Cocoa Powder":
        qty = f"{random.randint(22, 50000)} MT"
    else:
        qty = f"{random.randint(1, 10)} x 20ft Containers"
    
    doc = {
        "fields": {
            "buyerName": {"stringValue": buyer_name},
            "company": {"stringValue": buyer_name},
            "phone": {"stringValue": f"+{random.choice(['971', '44', '1', '254', '20', '968'])}{random.randint(10000000, 99999999)}"},
            "product": {"stringValue": chosen_product},
            "commodity": {"stringValue": chosen_product},
            "quantity": {"stringValue": qty},
            "qty": {"stringValue": qty},
            "destination": {"stringValue": random.choice(destinations)},
            "isSynthetic": {"booleanValue": True},
            "status": {"stringValue": "active"},
            "createdAt": {"timestampValue": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")}
        }
    }
    
    res = requests.post(URL, json=doc)
    if res.status_code == 200:
        print(f"[{i+1}/20] ✅ Injected synthetic RFQ: {chosen_product} ({qty})")
    else:
        print(f"[{i+1}/20] ❌ Failed to inject: {res.text}")
        
    time.sleep(0.2)

print("\nDONE! Synthetic leads injected.")
