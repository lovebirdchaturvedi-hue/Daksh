// admin-dashboard.js
// Works with Firebase v10 (MODULAR SDK ONLY)

import {
  auth,
  db,
  onAuthStateChanged,
  collection,
  getDocs,
  doc,
  updateDoc
} from "./firebase-init.js";

/* -------------------------------
   AUTH GUARD (ADMIN ONLY)
-------------------------------- */
onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  try {
    // Force refresh token to get latest claims
    const token = await user.getIdTokenResult(true);

    console.log("ADMIN CLAIMS:", token.claims);

    if (token.claims.role !== "admin") {
      alert("Access denied: Admins only");
      await auth.signOut();
      window.location.href = "/supplier-login.html";
      return;
    }

    // ✅ ADMIN VERIFIED
    loadSuppliers();

  } catch (err) {
    console.error("Auth error:", err);
    alert("Authentication error");
  }
});

/* -------------------------------
   LOAD SUPPLIERS
-------------------------------- */
async function loadSuppliers() {
  const tableBody = document.getElementById("suppliersTableBody");

  if (!tableBody) {
    console.error("suppliersTableBody not found in HTML");
    return;
  }

  tableBody.innerHTML = "";

  try {
    const snapshot = await getDocs(collection(db, "suppliers"));

    snapshot.forEach((docSnap) => {
      const data = docSnap.data();
      const supplierId = docSnap.id;

      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${data.companyName || "-"}</td>
        <td>${data.email || "-"}</td>
        <td>${data.status || "pending"}</td>
        <td>
          <button data-id="${supplierId}" data-action="approve">Approve</button>
          <button data-id="${supplierId}" data-action="ban">Ban</button>
        </td>
      `;

      tableBody.appendChild(tr);
    });

    attachActionHandlers();

  } catch (err) {
    console.error("Error loading suppliers:", err);
    alert("Missing or insufficient permissions");
  }
}

/* -------------------------------
   APPROVE / BAN HANDLERS
-------------------------------- */
function attachActionHandlers() {
  document.querySelectorAll("button[data-action]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const supplierId = btn.dataset.id;
      const action = btn.dataset.action;

      try {
        if (action === "approve") {
          await updateSupplierStatus(supplierId, "approved");
        }

        if (action === "ban") {
          await updateSupplierStatus(supplierId, "banned");
        }

        loadSuppliers();

      } catch (err) {
        console.error("Update error:", err);
        alert("Action failed");
      }
    });
  });
}

/* -------------------------------
   UPDATE SUPPLIER STATUS
-------------------------------- */
async function updateSupplierStatus(supplierId, status) {
  const ref = doc(db, "suppliers", supplierId);

  await updateDoc(ref, {
    status: status,
    updatedAt: new Date()
  });
}
