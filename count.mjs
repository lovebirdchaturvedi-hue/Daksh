import { initializeApp } from "firebase/app";
import { getFirestore, collection, getCountFromServer } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function count() {
    try {
        console.log("Fetching count...");
        const snapshot = await getCountFromServer(collection(db, "suppliers"));
        console.log("Total suppliers:", snapshot.data().count);
    } catch(e) {
        console.error(e);
    }
    process.exit();
}
count();
