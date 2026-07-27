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

async function upload() {
    console.log("Reading extracted_leads.json...");
    const data = JSON.parse(fs.readFileSync('extracted_leads.json', 'utf-8'));
    
    console.log(`Found ${data.length} leads. Beginning upload...`);
    
    let successCount = 0;
    let errorCount = 0;
    
    // We will do chunks of 50 to avoid rate limits / hanging
    const chunkSize = 50;
    for (let i = 0; i < data.length; i += chunkSize) {
        const chunk = data.slice(i, i + chunkSize);
        
        await Promise.all(chunk.map(async (lead) => {
            try {
                lead.createdAt = serverTimestamp();
                await addDoc(collection(db, "suppliers"), lead);
                successCount++;
            } catch (err) {
                console.error("Error adding lead:", err.message);
                errorCount++;
            }
        }));
        
        console.log(`Progress: ${Math.min(i + chunkSize, data.length)} / ${data.length} | Success: ${successCount} | Errors: ${errorCount}`);
        
        // Small delay between chunks
        await new Promise(r => setTimeout(r, 1000));
    }
    
    console.log("Upload Complete!");
    console.log(`Successfully added: ${successCount}`);
    console.log(`Failed: ${errorCount}`);
    process.exit(0);
}

upload().catch(console.error);
