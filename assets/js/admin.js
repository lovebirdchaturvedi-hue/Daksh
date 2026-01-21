import { auth } from "./firebase-init.js";
import { db } from "./firebase-init.js";

import {
  collection,
  getDocs,
  doc,
  updateDoc
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

import {
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const table = document.getElementById("supplierTable");

// 🔒 Hide page until admin verified
document.body.style.display = "none";

/* ===============================
   AUTH + ADMIN CHECK
================================ */
onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  const token = await user.getIdTokenResult(true);
  console.log("ADMIN CLAIMS:", token.claims);

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

/* ===============================
   LOAD SUPPLIERS
================================ */
async function loadSuppliers() {
  table.innerHTML = "";

  const snap = await getDocs(collection(db, "suppliers"));

  snap.forEach((docSnap) => {
    const s = docSnap.data();

    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${s.companyName || "-"}</td>
      <td>${s.email || "-"}</td>
      <td>${s.status || "pending"}</td>
      <td>${s.plan || "free"}</td>
      <td>
        <button onclick="approve('${docSnap.id}')">Approve</button>
        <button onclick="setPlan('${docSnap.id}','gold')">Gold</button>
        <button onclick="setPlan('${docSnap.id}','platinum')">Platinum</button>
        <button onclick="setPlan('${docSnap.id}','free')">Free</button>
        <button onclick="banSupplier('${docSnap.id}')">Ban</button>
        <button onclick="unbanSupplier('${docSnap.id}')">Unban</button>
      </td>
    `;

    table.appendChild(row);
  });
}

/* ===============================
   ACTIONS
================================ */

// ✅ APPROVE
window.approve = async (id) => {
  await updateDoc(doc(db, "suppliers", id), {
    status: "approved"
  });
  loadSuppliers();
};

// 🎖️ SET PLAN
window.setPlan = async (id, plan) => {
  await updateDoc(doc(db, "suppliers", id), {
    plan: plan
  });
  loadSuppliers();
};

// 🚫 BAN
window.banSupplier = async (id) => {
  if (!confirm("Ban this supplier?")) return;

  await updateDoc(doc(db, "suppliers", id), {
    status: "banned",
    plan: "free"
  });

  alert("Supplier banned");
  loadSuppliers();
};

// ♻️ UNBAN
window.unbanSupplier = async (id) => {
  if (!confirm("Unban this supplier?")) return;

  await updateDoc(doc(db, "suppliers", id), {
    status: "approved"
  });

  alert("Supplier unbanned");
  loadSuppliers();
};

// 🚪 LOGOUT
window.logout = async () => {
  await signOut(auth);
  window.location.href = "/supplier-login.html";
};
