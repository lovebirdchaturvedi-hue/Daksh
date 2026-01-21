import { auth, db } from "./firebase-init.js";
import {
  collection,
  getDocs,
  doc,
  updateDoc
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import {
  sendPasswordResetEmail,
  signOut,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const table = document.getElementById("supplierTable");

// 🔒 Hide page until admin verified
document.body.style.display = "none";

/* 🔐 ADMIN AUTH GUARD (CUSTOM CLAIMS) */
onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  // Force refresh token to get latest claims
  const token = await user.getIdTokenResult(true);

  // ✅ ADMIN CHECK
  if (!token.claims.admin) {
    alert("Unauthorized access");
    await signOut(auth);
    window.location.href = "/supplier-login.html";
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

  if (snapshot.empty) {
    table.innerHTML = `<tr><td colspan="5">No suppliers found</td></tr>`;
    return;
  }

  snapshot.forEach((docSnap) => {
    const s = docSnap.data();

    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${s.companyName || "-"}</td>
      <td>${s.email || "-"}</td>
      <td>
        <span class="badge ${s.status || "pending"}">
          ${s.status || "pending"}
        </span>
      </td>
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
