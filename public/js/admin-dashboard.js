import { auth, db } from "./firebase-init.js";
import { onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { collection, getDocs, doc, updateDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const statusEl = document.getElementById("status");
const listEl = document.getElementById("supplierList");
const logoutBtn = document.getElementById("logoutBtn");

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    statusEl.innerText = "Please login as admin.";
    return;
  }

  if (user.email !== "admin@apdglobaltrade.com") {
    statusEl.innerText = "Access denied.";
    return;
  }

  statusEl.innerText = "Loading suppliers…";
  logoutBtn.style.display = "inline-block";

  loadSuppliers();
});

async function loadSuppliers() {
  listEl.innerHTML = "";

  try {
    const snap = await getDocs(collection(db, "suppliers"));

    if (snap.empty) {
      listEl.innerHTML = "<p>No suppliers found.</p>";
      return;
    }

    snap.forEach((docSnap) => {
      const s = docSnap.data();
      const id = docSnap.id;

      const div = document.createElement("div");
      div.style.border = "1px solid #ccc";
      div.style.padding = "10px";
      div.style.marginBottom = "10px";

      div.innerHTML = `
        <strong>${s.companyName || "Supplier"}</strong><br>
        Status: ${s.status || "pending"}<br><br>
        <button data-id="${id}" data-action="approved">Approve</button>
        <button data-id="${id}" data-action="rejected">Reject</button>
      `;

      listEl.appendChild(div);
    });

  } catch (err) {
    statusEl.innerText = "Firestore error";
    alert(err.message);
  }
}

document.addEventListener("click", async (e) => {
  const id = e.target.dataset.id;
  const action = e.target.dataset.action;
  if (!id || !action) return;

  await updateDoc(doc(db, "suppliers", id), { status: action });
  loadSuppliers();
});

logoutBtn.addEventListener("click", async () => {
  await signOut(auth);
  statusEl.innerText = "Logged out.";
  listEl.innerHTML = "";
});
