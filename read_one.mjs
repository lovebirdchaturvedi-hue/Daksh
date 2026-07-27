import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs, query, limit } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function readOne() {
    try {
        console.log("Fetching one doc...");
        const q = query(collection(db, "suppliers"), limit(1));
        const snapshot = await getDocs(q);
        console.log("Success! Found:", snapshot.docs.length);
    } catch(e) {
        console.error("Error:", e);
    }
    process.exit();
}
readOne();
