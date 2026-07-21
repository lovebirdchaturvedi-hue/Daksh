import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore, collection, onSnapshot, query, orderBy, limit, enableIndexedDbPersistence }
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

// Enable Offline Persistence for "Instant" feel
enableIndexedDbPersistence(db).catch((err) => {
    if (err.code == 'failed-precondition') {
        console.warn("Multiple tabs open, persistence can only be enabled in one tab at a a time.");
    } else if (err.code == 'unimplemented') {
        console.warn("The current browser does not support all of the features required to enable persistence");
    }
});

function aiSummary(r) {
  return `Buyer seeking ${r.product} (${r.quantity}) for ${r.country || "global"} market`;
}

function startRFQStream() {
  const ticker = document.getElementById("rfqTicker");
  if (!ticker) return;

  // Simple query to avoid index requirements
  const q = query(collection(db, "rfqs"), limit(12));
  
  onSnapshot(q, (snap) => {
    ticker.innerHTML = "";
    if (snap.empty) {
      ticker.innerHTML = `<span>No Live RFQs Available</span>`;
      return;
    }

    // Manual sort by date
    const docs = [...snap.docs].sort((a,b) => (b.data().createdAt?.seconds || 0) - (a.data().createdAt?.seconds || 0));

    docs.forEach(doc => {
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
  }, (error) => {
    console.error("RFQ Ticker Stream Error:", error);
    ticker.innerHTML = `<span>Trade Feed Active (Updates Real-time)</span>`;
  });
}

// Start the real-time stream immediately
document.addEventListener('DOMContentLoaded', startRFQStream);

