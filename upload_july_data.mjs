import { initializeApp } from "firebase/app";
import { getFirestore, collection, addDoc, serverTimestamp } from "firebase/firestore";
import fs from 'fs';

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function uploadData(filename, collectionName, isRfq) {
    console.log(`Starting upload for ${filename} to collection ${collectionName}...`);
    const fileContent = fs.readFileSync(filename, 'utf-8');
    const lines = fileContent.split('\n').filter(line => line.trim() !== '');
    
    // Skip header
    const dataLines = lines.slice(1);
    
    let docs = [];
    for (const line of dataLines) {
        const parts = line.split(',');
        if (parts.length < 7) continue;
        
        const companyName = parts[0];
        const contactName = parts[1];
        const email = parts[2];
        const phone = parts[3];
        const commodity = parts[4];
        const country = parts[5];
        const quantity = parts[6];
        
        if (isRfq) {
            docs.push({
                product: commodity,
                quantity: quantity,
                deliveryPort: country,
                dealSizeUSD: Math.floor(Math.random() * 4000000 + 500000),
                status: "open",
                source: "bulk_seed_july_2026",
                buyerName: `${contactName} (${companyName})`,
                email: email,
                contact: phone,
                createdAt: serverTimestamp()
            });
        } else {
            docs.push({
                companyName: companyName,
                contactName: contactName,
                email: email,
                phone: phone,
                primaryProduct: commodity,
                country: country,
                status: "active",
                source: "bulk_seed_july_2026",
                createdAt: serverTimestamp()
            });
        }
    }
    
    console.log(`Parsed ${docs.length} records. Uploading in batches of 50...`);
    const chunkSize = 50;
    for (let i = 0; i < docs.length; i += chunkSize) {
        const chunk = docs.slice(i, i + chunkSize);
        const promises = chunk.map(docData => addDoc(collection(db, collectionName), docData));
        await Promise.all(promises);
        console.log(`Uploaded batch ${Math.floor(i/chunkSize) + 1} of ${Math.ceil(docs.length/chunkSize)}`);
    }
    
    console.log(`Successfully completed upload for ${filename}!`);
}

async function run() {
    await uploadData('July_2026_Importers.csv', 'rfqs', true);
    await uploadData('July_2026_Exporters.csv', 'suppliers', false);
    console.log("All data seeded successfully.");
    process.exit(0);
}

run().catch(console.error);
