import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs } from "firebase/firestore";
import fs from "fs";

const firebaseConfig = {
    apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
    authDomain: "apd-globaltrade-prod.firebaseapp.com",
    projectId: "apd-globaltrade-prod",
    storageBucket: "apd-globaltrade-prod.firebasestorage.app",
    messagingSenderId: "226407312435",
    appId: "1:226407312435:web:f8a54b1132af3899170746"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function fetchRFQs() {
    const rfqsCol = collection(db, "rfqs");
    const snapshot = await getDocs(rfqsCol);
    const rfqs = [];
    snapshot.forEach(doc => {
        rfqs.push({ id: doc.id, ...doc.data() });
    });
    fs.writeFileSync("C:/Users/DELL/.gemini/antigravity/brain/04a4cabb-5e34-4e91-9255-a6d9256e8085/scratch/rfqs.json", JSON.stringify(rfqs, null, 2));
    console.log("RFQs exported to scratch folder.");
}

fetchRFQs().catch(console.error);
