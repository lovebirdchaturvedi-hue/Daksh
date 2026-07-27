import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs, query, where, deleteDoc } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function deleteBulk() {
    console.log("Fetching bulk leads to delete...");
    const q = query(collection(db, "suppliers"), where("source", "==", "july_bulk_upload"));
    const snap = await getDocs(q);
    
    console.log(`Found ${snap.size} leads. Deleting...`);
    let count = 0;
    
    const docs = snap.docs;
    // Delete in chunks
    for (let i = 0; i < docs.length; i += 50) {
        const chunk = docs.slice(i, i + 50);
        await Promise.all(chunk.map(d => deleteDoc(d.ref)));
        count += chunk.length;
        console.log(`Deleted ${count} / ${snap.size}`);
    }
    
    console.log("Deletion complete!");
    process.exit(0);
}

deleteBulk().catch(console.error);
