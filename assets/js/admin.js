import { auth, db } from "./firebase-init.js";
import {
  collection,
  getDocs,
  doc,
  updateDoc,
  getDoc
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import {
  sendPasswordResetEmail,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const table = document.getElementById("supplierTable");

// 🔒 Hide page until auth check completes
document.body.style.display = "none";

auth.onAuthStateChanged(async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  // 🔐 Check admin role via Firestore
  const adminRef = doc(db, "admins", user.uid);
  const adminSnap = await getDoc(adminRef);

  if (!adminSnap.exists()) {
    alert("Unauthorized access");
    await signOut(auth);
    window.location.href = "/";
    return;
  }

  // ✅ Admin verified
  document.body.style.display = "block";
  loadSuppliers();
});

/* 📦 LOAD SUPPLIERS */
async function loadSuppliers() {
  const snapshot = await getDocs(collection(db, "suppliers"));
  table.innerHTML = "";

  snapshot.forEach(docSnap => {
    const s = docSnap.data();

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${s.companyName || "-"}</td>
      <td>${s.email}</td>
      <td>${s.status || "pending"}</td>
      <td>${s.plan || "free"}</td>
      <td>
        <button class="approve" onclick="approve('${docSnap.id}')">Approve</button>
        <button class="suspend" onclick="suspend('${docSnap.id}')">Suspend</button>
        <button class="gold" onclick="setPlan('${docSnap.id}','gold')">Gold</button>
        <button class="platinum" onclick="setPlan('${docSnap.id}','platinum')">Platinum</button>
        <button class="free" onclick="setPlan('${docSnap.id}','free')">Free</button>
        <button class="reset" onclick="resetPwd('${s.email}')">Reset Password</button>
      </td>
    `;
    table.appendChild(row);
  });
}

/* ✅ ACTIONS */
window.approve = async (id) => {
  await updateDoc(doc(db, "suppliers", id), { status: "approved" });
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
  await updateDoc(doc(db, "suppliers", id), { plan });
  loadSuppliers();
};

/* 🔑 RESET SUPPLIER PASSWORD */
window.resetPwd = async (email) => {
  if (!confirm(`Send password reset email to ${email}?`)) return;
  await sendPasswordResetEmail(auth, email);
  alert("Password reset email sent.");
};

/* 🚪 LOGOUT */
window.logout = async () => {
  await signOut(auth);
  window.location.href = "/supplier-login.html";
};
