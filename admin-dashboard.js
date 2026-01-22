import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, collection, getDocs, doc, updateDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

const statusEl = document.getElementById("status");
const listEl = document.getElementById("supplierList");

/* 🔐 HARD ADMIN LOCK */
onAuthStateChanged(auth, async (user) => {
  if (!user) {
    statusEl.innerText = "Please login first.";
    return;
  }

  if (user.email !== "admin@apdglobaltrade.com") {
    statusEl.innerText = "Access denied.";
    await signOut(auth);
    return;
  }

  statusEl.innerText = "Loading suppliers…";
  loadSuppliers();
});
