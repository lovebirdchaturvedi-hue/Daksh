import { auth, db } from "./firebase-init.js";
import { onAuthStateChanged } from
  "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import {
  doc, getDoc,
  collection, getDocs,
  query, where, orderBy
} from
  "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const statusEl = document.getElementById("supplierStatus");
const planEl = document.getElementById("supplierPlan");
const rfqGrid = document.getElementById("rfqGrid");

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    window.location.href = "/supplier-login.html";
    return;
  }

  // Fetch supplier profile
  const supplierSnap = await getDoc(doc(db, "suppliers", user.uid));

  if (!supplierSnap.exists()) {
    statusEl.textContent = "Pending Approval";
    planEl.textContent = "Not Assigned";
    return;
  }

  const supplier = supplierSnap.data();
  statusEl.textContent = supplier.status;
  planEl.textContent = supplier.plan || "basic";

  // Fetch RFQs
  const q = query(
    collection(db, "rfqs"),
    where("status", "==", "active"),
    orderBy("createdAt", "desc")
  );

  const rfqs = await getDocs(q);
  rfqGrid.innerHTML = "";

  rfqs.forEach(docSnap => {
    const r = docSnap.data();

    let contactHTML = `<div class="lock">🔒 Upgrade to view buyer contact</div>`;

    if (
      supplier.status === "approved" &&
      (supplier.plan === "gold" || supplier.plan === "platinum")
    ) {
      contactHTML = `
        <div class="contact">
          📧 ${r.email}<br>
          📞 ${r.phone}
        </div>
      `;
    }

    rfqGrid.innerHTML += `
      <div class="rfq-card">
        <h4>${r.product}</h4>
        <p>${r.quantity} · ${r.country}</p>
        ${contactHTML}
      </div>
    `;
  });
});
