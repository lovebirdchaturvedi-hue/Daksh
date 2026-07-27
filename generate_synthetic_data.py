import csv
import random
from datetime import datetime

# Real commodities from the platform
PRODUCTS = [
    '1121 Basmati Rice', '1401 Basmati Rice', '1509 Basmati Rice', 'Almond', 'Apple Powder', 
    'Arabica Coffee', 'Banana Powder', 'Barley', 'Black Pepper', 'Cardamom (Green)', 'Cashew Nut', 
    'Cinnamon Stick', 'Clove', 'Coffee', 'Coriander Seeds', 'Cumin Seeds', 'Dates (Khajoor)', 
    'Fennel Seeds', 'Fox Nuts (Makhana)', 'ICUMSA 45 Sugar', 'IR 64 Rice', 'Jaggery', 
    'Lentils', 'Makhana', 'Mustard Seeds', 'Olive Oil', 'Palm Oil', 'Peanuts', 
    'Raisin (Kishmish)', 'Robusta Coffee', 'Saffron', 'Sella Basmati Rice', 'Sesame Seeds', 
    'Soybean Oil', 'Sunflower Oil', 'Tamarind', 'Turmeric Finger', 'Walnuts', 'Wheat'
]

COUNTRIES_IMPORTERS = ["UAE", "USA", "Saudi Arabia", "Egypt", "Nigeria", "UK", "France", "Canada", "Singapore", "Oman", "Qatar", "Kuwait", "Bahrain", "Malaysia"]
COUNTRIES_EXPORTERS = ["India", "Vietnam", "Thailand", "Brazil", "Indonesia", "Pakistan", "Turkey", "USA", "Argentina"]

COMPANY_PREFIXES = ["Global", "Prime", "Apex", "Elite", "Royal", "Crest", "Summit", "Horizon", "Pioneer", "Nova", "Stellar", "Orient", "Gulf", "Desert", "Ocean", "Continental", "Universal", "Atlas"]
COMPANY_SUFFIXES = ["Trading Co.", "Agro LLC", "Imports", "Exports", "General Trading", "Enterprises", "Ventures", "Group", "Foods", "Holdings", "Logistics", "Commodities", "Suppliers", "Distributors"]

NAMES = ["Mohammed Al-Fayed", "James Smith", "Li Wei", "Fatima Zahra", "John Doe", "Sarah Connor", "Ahmed Hassan", "Chen Wu", "David Miller", "Elena Rossi", "Omar Al-Khatib", "Lucas Silva", "Isabella Fernandez", "Rajesh Kumar", "Anna Muller", "Michael Chang", "Tariq Aziz", "William Jones", "Maria Garcia", "Hiroshi Tanaka", "Youssef Ibrahim", "Kareem Abdul", "Aisha Rahman", "Nour El-Din"]

def generate_phone():
    return f"+{random.randint(1, 99)} {random.randint(100, 999)} {random.randint(1000000, 9999999)}"

def generate_email(name, company):
    domain = company.split()[0].lower().replace(",", "").replace(".", "")
    return f"procurement@{domain}trading.com" if random.random() > 0.5 else f"{name.split()[0].lower()}@{domain}agro.net"

def generate_data(num_records, type_data):
    data = []
    for _ in range(num_records):
        name = random.choice(NAMES)
        company = f"{random.choice(COMPANY_PREFIXES)} {random.choice(COMPANY_SUFFIXES)}"
        country = random.choice(COUNTRIES_IMPORTERS) if type_data == "Importer" else random.choice(COUNTRIES_EXPORTERS)
        data.append({
            "Company Name": company,
            "Contact Name": name,
            "Email": generate_email(name, company),
            "WhatsApp Number": generate_phone(),
            "Commodity": random.choice(PRODUCTS),
            "Country": country,
            "Quantity": "Not Mentioned"
        })
    return data

def save_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Company Name", "Contact Name", "Email", "WhatsApp Number", "Commodity", "Country", "Quantity"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} records to {filename}")

if __name__ == "__main__":
    print("Generating synthetic data for July 2026...")
    importers = generate_data(1000, "Importer")
    exporters = generate_data(1000, "Exporter")
    
    save_to_csv("July_2026_Importers.csv", importers)
    save_to_csv("July_2026_Exporters.csv", exporters)
    print("Data generation complete!")
