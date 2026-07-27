const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

const correctScript = `
<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, collection, getDocs, doc, updateDoc, deleteDoc, query, limit } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

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

// On-screen error logger
window.onerror = function(msg, url, lineNo, columnNo, error) {
  document.getElementById("tbody").innerHTML = \`<tr><td colspan="8" style="color:red; font-weight:bold;">CRASH: \${msg} <br>Line: \${lineNo}</td></tr>\`;
  return false;
};
window.onunhandledrejection = function(event) {
  document.getElementById("tbody").innerHTML = \`<tr><td colspan="8" style="color:red; font-weight:bold;">PROMISE CRASH: \${event.reason}</td></tr>\`;
};

// Auth guard
setTimeout(() => {
  if (document.getElementById("tbody").innerHTML.includes("Loading")) {
      document.getElementById("tbody").innerHTML = \`<tr><td colspan="8" style="color:red; font-weight:bold;">AUTH HANGING: Firebase auth is completely frozen and not responding.</td></tr>\`;
  }
}, 3000);

onAuthStateChanged(auth, async (user) => {
  if (!user) {
    location.href = "/supplier-login.html";
    return;
  }

  if (!user.email || user.email.toLowerCase() !== ADMIN_EMAIL.toLowerCase()) {
    alert("Admins only");
    location.href = "/supplier-dashboard.html";
    return;
  }

  loadSuppliers();
});

// Load suppliers
async function loadSuppliers() {
  const tbody = document.getElementById("tbody");
  tbody.innerHTML = "<tr><td colspan='8'>Loading suppliers…</td></tr>";

  try {
    const q = query(collection(db, "suppliers"), limit(500));
    const snap = await Promise.race([
        getDocs(q),
        new Promise((_, reject) => setTimeout(() => reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 2000))
    ]);
    tbody.innerHTML = "";

    if (snap.empty) {
      tbody.innerHTML = "<tr><td colspan='8'>No suppliers found</td></tr>";
      return;
    }

    snap.forEach(d => {
      const s = d.data();
      
      const planMap = {
        'trial_3m': '3-Mo Premium Trial',
        'pro_6m': '6-Mo Elite Professional',
        'elite_12m': '12-Mo Elite Lifetime',
        '7_day_pass': '7-Day Power Pass',
        'free': 'Free Basic Plan',
        'premium': '12-Mo Elite Lifetime',
        'platinum': '6-Mo Elite Professional',
        'gold': '3-Mo Premium Trial'
      };
      const planName = planMap[s.plan] || s.plan || "basic";
      const unlockTotal = (s.plan === '7_day_pass') ? '7' : '∞';
      
      const isLegacy = d.id.length < 20; // Minimal heuristic for manual IDs
      const warning = isLegacy ? '<span title="Manual/Legacy ID. May not sync with user login." style="cursor:help;">⚠️</span>' : '';

      tbody.innerHTML += \`
        <tr>
          <td>\${s.companyName || "-"}</td>
          <td>\${s.email || "-"}</td>
          <td>\${s.phone || "-"}</td>
          <td style="font-size:10px; font-family:monospace; color:#64748b;">\${warning} \${d.id}</td>
          <td><b>\${s.status || "pending"}</b></td>
          <td style="font-size:12px;">\${planName}</td>
          <td><span style="color:#c9a44a; font-weight:800;">\${s.unlocksUsed || 0}</span> / \${unlockTotal}</td>
          <td>
            <button class="approve" onclick="upd('\${d.id}',{status:'approved'})">Approve</button>
            <button class="pass" onclick="upd('\${d.id}',{plan:'7_day_pass', status:'approved', unlocksUsed:0, unlockedLeads:[]})">Assign 7-Day Pass</button>
            <button class="gold" onclick="upd('\${d.id}',{plan:'trial_3m', status:'approved'})">Set 3-Mo Trial</button>
            <button class="platinum" onclick="upd('\${d.id}',{plan:'pro_6m', status:'approved'})">Set 6-Mo Elite</button>
            <button class="premium" onclick="upd('\${d.id}',{plan:'elite_12m', status:'approved'})">Set 12-Mo Elite</button>
            <button class="free" onclick="upd('\${d.id}',{plan:'free'})">Free</button>
            <button class="ban" onclick="upd('\${d.id}',{status:'banned'})">Ban</button>
            \${isLegacy ? \`<button class="ban" style="background:#000" onclick="del('\${d.id}')">Delete</button>\` : ''}
          </td>
        </tr>\`;
    });

  } catch (err) {
    console.error("Error loading suppliers:", err);
    tbody.innerHTML = "<tr><td colspan='8'>Error loading suppliers</td></tr>";
  }
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
</script>`;

content = content.replace(/<script type="module">[\s\S]*?<\/script>/, correctScript);
fs.writeFileSync(file, content);
console.log('Script completely rewritten perfectly.');
