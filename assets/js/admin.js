import { auth } from "./firebase-init.js";
import {
  collection,
  getDocs,
  doc,
  updateDoc
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { db } from "./firebase-init.js";
import {
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const table = document.getElementById("supplierTable");

// Hide page until verified
document.body.style.display = "none";

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  // 🔐 CHECK ADMIN CLAIM (ONLY SOURCE OF TRUTH)
  const token = await user.getIdTokenResult(true);

  console.log("ADMIN CLAIM CHECK:", token.claims);

  if (token.claims.role !== "admin") {
    alert("Unauthorized access");
    await signOut(auth);
    window.location.href = "/";
    return;
  }

  // ✅ ADMIN VERIFIED
  document.body.style.display = "block";
  loadSuppliers();
});

// 📦 LOAD SUPPLIERS
async function loadSuppliers() {
  table.innerHTML = "";
  const snap = await getDocs(collection(db, "suppliers"));

  snap.forEach(docSnap => {
    const s = docSnap.data();

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${s.companyName || "-"}</td>
      <td>${s.email}</td>
      <td>${s.status || "pending"}</td>
      <td>${s.plan || "free"}</td>
      <td>
        <td>
  <button onclick="approve('${docSnap.id}')">Approve</button>
  <button onclick="setPlan('${docSnap.id}','gold')">Gold</button>
  <button onclick="setPlan('${docSnap.id}','platinum')">Platinum</button>
  <button onclick="setPlan('${docSnap.id}','free')">Free</button>
  <button onclick="banSupplier('${docSnap.id}')">Ban</button>
  <button onclick="unbanSupplier('${docSnap.id}')">Unban</button>
</td>
>
      </td>
    `;
    table.appendChild(row);
  });
}

// ACTIONS
window.approve = id =>
  updateDoc(doc(db, "suppliers", id), { status: "approved" }).then(loadSuppliers);

window.suspend = id =>
  updateDoc(doc(db, "suppliers", id), { status: "suspended", plan: "free" }).then(loadSuppliers);

window.setPlan = (id, plan) =>
  updateDoc(doc(db, "suppliers", id), { plan }).then(loadSuppliers);

window.logout = async () => {
  await signOut(auth);
  window.location.href = "/supplier-login.html";
};

