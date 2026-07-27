import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc, serverTimestamp } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const commodities = [
  "CM Husk Powder", "CM Husk Powder (Premium)", "Refined Palm Oil", "Crude Palm Oil", 
  "Refined Sunflower Oil", "Organic Moringa Powder", "Moringa Leaf Powder", 
  "Red Chilli Powder", "Kashmiri Chilli Powder", "Organic Fresh Ginger", "Dry Ginger (Saunth)", 
  "Turmeric Powder (High Curcumin)", "Black Pepper (500 GL)", "Green Cardamom (8mm)", 
  "Cumin Seeds (Singapore Quality)", "Cow Dung Cakes (Fuel)", "Organic Cow Dung Compost", 
  "Red Lentils (Masoor Dal)", "Chickpeas (Kabuli)", "Pigeon Peas (Toor Dal)", 
  "1121 Basmati Rice", "Sella Basmati Rice", "ICUMSA 45 White Sugar", "Soya Bean Meal", 
  "Milling Wheat", "Yellow Maize (Animal Feed)"
];

const destinations = [
  "Dubai, UAE", "Jebel Ali, UAE", "Rotterdam, Netherlands", "Hamburg, Germany", 
  "London Gateway, UK", "New York, USA", "Los Angeles, USA", "Miami, USA", 
  "Singapore", "Sydney, Australia", "Cape Town, South Africa", "Santos, Brazil", 
  "Jeddah, Saudi Arabia", "Port Klang, Malaysia", "Ho Chi Minh, Vietnam", "Durban, South Africa",
  "Colombo, Sri Lanka", "Chittagong, Bangladesh", "Mombasa, Kenya", "Aqaba, Jordan"
];

const quantities = [
  "50 MT", "100 MT", "500 MT", "1,000 MT", "2,500 MT", "5,000 MT", "10,000 MT",
  "2 FCL (20ft)", "5 FCL (40ft)", "10 FCL (40ft)", "20 FCL", "25 MT", "200 MT"
];

const companies = [
  "Al-Futtaim Trading", "Global Agro LLC", "Euro Spice Co", "Apex Imports", 
  "Crescent General Trading", "Moringa Health USA", "B2B Organic Supplies", 
  "Green Earth Fertilizers", "Golden State Oil Co", "Gulf Food Imports", 
  "Nile Trade Partners", "Eastern Spice Route", "Oasis Trading Hub", 
  "Pacific Rim Imports", "EuroFoods GMBH", "AusAgri Logistics", "Saudi Star Enterprises"
];

const names = ["Ahmed M.", "John S.", "Fatima R.", "Carlos M.", "David P.", "Sarah W.", "Omar K.", "Ling C.", "Wei Y.", "Sanjay D.", "Michael B.", "Emma T."];

function randomChoice(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

async function seedDatabase() {
  console.log("Starting DB Seed for 150 RFQs...");
  const rfqsRef = collection(db, "rfqs");
  
  let promises = [];
  
  for(let i = 0; i < 150; i++) {
    const product = randomChoice(commodities);
    const dest = randomChoice(destinations);
    const qty = randomChoice(quantities);
    const company = randomChoice(companies);
    const buyer = randomChoice(names);
    
    // Slight jitter to make the timestamps look natural
    // We will set them all as recent, within the last 48 hours
    const jitter = Math.floor(Math.random() * (48 * 60 * 60 * 1000));
    const simulatedDate = new Date(Date.now() - jitter);
    
    // Hack for node.js to pass serverTimestamp equivalent or Date objects
    
    const docData = {
      buyerName: buyer,
      buyerCompany: company,
      email: `${buyer.split(" ")[0].toLowerCase()}@${company.split(" ")[0].toLowerCase()}.com`,
      phone: `+${Math.floor(Math.random() * 90) + 10} ${Math.floor(Math.random() * 900000000) + 100000000}`,
      country: dest.split(", ").pop(),
      product: product,
      quantity: qty,
      deliveryPort: dest,
      destination: dest,
      description: `We are looking for immediate supply of ${qty} of ${product} delivered to ${dest}. Please quote CIF/FOB.`,
      status: "open",
      source: "website",
      createdAt: simulatedDate // raw JS Date object translates cleanly to Firestore Timestamp in Node SDK
    };
    
    promises.push(addDoc(rfqsRef, docData));
    
    if (promises.length >= 25) {
      await Promise.all(promises);
      console.log(`Inserted 25...`);
      promises = [];
    }
  }
  
  if (promises.length > 0) {
    await Promise.all(promises);
  }
  
  console.log("Finished seeding 150 RFQs!");
  process.exit(0);
}

seedDatabase();
