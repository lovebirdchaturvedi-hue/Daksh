import pandas as pd

file_path = r"C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS Final.xlsx"

leads_data = {
    "04 2354793": "Spices",
    "052 5064269": "Spices, Pulses, Legumes, Nuts, Grains, Dry Fruits",
    "04 2944715": "Spices, Rice, Milk Powder Suppliers, Sugar, Pulses, Food Products, Cooking Oil, Flour, Food Suppliers",
    "04 2263574": "Spices",
    "04 8829299": "Spices, Rice, Food Importers, Chocolates, Food Products, Pulses",
    "052 7108880": "Spices",
    "04 2979189": "Spices, Rice, Food Importers And Wholesalers, Fish and Seafood Processors, Food Suppliers, Frozen Food, Pulses, Sugar Brokers and Wholesalers",
    "050 9569939": "Spices, Ghee, Vegetable Oil",
    "052 1504512": "Spices, General Trading, Metals, Steel, Copper, Aluminium, Foodstuff Trading, Waste Management Equipment, Readymade Clothing",
    "04 2251048": "Spices, Coffee Importers and Wholesalers",
    "04 5687185": "Spices",
    "04 2352515": "Spices, Rice, Frozen Food, Sugar Brokers and Wholesalers",
    "055 8612680": "Spices, Pickles, Rice",
    "04 5644106": "Spices, Rice, Sauces",
    "04 2264775": "Spices",
    "04 3474843": "Spices",
    "04 2671621": "Spices, Flour Merchants and Spice Mills, Food Importers And Wholesalers",
    "04 2268791": "Spices, Food Importers And Wholesalers",
    "04 2265211": "Spices, Food Suppliers",
    "058 5832019": "Spices, Millets, Cereals, Dry Fruits",
    "04 4335655": "Spices, Food and Beverages Trading, Tea",
    "04 3281988": "Spices, Clothing, Pulses, Meat Merchant, Metals, Minerals, Auto Spare Parts, Oil, Mechanical Supplies, Building Material, Fresh Fruits and Vegetables Wholesalers",
    "04 2266854": "Spices, Dry Fruits, Vegetable, Food Suppliers",
    "04 2264043": "Spices",
    "055 3567625": "Spices, Rice, Pulses",
    "04 5527207": "Spices, Rice, Foodstuff Trading",
    "04 3479905": "Spices, Fruits Dried, Nuts, Pulses, Roastery",
    "04 3371766": "Spices",
    "04 3203744": "Spices",
    "04 2262855": "Spices",
    "052 7542126": "Spices, Agro Spices, Rice, T Shirts, API Development, Desktop Application Development, Business Intelligence, Food Importers and Exporters, Food Importers And Wholesalers, Web Development, IT Solutions, Web Design, Social Media Marketing, IT Consultants, Areca Leaf Disposable Items, Ladies Garments, Data Backend and Front End Restoration, Software As A Service, Software Application Development, E-Commerce Website, Digital Marketing, Garments, Shirt, Mens Garments, International BPO Call Centre, Mobile and Remote Network, Web Application Performance, Database Management, Food Supplies, Foodstuff Trading, Wheat, Mustard Seeds, Web Development Front End and Backend, Agricultural Products, Garments Readymade Retail",
    "04 2980073": "Spices",
    "050 5085004": "Spices, Rice, Dry Fruits, Herbs, Pulses, Grains, Cereals",
    "04 2252246": "Spices",
    "04 3309641": "Spices, Dry Fruits",
    "056 6529222": "Spices, Tea Importers and Merchants",
    "04 43510195": "Chinese Restaurants, Indian Restaurants",
}

print(f"Reading {file_path}...")
df = pd.read_excel(file_path)

updates = 0
for i in range(len(df)):
    original_phone = str(df.loc[i, 'Original_Phone']) if pd.notna(df.loc[i, 'Original_Phone']) else ""
    if original_phone in leads_data:
        df.loc[i, 'Commodity'] = leads_data[original_phone]
        updates += 1

print(f"Updated commodities for {updates} rows.")
df.to_excel(file_path, index=False)
print("Saved successfully!")
