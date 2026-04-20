import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore, collection, getDocs, query, orderBy, limit }
  from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod",
  storageBucket: "apd-globaltrade-prod.firebasestorage.app",
  messagingSenderId: "226407312435",
  appId: "1:226407312435:web:f8a54b1132af3899170746"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

function aiSummary(r) {
  return `Buyer seeking ${r.product} (${r.quantity}) for ${r.country || "global"} market`;
}

async function loadRFQs() {
  const ticker = document.getElementById("rfqTicker");
  if (!ticker) return;

  try {
    const q = query(collection(db, "rfqs"), orderBy("createdAt", "desc"), limit(12));
    const snap = await getDocs(q);
    ticker.innerHTML = "";
    if (snap.empty) {
      ticker.innerHTML = `<span>No Live RFQs Available</span>`;
      return;
    }
    snap.forEach(doc => {
      const r = doc.data();
      const country = r.destination || r.country || "Global";
      const code = (r.countryCode || "").toLowerCase();
      const flag = code
        ? `<img src="https://flagcdn.com/16x12/${code}.png" style="vertical-align:middle;margin-right:6px">`
        : "🌍";
      
      const item = document.createElement('span');
      item.style.display = 'flex';
      item.style.alignItems = 'center';
      item.style.gap = '8px';
      item.style.cursor = 'pointer';
      item.onclick = () => location.href='/membership.html';
      item.innerHTML = `
        ${flag} ${aiSummary({ ...r, country })}
        <span style="background: rgba(34, 197, 94, 0.1); color: #4ade80; font-size: 10px; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(74, 222, 128, 0.2); font-weight: 800; text-transform: uppercase;">✅ Verified Lead</span>
      `;
      ticker.appendChild(item);
    });
  } catch (error) {
    ticker.innerHTML = `<span>Error loading live trade feed</span>`;
    console.error(error);
  }
}

// Initial load
document.addEventListener('DOMContentLoaded', loadRFQs);
// Refresh every 5 minutes
setInterval(loadRFQs, 300000);
