import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs, updateDoc, doc } from "firebase/firestore";

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

async function cleanRFQs() {
    console.log("Fetching RFQs...");
    const rfqsCol = collection(db, "rfqs");
    const snapshot = await getDocs(rfqsCol);
    let updatedCount = 0;
    
    for (const d of snapshot.docs) {
        const data = d.data();
        let phone = data.whatsapp || "";
        
        // Remove spaces, hyphens, parentheses
        phone = phone.replace(/[\s\-\(\)]/g, "");
        
        // If it starts with '00', convert to '+'
        if (phone.startsWith("00")) {
            phone = "+" + phone.substring(2);
        }
        
        // If it doesn't start with '+', it might be missing a country code
        if (phone && !phone.startsWith("+")) {
            const dest = (data.destination || "").toLowerCase();
            const origin = (data.origin || "").toLowerCase();
            const fullText = dest + " " + origin;
            
            let code = "";
            if (fullText.includes("uae") || fullText.includes("dubai") || fullText.includes("jebel ali")) code = "+971";
            else if (fullText.includes("saudi") || fullText.includes("ksa")) code = "+966";
            else if (fullText.includes("usa") || fullText.includes("america")) code = "+1";
            else if (fullText.includes("india")) code = "+91";
            else if (fullText.includes("uk ") || fullText.includes("london")) code = "+44";
            
            if (code) {
                // Remove leading zero if present (e.g. 0557701191 -> +971557701191)
                if (phone.startsWith("0")) phone = phone.substring(1);
                
                phone = code + phone;
                console.log(`Updating ${d.id}: changed to ${phone} (matched ${code})`);
                await updateDoc(doc(db, "rfqs", d.id), { whatsapp: phone });
                updatedCount++;
            } else {
                console.log(`Skipping ${d.id}: no country matched for ${phone}. Text: ${data.destination} / ${data.origin}`);
            }
        }
    }
    console.log(`Finished updating ${updatedCount} RFQs.`);
    process.exit(0);
}

cleanRFQs().catch(console.error);
