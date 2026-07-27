import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc, getDocs, deleteDoc, doc, serverTimestamp } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const fakeNames = ["Mohammed Al-Fayed", "James Smith", "Li Wei", "Fatima Zahra", "John Doe", "Sarah Connor", "Ahmed Hassan", "Chen Wu", "David Miller", "Elena Rossi", "Omar Al-Khatib", "Lucas Silva", "Isabella Fernandez", "Rajesh Kumar", "Anna Muller"];
const fakeDomains = ["gmail.com", "import-trading.com", "global-sourcing.ae", "eu-foods.net", "supply-chain.co.uk", "agri-ventures.com"];
function generateContactInfo(name) {
  const emailName = name.toLowerCase().replace(/ /g, ".");
  const domain = fakeDomains[Math.floor(Math.random() * fakeDomains.length)];
  const phone = "+" + Math.floor(Math.random() * 90 + 10) + " " + Math.floor(Math.random() * 9000000000 + 1000000000);
  return { email: `${emailName}@${domain}`, phone: phone };
}

const PRODUCTS = ["Basmati Rice 1121", "Sugar ICUMSA 45", "Red Chilli Powder", "Turmeric Powder", "Soybean Meal", "Maize Corn", "Palm Oil", "Sunflower Oil", "Wheat Flour", "Cashew Nuts", "Atlantic Potatoes (PepsiCo Grade)", "Industrial Sugar S-30", "Extrusion Corn (Maize)", "Refined Sunflower Oil (Bulk)", "Potato Flakes"];
const WORLDWIDE_PEPSICO_BUYERS = [
  { name: "PepsiCo Global Procurement (USA)", email: "procurement@pepsico.com", phone: "+1 914-253-2000", product: "Industrial Sugar S-30", qty: "50,000 MT", port: "New York", size: 12500000 },
  { name: "PepsiCo Mexico (Sabritas)", email: "compras@sabritas.com.mx", phone: "+52 55-5201-1400", product: "Atlantic Potatoes (PepsiCo Grade)", qty: "20,000 MT", port: "Veracruz", size: 5500000 },
  { name: "PepsiCo UK (Walkers)", email: "supply@walkers.co.uk", phone: "+44 116-234-2000", product: "Potato Flakes", qty: "5,000 MT", port: "Liverpool", size: 1200000 },
  { name: "Varun Beverages Nepal (Pepsi Bottler)", email: "import@varunbeverages.com.np", phone: "+977 1-424-3456", product: "Industrial Sugar S-30", qty: "1,000 MT", port: "Birgunj", size: 850000 },
  { name: "CG Corp Global (Wai Wai/Kwik's)", email: "procurement@cgcorpglobal.com", phone: "+977 1-552-2256", product: "Atlantic Potatoes (PepsiCo Grade)", qty: "500 MT", port: "Biratnagar", size: 450000 },
  { name: "PepsiCo India (Gurgaon Hub)", email: "sourcing.india@pepsico.com", phone: "+91 124-469-6969", product: "Extrusion Corn (Maize)", qty: "10,000 MT", port: "Kandla", size: 2800000 },
  { name: "Yashoda Foods (Current)", email: "purchase@yashodafoods.com", phone: "+977 71-520-222", product: "Refined Sunflower Oil (Bulk)", qty: "200 MT", port: "Bhairahawa", size: 320000 }
];
const COUNTRIES = ["UAE","USA","Indonesia","Vietnam","Bangladesh","Saudi Arabia","Egypt","Nigeria","Brazil","Philippines","Nepal"];

const MORINGA_MAKHANA_BUYERS = [
  { name: "Organica Superfoods LLC", email: "john.davis@organicasuperfoods.com", phone: "+1 415-555-0198", product: "Organic Moringa Powder", qty: "25 MT", port: "Los Angeles, USA", size: 125000 },
  { name: "Holland & Barrett Procurement", email: "procurement.eu@hollandbarrett.com", phone: "+44 20-7946-0921", product: "Moringa Leaf Powder", qty: "50 MT", port: "London, UK", size: 240000 },
  { name: "Green Origins Trading", email: "sourcing@greenorigins.de", phone: "+49 30-1928-3746", product: "Organic Moringa Powder", qty: "10 MT", port: "Hamburg, Germany", size: 55000 },
  { name: "Nature's Way Inc", email: "vendor.management@naturesway.com", phone: "+1 801-555-0234", product: "Moringa Extract Powder", qty: "100 MT", port: "New York, USA", size: 600000 },
  { name: "Zenith Snack Brands", email: "import@zenithsnacks.ca", phone: "+1 416-555-0891", product: "Raw Fox Nuts (Makhana)", qty: "40 MT", port: "Toronto, Canada", size: 320000 },
  { name: "Emirates Vegan Foods", email: "purchasing@emiratesvegan.ae", phone: "+971 4-223-9981", product: "Roasted Makhana (Bulk)", qty: "20 MT", port: "Jebel Ali, UAE", size: 180000 },
  { name: "Lotus Bites UK", email: "supply@lotusbites.co.uk", phone: "+44 161-496-0391", product: "Raw Fox Nuts (Makhana) - Size 5+", qty: "60 MT", port: "Felixstowe, UK", size: 480000 },
  { name: "Aussie Health Co.", email: "imports@aussiehealth.com.au", phone: "+61 2-9876-5432", product: "Organic Moringa Powder", qty: "15 MT", port: "Sydney, Australia", size: 75000 },
  { name: "SpiceJet Imports LLC", email: "trade@spicejetusa.com", phone: "+1 312-555-0762", product: "Raw Fox Nuts (Makhana)", qty: "100 MT", port: "Chicago, USA", size: 850000 },
  { name: "NutriLife Supplements", email: "buyer@nutrilife.sg", phone: "+65 6789-0123", product: "Moringa Powder", qty: "30 MT", port: "Singapore", size: 145000 }
];

const COW_DUNG_BUYERS = [
  { name: "Al Barakah Agro Fertilizers", email: "procurement@albarakah-agro.ae", phone: "+971 4-332-9011", product: "Dry Cow Dung (Organic Fertilizer)", qty: "1,500 MT", port: "Jebel Ali, UAE", size: 45000 },
  { name: "Dubai Green Energy Co.", email: "biomass@dubaienergy.ae", phone: "+971 50-888-2345", product: "Cow Dung Briquettes", qty: "500 MT", port: "Dubai, UAE", size: 25000 },
  { name: "EcoFarms Middle East", email: "sourcing@ecofarms.me", phone: "+974 44-55-2233", product: "Organic Cow Dung Compost", qty: "2,000 MT", port: "Doha, Qatar", size: 60000 },
  { name: "Oman Agricultural Resources", email: "import@omanagro.om", phone: "+968 24-555-123", product: "Dry Cow Dung (Organic Fertilizer)", qty: "800 MT", port: "Sohar, Oman", size: 30000 },
  { name: "Saudi Organic Cultivation Ltd", email: "purchase@saudiorganic.sa", phone: "+966 11-456-7890", product: "Cow Dung Compost", qty: "3,000 MT", port: "Jeddah, Saudi Arabia", size: 85000 },
  { name: "Global BioMass Trading", email: "trade@biomasstrading.uk", phone: "+44 20-3333-4444", product: "Cow Dung Briquettes", qty: "1,000 MT", port: "Rotterdam, Netherlands", size: 40000 }
];

async function run() {
  console.log("Deleting old RFQs...");
  const querySnapshot = await getDocs(collection(db, "rfqs"));
  const deletePromises = [];
  querySnapshot.forEach((document) => {
    deletePromises.push(deleteDoc(doc(db, "rfqs", document.id)));
  });
  await Promise.all(deletePromises);
  console.log(`Deleted ${deletePromises.length} old RFQs.`);

  let rfqs = [];

  // General RFQs
  for (let i = 0; i < 100; i++) {
    const fakeName = fakeNames[Math.floor(Math.random() * fakeNames.length)] + " " + Math.floor(Math.random()*1000);
    const generatedContact = generateContactInfo(fakeName);
    rfqs.push({
      product: PRODUCTS[Math.floor(Math.random() * PRODUCTS.length)],
      quantity: `${Math.floor(Math.random() * 900 + 100)} MT`,
      deliveryPort: COUNTRIES[Math.floor(Math.random() * COUNTRIES.length)],
      dealSizeUSD: Math.floor(Math.random() * 4000000 + 500000),
      status: "open",
      source: "admin-seed",
      buyerName: fakeName,
      email: generatedContact.email,
      contact: generatedContact.phone
    });
  }

  // PepsiCo
  WORLDWIDE_PEPSICO_BUYERS.forEach(b => {
    rfqs.push({
      product: b.product,
      quantity: b.qty,
      deliveryPort: b.port,
      dealSizeUSD: b.size,
      status: "open",
      source: "admin-seed",
      buyerName: b.name,
      email: b.email,
      contact: b.phone
    });
  });

  // Moringa / Makhana (500)
  const moringaBuyers = MORINGA_MAKHANA_BUYERS.filter(b => b.product.includes("Moringa"));
  const makhanaBuyers = MORINGA_MAKHANA_BUYERS.filter(b => b.product.includes("Makhana"));

  for (let i = 0; i < 250; i++) {
    const baseBuyer = moringaBuyers[Math.floor(Math.random() * moringaBuyers.length)];
    const multiplier = 1 + (Math.random() * 0.5);
    const newSize = Math.floor(baseBuyer.size * multiplier);
    const baseQtyNum = parseInt(baseBuyer.qty);
    const newQty = Math.floor(baseQtyNum * multiplier) + " MT";
    rfqs.push({ product: baseBuyer.product, quantity: newQty, deliveryPort: baseBuyer.port, dealSizeUSD: newSize, status: "open", source: "admin-seed", buyerName: baseBuyer.name, email: baseBuyer.email, contact: baseBuyer.phone });
  }

  for (let i = 0; i < 250; i++) {
    const baseBuyer = makhanaBuyers[Math.floor(Math.random() * makhanaBuyers.length)];
    const multiplier = 1 + (Math.random() * 0.5);
    const newSize = Math.floor(baseBuyer.size * multiplier);
    const baseQtyNum = parseInt(baseBuyer.qty);
    const newQty = Math.floor(baseQtyNum * multiplier) + " MT";
    rfqs.push({ product: baseBuyer.product, quantity: newQty, deliveryPort: baseBuyer.port, dealSizeUSD: newSize, status: "open", source: "admin-seed", buyerName: baseBuyer.name, email: baseBuyer.email, contact: baseBuyer.phone });
  }

  // Cow Dung (200)
  for (let i = 0; i < 200; i++) {
    const baseBuyer = COW_DUNG_BUYERS[Math.floor(Math.random() * COW_DUNG_BUYERS.length)];
    const multiplier = 1 + (Math.random() * 0.4);
    const newSize = Math.floor(baseBuyer.size * multiplier);
    const baseQtyNum = parseInt(baseBuyer.qty.replace(/,/g, ''));
    const newQty = Math.floor(baseQtyNum * multiplier).toLocaleString() + " MT";
    rfqs.push({ product: baseBuyer.product, quantity: newQty, deliveryPort: baseBuyer.port, dealSizeUSD: newSize, status: "open", source: "admin-seed", buyerName: baseBuyer.name, email: baseBuyer.email, contact: baseBuyer.phone });
  }

  console.log(`Uploading ${rfqs.length} new RFQs...`);
  
  // Chunking the uploads so we don't hit rate limits or memory issues
  const chunkSize = 50;
  for (let i = 0; i < rfqs.length; i += chunkSize) {
      const chunk = rfqs.slice(i, i + chunkSize);
      const promises = chunk.map(r => addDoc(collection(db, "rfqs"), {
          ...r,
          createdAt: serverTimestamp()
      }));
      await Promise.all(promises);
      console.log(`Uploaded batch ${i/chunkSize + 1}`);
  }

  console.log("Done!");
}

run().catch(console.error);
