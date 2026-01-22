import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, collection, getDocs, doc, updateDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

/* 🔐 Firebase config */
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

/* 🚫 NO REDIRECTS. NO RELOADS. */
onAuthStateChanged(auth, async (user) => {
  if (!user) {
    statusEl.innerText = "Please login as admin.";
    return;
  }

  /* SIMPLE ADMIN CHECK (SAFE) */
  if (user.email !== "admin@apdglobaltrade.com") {
    statusEl.innerText = "Access denied.";
    return;
  }

  statusEl.innerText = "Loading suppliers…";

  const snap = await getDocs(collection(db, "suppliers"));
  listEl.innerHTML = "";

  snap.forEach((docSnap) => {
    const s = docSnap.data();
    const li = document.createElement("li");

    li.innerHTML = `
      <strong>${s.companyName || "Supplier"}</strong>
      <button data-id="${docSnap.id}" data-action="approve">Approve</button>
      <button data-id="${docSnap.id}" data-action="ban">Ban</button>
    `;

    listEl.appendChild(li);
  });

  statusEl.innerText = `Suppliers loaded: ${snap.size}`;
});

/* 🔘 Button actions */
document.addEventListener("click", async (e) => {
  if (!e.target.dataset.id) return;

  const ref = doc(db, "suppliers", e.target.dataset.id);

  if (e.target.dataset.action === "approve") {
    await updateDoc(ref, { approved: true });
    alert("Approved");
  }

  if (e.target.dataset.action === "ban") {
    await updateDoc(ref, { banned: true });
    alert("Banned");
  }
});
