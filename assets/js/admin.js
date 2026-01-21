import { auth, db } from "./firebase-init.js";
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

const ADMIN_EMAIL = "admin@apdglobaltrade.com";
const table = document.getElementById("supplierTable");

// 🔒 Protect admin page
onAuthStateChanged(auth, async (user) => {
  if (!user || user.email !== ADMIN_EMAIL) {
    alert("Unauthorized access");
    await signOut(auth);
    window.location.href = "/supplier-login.html";
    return;
  }

  document.body.style.display = "block";
  loadSuppliers();
});

// 📦 Load suppliers
async function loadSuppliers() {
  table.innerHTML = "";
  const snap = await getDocs(collection(db, "suppliers"));

  snap.forEach(docSnap => {
    const s = docSnap.data();

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${s.companyName || "-"}</td>
      <td>${s.email || "-"}</td>
      <td>${s.status || "pending"}</td>
      <td>${s.plan || "free"}</td>
      <td>
        <button class="approve" onclick="approve('${docSnap.id}')">Approve</button>
        <button class="gold" onclick="setPlan('${docSnap.id}','gold')">Gold</button>
        <button class="platinum" onclick="setPlan('${docSnap.id}','platinum')">Platinum</button>
        <button class="free" onclick="setPlan('${docSnap.id}','free')">Free</button>
        <button class="ban" onclick="banSupplier('${docSnap.id}')">Ban</button>
        <button class="unban" onclick="unbanSupplier('${docSnap.id}')">Unban</button>
      </td>
    `;
    table.appendChild(row);
  });
}

// ✅ Actions
window.approve = async (id) => {
  await updateDoc(doc(db, "suppliers", id), { status: "approved" });
  loadSuppliers();
};

window.setPlan = async (id, plan) => {
  await updateDoc(doc(db, "suppliers", id), { plan });
  loadSuppliers();
};

window.banSupplier = async (id) => {
  await updateDoc(doc(db, "suppliers", id), { status: "banned" });
  loadSuppliers();
};

window.unbanSupplier = async (id) => {
  await updateDoc(doc(db, "suppliers", id), { status: "approved" });
  loadSuppliers();
};

// 🚪 Logout
window.logout = async () => {
  await signOut(auth);
  window.location.href = "/supplier-login.html";
};
