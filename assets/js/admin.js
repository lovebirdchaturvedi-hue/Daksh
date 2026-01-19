import { auth, db } from "./firebase-init.js";
import {
  collection,
  getDocs,
  doc,
  updateDoc
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const table = document.getElementById("supplierTable");

// 🔒 Hide page until auth check completes
document.body.style.display = "none";

auth.onAuthStateChanged(async (user) => {
  // ❌ Not logged in → redirect
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  // 🔐 Only allow ADMIN email
  if (user.email !== "admin@apdglobaltrade.com") {
    alert("Unauthorized access");
    await auth.signOut();
    window.location.href = "/login.html";
    return;
  }

  // ✅ Admin verified → show page
  document.body.style.display = "block";

  loadSuppliers();
});

async function loadSuppliers() {
  const snapshot = await getDocs(collection(db, "suppliers"));
  table.innerHTML = "";

  snapshot.forEach(docSnap => {
    const s = docSnap.data();

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${s.companyName || "-"}</td>
      <td>${s.email}</td>
      <td>${s.status}</td>
      <td>${s.plan || "free"}</td>
      <td>
        <button class="approve" onclick="approve('${docSnap.id}')">Approve</button>
        <button class="suspend" onclick="suspend('${docSnap.id}')">Suspend</button>
        <button class="gold" onclick="setPlan('${docSnap.id}','gold')">Gold</button>
        <button class="platinum" onclick="setPlan('${docSnap.id}','platinum')">Platinum</button>
        <button class="free" onclick="setPlan('${docSnap.id}','free')">Free</button>
      </td>
    `;
    table.appendChild(row);
  });
}

window.approve = async (id) => {
  await updateDoc(doc(db, "suppliers", id), {
    status: "approved"
  });
  loadSuppliers();
};

window.suspend = async (id) => {
  await updateDoc(doc(db, "suppliers", id), {
    status: "suspended",
    plan: "free"
  });
  loadSuppliers();
};

window.setPlan = async (id, plan) => {
  await updateDoc(doc(db, "suppliers", id), {
    plan
  });
  loadSuppliers();
};

