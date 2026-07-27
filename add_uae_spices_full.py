import pandas as pd

file_path = r"C:\Users\DELL\Downloads\Daksh\APD GLOBAL BUYERS Final.xlsx"

# Tuple of (Company Name, Phone, Commodities)
leads = [
    ("Eden Val Trading LLC", "04 2354793", "Spices"),
    ("Elite Food Supplements Manufacturing Co LLC", "052 5064269", "Spices, Pulses, Legumes, Nuts, Grains, Dry Fruits"),
    ("GAJS Foodstuff Trading LLC", "04 2944715", "Spices, Rice, Milk Powder Suppliers, Sugar, Pulses, Food Products, Cooking Oil, Flour, Food Suppliers"),
    ("Ghuloom Hussain Ali Naqi Trading", "04 2263574", "Spices"),
    ("Global Green Food Trading LLC", "04 8829299", "Spices, Rice, Food Importers, Chocolates, Food Products, Pulses"),
    ("GRK Food Industry LLC", "052 7108880", "Spices"),
    ("High Volume Food Stuff Trading LLC", "04 2979189", "Spices, Rice, Food Importers And Wholesalers, Fish and Seafood Processors, Food Suppliers, Frozen Food, Pulses, Sugar Brokers and Wholesalers"),
    ("Honest Origin Good Foodstuff Trading LLC", "050 9569939", "Spices, Ghee, Vegetable Oil"),
    ("Inox Ventures FZCO", "052 1504512", "Spices, General Trading, Metals, Steel, Copper, Aluminium, Foodstuff Trading, Waste Management Equipment, Readymade Clothing"),
    ("Kahraman Dubai General Trading Co", "04 2251048", "Spices, Coffee Importers and Wholesalers"),
    ("Kamaki Foodstuff Trading LLC", "04 5687185", "Spices"),
    ("Kinda Food Stuff Trading LLC", "04 2352515", "Spices, Rice, Frozen Food, Sugar Brokers and Wholesalers"),
    ("Ridhu Foodstuff Trading LLC", "055 8612680", "Spices, Pickles, Rice"),
    ("Meridian PF General Trading LLC", "04 5644106", "Spices, Rice, Sauces"),
    ("Abdul Hamid Al Reza Co", "04 2264775", "Spices"),
    ("Al Maya Trading Co LLC", "04 3474843", "Spices"),
    ("Alwan Dubai Mill", "04 2671621", "Spices, Flour Merchants and Spice Mills, Food Importers And Wholesalers"),
    ("Brooks Trading Company LLC", "04 2268791", "Spices, Food Importers And Wholesalers"),
    ("Dhirani Foodstuff Company LLC", "04 2265211", "Spices, Food Suppliers"),
    ("Dow Alhaya Flour Mill LLC", "058 5832019", "Spices, Millets, Cereals, Dry Fruits"),
    ("Leoste Global LLC FZ", "04 4335655", "Spices, Food and Beverages Trading, Tea"),
    ("MKK Trade", "04 3281988", "Spices, Clothing, Pulses, Meat Merchant, Metals, Minerals, Auto Spare Parts, Oil, Mechanical Supplies, Building Material, Fresh Fruits and Vegetables Wholesalers"),
    ("Najmat Al Abeer Trading LLC", "04 2266854", "Spices, Dry Fruits, Vegetable, Food Suppliers"),
    ("Naseeri General Trading Company LLC", "04 2264043", "Spices"),
    ("Nawab Foodstuff Trading LLC", "055 3567625", "Spices, Rice, Pulses"),
    ("Noor Albarakah Goods Wholesalers LLC", "04 5527207", "Spices, Rice, Foodstuff Trading"),
    ("Nutty Nuts Foodstuff Factory (LLC)", "04 3479905", "Spices, Fruits Dried, Nuts, Pulses, Roastery"),
    ("Prince Sweets", "04 3371766", "Spices"),
    ("Rabiah Trading", "04 3203744", "Spices"),
    ("Rashwell Company (LLC)", "04 2262855", "Spices"),
    ("Rospand Global Techno Services", "052 7542126", "Spices, Agro Spices, Rice, T Shirts, API Development, Desktop Application Development, Business Intelligence, Food Importers and Exporters, Food Importers And Wholesalers, Web Development, IT Solutions, Web Design, Social Media Marketing, IT Consultants, Areca Leaf Disposable Items, Ladies Garments, Data Backend and Front End Restoration, Software As A Service, Software Application Development, E-Commerce Website, Digital Marketing, Garments, Shirt, Mens Garments, International BPO Call Centre, Mobile and Remote Network, Web Application Performance, Database Management, Food Supplies, Foodstuff Trading, Wheat, Mustard Seeds, Web Development Front End and Backend, Agricultural Products, Garments Readymade Retail"),
    ("Royal Golden General Trading", "04 2980073", "Spices"),
    ("Sakhi Khan International Foodstuff Trading LLC", "050 5085004", "Spices, Rice, Dry Fruits, Herbs, Pulses, Grains, Cereals"),
    ("Sher Muhammed Trading", "04 2252246", "Spices"),
    ("Yousify General Trading Co. LLC", "04 3309641", "Spices, Dry Fruits"),
    ("Zuva Foodstuff Trading LLC", "056 6529222", "Spices, Tea Importers and Merchants"),
    ("Spices Garden Cafe", "04 43510195", "Chinese Restaurants, Indian Restaurants"),
]

new_rows = []
for name, phone, commodities in leads:
    clean_num = phone.replace(" ", "")
    if clean_num.startswith("0"):
        clean_num = clean_num[1:]
    
    formatted_phone = f" +971 {clean_num}"
    
    new_rows.append({
        'Source File': 'Custom Added',
        'Type': 'Buyer',
        'Country': 'UAE',
        'Commodity': commodities,
        'Company Name': name,
        'Phone': formatted_phone,
        'Original_Phone': phone
    })

new_df = pd.DataFrame(new_rows)

print(f"Reading existing file: {file_path}")
try:
    df = pd.read_excel(file_path)
    combined_df = pd.concat([df, new_df], ignore_index=True)

    print(f"Saving {len(combined_df)} total records...")
    combined_df.to_excel(file_path, index=False)
    print(f"Successfully added {len(new_df)} new UAE spices leads with full commodities!")
except Exception as e:
    print(f"Error: {e}")
