import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import {
  getAuth,
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import {
  getFirestore,
  collection,
  getDocs,
  doc,
  updateDoc,
  deleteDoc,
  query,
  limit
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const ADMIN_EMAIL = "admin@apdglobaltrade.com";

// Firebase init
const app = initializeApp({
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod",
  storageBucket: "apd-globaltrade-prod.firebasestorage.app",
  messagingSenderId: "226407312435",
  appId: "1:226407312435:web:f8a54b1132af3899170746"
});

const auth = getAuth(app);
const db = getFirestore(app);
const tbody = document.getElementById("tbody");

// Auth guard
let authGuardTimeout = setTimeout(() => {
  if (document.getElementById("tbody").innerHTML.includes("Loading")) {
      document.getElementById("tbody").innerHTML = `<tr><td colspan="12" >AUTH HANGING: Firebase auth is taking a while to respond. Please check your connection or refresh.</td></tr>`;
  }
}, 12000);

onAuthStateChanged(auth, async (user) => {
  clearTimeout(authGuardTimeout);
  if (!user) {
    location.href = "/supplier-login.html";
    return;
  }

  if (user.email !== ADMIN_EMAIL) {
    alert("Admins only");
    location.href = "/supplier-dashboard.html";
    return;
  }

  loadSuppliers();
});

// Load suppliers
window.loadSuppliers = loadSuppliers;
async function loadSuppliers() {
  tbody.innerHTML = "<tr><td colspan='13'>Loading suppliers…</td></tr>";

  try {
    const q = query(collection(db, "suppliers"), limit(3000));
    const snap = await Promise.race([
        getDocs(q),
        new Promise((_, reject) => setTimeout(() => reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 8000))
    ]);

    if (snap.empty) {
      tbody.innerHTML = "<tr><td colspan='13'>No suppliers found</td></tr>";
      return;
    }

    let htmlOutput = "";

    snap.forEach(d => {
      const s = d.data();
      
      const hideBulk = document.getElementById('hideBulkToggle')?.checked;
      if (hideBulk && (s.isBulkLead || d.id.startsWith("bulk_"))) return;
      
      const planMap = {
        'custom_credits': 'Custom Credits',
        '1_lead_pass': '1 Free Lead',
        '7_day_pass': '7-Day Power Pass',
        '3_day_trial': '3-Day Premium Trial',
        'trial_3m': '3-Mo Premium Trial',
        'pro_6m': '6-Mo Elite Professional',
        'elite_12m': '12-Mo Institutional Elite',
        'lifetime': 'Lifetime Access (Buyer)',
        'free': 'Free',
        'basic': 'Basic',
        'premium': '3-Mo Premium Trial',
        'platinum': '6-Mo Elite Professional',
        'gold': '3-Mo Premium Trial'
      };
      const planName = planMap[s.plan] || s.plan || "basic";
      const unlockTotal = (s.plan === 'custom_credits') ? (s.totalCredits || 0) : ((s.plan === '1_lead_pass') ? '1' : ((s.plan === '3_day_trial') ? '3' : ((s.plan === '7_day_pass') ? '7' : '∞')));
      
      const isLegacy = d.id.length < 20; // Minimal heuristic for manual IDs
      const warning = isLegacy ? '<span title="Manual/Legacy ID. May not sync with user login." style="cursor:help;">⚠️</span>' : '';

      htmlOutput += `
        <tr>
          <td>${s.companyName || "-"}</td>
          <td>${s.role === 'buyer' ? '<span style="color:#9333ea; font-weight:800; font-size:11px;">BUYER</span>' : '<span style="color:#16a34a; font-weight:800; font-size:11px;">SUPPLIER</span>'}</td>
          <td>${s.email || "-"}</td>
          <td>${(s.productsString || s.product) ? (s.productsString || s.product) : "-"}</td>
          <td>${(s.targetMarket && Array.isArray(s.targetMarket)) ? s.targetMarket.join(', ') : (s.targetMarket || "-")}</td>
          <td style="max-width: 150px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${s.comment || ""}">${s.comment || "-"}</td>
          <td>${s.phone || s.contact || s.whatsapp || "-"}</td>
          <td style="font-size:10px; font-family:monospace; color:#64748b;">${warning} ${d.id}</td>
          <td><b>${s.status || "pending"}</b></td>
          <td style="font-size:12px;">${planName}</td>
          <td><span style="color:#c9a44a; font-weight:800;">${s.unlocksUsed || 0}</span> / ${unlockTotal}</td>
          <td style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 320px;">
            <button class="approve" onclick="upd('${d.id}',{status:'approved'})">Approve</button>
            <button class="pass" style="background:#22c55e; color:#fff;" onclick="upd('${d.id}',{plan:'custom_credits', status:'approved', totalCredits:1, unlocksUsed:0, unlockedLeads:[]})">+1 Credit</button>
            <button class="pass" style="background:#22c55e; color:#fff;" onclick="upd('${d.id}',{plan:'custom_credits', status:'approved', totalCredits:3, unlocksUsed:0, unlockedLeads:[]})">+3 Credits</button>
            <button class="pass" style="background:#22c55e; color:#fff;" onclick="upd('${d.id}',{plan:'custom_credits', status:'approved', totalCredits:5, unlocksUsed:0, unlockedLeads:[]})">+5 Credits</button>
            <button class="pass" style="background:#22c55e; color:#fff;" onclick="upd('${d.id}',{plan:'custom_credits', status:'approved', totalCredits:8, unlocksUsed:0, unlockedLeads:[]})">+8 Credits</button>
            <button class="pass" onclick="upd('${d.id}',{plan:'3_day_trial', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Assign 3-Day Trial</button>
            <button class="gold" onclick="upd('${d.id}',{plan:'trial_3m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Professional Pass</button>
            <button class="platinum" onclick="upd('${d.id}',{plan:'pro_6m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Institutional Elite</button>
            <button class="premium" onclick="upd('${d.id}',{plan:'elite_12m', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Global Enterprise</button>
            <button class="premium" style="background:linear-gradient(135deg, #d97706, #fbbf24);" onclick="upd('${d.id}',{plan:'nexus', status:'approved', unlocksUsed:0, unlockedLeads:[]})">APD Global Trade Nexus™ 4999 USD Plan</button>
            <button class="lifetime" onclick="upd('${d.id}',{plan:'buyer_1yr', status:'approved', role:'buyer'})">1 Years Buyer Membership</button>
            <button class="free" onclick="upd('${d.id}',{plan:'free'})">Free</button>
            <button class="ban" onclick="upd('${d.id}',{status:'banned'})">Ban</button>
            ${isLegacy ? `<button class="ban" style="background:#000" onclick="del('${d.id}')">Delete</button>` : ''}
          </td>
        </tr>`;
    });

    tbody.innerHTML = htmlOutput || "<tr><td colspan='13'>No suppliers match the filter</td></tr>";
    filterSuppliersTable();

  } catch (err) {
    console.error("Error loading suppliers:", err);
    tbody.innerHTML = `<tr><td colspan='13' >Error loading suppliers: ${err.message}</td></tr>`;
  }
}

// REAL-TIME SEARCH FILTER FOR ADMIN PANEL
window.filterSuppliersTable = filterSuppliersTable;
window.clearAdminSearch = clearAdminSearch;

function filterSuppliersTable() {
  const query = (document.getElementById("adminSearchInput")?.value || "").toLowerCase().trim();
  const rows = tbody.querySelectorAll("tr");
  let visibleCount = 0;
  let totalCount = 0;

  rows.forEach(row => {
    if (row.cells.length <= 1) return; // Skip loading/error messages
    totalCount++;
    const text = row.innerText.toLowerCase();
    if (!query || text.includes(query)) {
      row.style.display = "";
      visibleCount++;
    } else {
      row.style.display = "none";
    }
  });

  const badge = document.getElementById("supplierCountBadge");
  if (badge) {
    if (query) {
      badge.innerHTML = `Found <b style="color:#16a34a">${visibleCount}</b> of ${totalCount} suppliers`;
    } else {
      badge.innerHTML = `Total Suppliers: <b>${totalCount}</b>`;
    }
  }
}

function clearAdminSearch() {
  const input = document.getElementById("adminSearchInput");
  if (input) input.value = "";
  filterSuppliersTable();
}

// Update supplier
window.upd = async (id, data) => {
  await updateDoc(doc(db, "suppliers", id), data);
  loadSuppliers();
};

window.del = async (id) => {
  if (confirm("Are you sure you want to delete this LEGACY record? This will NOT delete the user account.")) {
    await deleteDoc(doc(db, "suppliers", id));
    loadSuppliers();
  }
};

// Logout
document.getElementById("logoutBtn").onclick = async () => {
  await signOut(auth);
  location.href = "/supplier-login.html";
};