import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, collection, getDocs, doc, setDoc, updateDoc, addDoc, deleteDoc, serverTimestamp, query, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyABA-KRY6bY7K2QZwLhQ2piHjQVLLceiGs",
  authDomain: "apd-globaltrade-prod.firebaseapp.com",
  projectId: "apd-globaltrade-prod",
  storageBucket: "apd-globaltrade-prod.firebasestorage.app",
  messagingSenderId: "226407312435",
  appId: "1:226407312435:web:f8a54b1132af3899170746"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

const ADMIN_EMAIL = "admin@apdglobaltrade.com";

// DOM Elements
const authOverlay = document.getElementById('authOverlay');
const authStatus = document.getElementById('authStatus');
const crmList = document.getElementById('crmList');
const broadcastStatus = document.getElementById('broadcastStatus');
const totalSuppliersEl = document.getElementById('totalSuppliers');
const premiumMembersEl = document.getElementById('premiumMembers');

let allSuppliers = [];

// 🔒 AUTHENTICATION LOGIC
onAuthStateChanged(auth, (user) => {
    if (user && user.email.toLowerCase() === ADMIN_EMAIL.toLowerCase()) {
        authOverlay.style.display = 'none';
        loadData();
    } else {
        authOverlay.style.display = 'flex';
    }
});

window.addEventListener('auth-attempt', async (e) => {
    const { email, pass } = e.detail;
    authStatus.innerText = "Authenticating...";
    try {
        await signInWithEmailAndPassword(auth, email, pass);
    } catch (err) {
        authStatus.innerText = "Invalid Admin Credentials.";
    }
});

window.addEventListener('auth-logout', async () => {
    await signOut(auth);
});

// 📊 PANEL SWITCHING
window.showPanel = (panelId) => {
    document.querySelectorAll('.panel').forEach(p => p.style.display = 'none');
    document.querySelectorAll('.sidebar-item').forEach(i => i.classList.remove('active'));
    
    // Highlight sidebar
    const items = document.querySelectorAll('.sidebar-item');
    for(let i=0; i<items.length; i++){
       if(items[i].getAttribute('onclick').includes(panelId)){
           items[i].classList.add('active');
       }
    }
    
    if (panelId === 'overview') {
        document.getElementById('overviewPanel').style.display = 'block';
        document.getElementById('broadcastPanel').style.display = 'block';
        document.getElementById('databasePanel').style.display = 'block';
    } else {
        const p = document.getElementById(panelId + 'Panel');
        if(p) p.style.display = 'block';
    }

    if (panelId === 'rfqs') {
        loadRfqs();
    }
};

// 📊 DATA LOADING
async function loadData() {
    crmList.innerHTML = '<div style="padding: 40px; text-align: center; color: #8b949e;">Fetching Institutional Data...</div>';
    
    try {
        const q = query(collection(db, "suppliers"), limit(1000));
        const snap = await Promise.race([
            getDocs(q),
            new Promise((_, reject) => setTimeout(() => reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 7000))
        ]);
        allSuppliers = [];
        let premiumCount = 0;

        snap.forEach(d => {
            const data = d.data();
            data.id = d.id;
            allSuppliers.push(data);
            if (data.plan && data.plan !== 'free' && data.plan !== 'basic') {
                premiumCount++;
            }
        });

        totalSuppliersEl.innerText = allSuppliers.length;
        premiumMembersEl.innerText = premiumCount;

        renderSuppliers(allSuppliers);
    } catch (err) {
        console.error(err);
        crmList.innerText = "Critical Error: Could not connect to Data Node.";
    }
}

function renderSuppliers(suppliers) {
    crmList.innerHTML = '';
    suppliers.sort((a, b) => (b.createdAt?.seconds || 0) - (a.createdAt?.seconds || 0));

    suppliers.forEach(s => {
        const row = document.createElement('div');
        row.className = 'user-row';
        
        const statusBadge = s.status === 'approved' ? 'badge-verified' : 'badge-pending';
        const planName = s.plan || 'Free';
        const phoneNumber = s.contact || s.phone || s.whatsapp || 'No Number';
        
        const lastContacted = s.lastContactedAt ? new Date(s.lastContactedAt.seconds * 1000).toLocaleDateString() : 'Never';
        const contactedColor = s.lastContactedAt ? '#22c55e' : '#64748b';

        let catDisplay = 'All Access';
        if (s.allowedCategories && !s.allowedCategories.includes('all')) {
            catDisplay = s.allowedCategories.map(c => c.toUpperCase()).join(', ');
        }

        row.innerHTML = `
            <div style="display: flex; align-items: center; gap: 12px;">
                <div class="g-avatar">${(s.companyName || 'U')[0]}</div>
                <div>
                    <div class="g-name">${s.companyName || 'Unknown Entity'}</div>
                    <div class="g-date">${s.email || 'bulk-lead@apd'}</div>
                </div>
            </div>
            <div><span class="badge ${statusBadge}">${s.status || 'Pending'}</span></div>
            <div>
                <div style="color: var(--crm-gold); font-weight: 800; font-size: 11px; text-transform: uppercase;">${planName}</div>
                <div style="color: #94a3b8; font-size: 9px; margin-top: 4px; font-weight: 600;">[ ${catDisplay} ]</div>
            </div>
            <div style="color: ${contactedColor}; font-size: 12px; font-weight: 700;">${lastContacted}</div>
            <div>
                <button class="btn-action btn-verify" onclick="verifyUser('${s.id}')">VERIFY</button>
                <button class="btn-action btn-wa" onclick="openChat('${phoneNumber}')">CHAT</button>
            </div>
        `;
        crmList.appendChild(row);
    });
}

// 🛡️ ACTIONS
window.verifyUser = async (id) => {
    if (confirm("Promote this entity to VERIFIED STATUS?")) {
        const categoriesInput = prompt("ENTER ALLOWED PRODUCT CATEGORIES (comma separated, e.g., 'Rice, Spices').\nLeave blank for 'All Access':");
        
        if (categoriesInput === null) return; // Admin cancelled
        
        let allowedArray = ['All'];
        if (categoriesInput.trim() !== '') {
            allowedArray = categoriesInput.split(',').map(c => c.trim().toLowerCase());
        }

        await updateDoc(doc(db, "suppliers", id), { 
            status: 'approved',
            allowedCategories: allowedArray
        });
        loadData();
    }
};

window.openChat = (phone) => {
    if (!phone || phone === 'No Number') return alert("No contact number recorded.");
    const cleanPhone = phone.replace(/\D/g, '');
    window.open(`https://wa.me/${cleanPhone}`, '_blank');
};

// 📢 BROADCAST ENGINE (ENTERPRISE PROXY VERSION)
window.saveApiSettings = () => {
    const inst = document.getElementById('apiInstance').value;
    const tok = document.getElementById('apiToken').value;
    if(inst) localStorage.setItem('apdcrm_instance', inst);
    if(tok) localStorage.setItem('apdcrm_token', tok);
    alert("API Credentials Saved!");
};

window.sendBroadcast = async () => {
    const msg = document.getElementById('broadcastMsg').value;
    const batchSize = parseInt(document.getElementById('batchSize').value) || 500;
    const audience = document.getElementById('targetAudience').value;

    const ULTRAMSG_INSTANCE = localStorage.getItem('apdcrm_instance') || "instance168990";
    const ULTRAMSG_TOKEN = localStorage.getItem('apdcrm_token') || "yx9xaxy5k1nbqjat";

    if (!msg) return alert("Please type an institutional message.");
    
    let targetLeads = allSuppliers.filter(s => s.contact || s.phone || s.whatsapp);
    if (audience === 'unsent') {
        targetLeads = targetLeads.filter(l => !l.lastContactedAt);
    }

    const dispatchList = targetLeads.slice(0, batchSize);
    if (dispatchList.length === 0) return alert("No pending leads found.");
    
    if (!confirm(`🚀 ENTERPRISE DISPATCH: Sending ${dispatchList.length} messages via Backend Proxy. Proceed?`)) return;

    document.querySelector('.btn-wa').disabled = true;
    
    for (let i = 0; i < dispatchList.length; i++) {
        const s = dispatchList[i];
        const rawPhone = s.contact || s.phone || s.whatsapp;
        const cleanPhone = rawPhone.replace(/\D/g, '');
        
        let finalPhone = cleanPhone;
        if (cleanPhone.length === 10) {
            finalPhone = '91' + cleanPhone;
        }

        broadcastStatus.innerText = `Dispatching: ${i + 1}/${dispatchList.length} (${s.companyName})`;
        
        try {
            // Using Vercel Backend Proxy!
            const response = await fetch('/api/send', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    instance: ULTRAMSG_INSTANCE,
                    token: ULTRAMSG_TOKEN,
                    to: `+${finalPhone}`,
                    body: msg
                })
            });

            const result = await response.json();

            if (response.ok && !result.error) {
                // NON-BLOCKING DB UPDATE
                updateDoc(doc(db, "suppliers", s.id), {
                    lastContactedAt: serverTimestamp(),
                    messageCount: (s.messageCount || 0) + 1
                }).catch(e => console.log("DB update skipped (Quota), but sent."));
                
                broadcastStatus.innerText = `✅ Sent: ${i + 1}/${dispatchList.length} (${s.companyName}) - Waiting randomly...`;
            } else {
                console.error(`API rejected ${s.companyName}`, result);
                broadcastStatus.innerText = `❌ Failed: ${s.companyName}`;
            }
            
        } catch (err) { 
            console.error(`Network Error for ${s.companyName}:`, err); 
        }

        // ADVANCED HUMAN EMULATION: Random delay between 15s and 35s
        const randomDelay = Math.floor(Math.random() * (35000 - 15000 + 1) + 15000);
        await new Promise(resolve => setTimeout(resolve, randomDelay));
    }
    
    alert(`✅ CAMPAIGN COMPLETE: ${dispatchList.length} leads processed.`);
    loadData();
    document.querySelector('.btn-wa').disabled = false;
};

// 📥 BULK INGESTION LOGIC
window.startBulkIngestion = async () => {
    const data = document.getElementById('bulkPasteArea').value;
    if (!data) return alert("Please paste lead data.");
    const lines = data.split('\n').filter(l => l.trim() !== '');
    if (!confirm(`Import ${lines.length} leads?`)) return;

    const ingestionStatus = document.getElementById('ingestionStatus');
    ingestionStatus.innerText = `Ingesting...`;
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const parts = line.split(',');
        const company = parts[0]?.trim();
        const contact = parts[1]?.trim();
        if (!company || !contact) continue;

        const leadId = "bulk_" + contact.replace(/\D/g, '');
        try {
            await setDoc(doc(db, "suppliers", leadId), {
                companyName: company,
                contact: contact,
                status: "approved",
                plan: "free",
                isBulkLead: true,
                createdAt: serverTimestamp()
            }, { merge: true });
        } catch (err) { console.error(err); }
        if (i % 20 === 0) {
            ingestionStatus.innerText = `Ingesting: ${i + 1} / ${lines.length}`;
            await new Promise(r => setTimeout(r, 100));
        }
    }
    alert("✅ SUCCESS: Bulk Ingestion Complete.");
    loadData();
};

window.onload = () => {
    const savedInst = localStorage.getItem('apdcrm_instance');
    const savedTok = localStorage.getItem('apdcrm_token');
    if(savedInst && document.getElementById('apiInstance')) document.getElementById('apiInstance').value = savedInst;
    if(savedTok && document.getElementById('apiToken')) document.getElementById('apiToken').value = savedTok;
};


// 🛍️ RFQ MANAGEMENT
let allRfqs = [];

window.loadRfqs = async () => {
    const rfqListEl = document.getElementById('rfqAdminList');
    rfqListEl.innerHTML = '<div style="padding: 40px; text-align: center; color: #8b949e;">Fetching Active RFQs...</div>';
    
    try {
        const q = query(collection(db, "rfqs"), orderBy("createdAt", "desc"), limit(200));
        const snap = await getDocs(q);
        allRfqs = [];
        
        snap.forEach(d => {
            const data = d.data();
            data.id = d.id;
            allRfqs.push(data);
        });
        
        renderRfqs(allRfqs);
    } catch (err) {
        console.error("Error loading RFQs:", err);
        rfqListEl.innerHTML = '<div style="padding: 40px; text-align: center; color: #ef4444;">Error loading RFQs.</div>';
    }
};

function renderRfqs(rfqs) {
    const rfqListEl = document.getElementById('rfqAdminList');
    rfqListEl.innerHTML = '';
    
    if(rfqs.length === 0) {
        rfqListEl.innerHTML = '<div style="padding: 40px; text-align: center; color: #8b949e;">No active RFQs found.</div>';
        return;
    }
    
    rfqs.forEach(r => {
        const row = document.createElement('div');
        row.className = 'user-row';
        row.style.gridTemplateColumns = '2fr 1fr 1fr 1fr 1fr';
        
        const isSynth = r.isSynthetic ? '<span class="badge" style="background: rgba(234, 179, 8, 0.1); color: #eab308; border: 1px solid #eab308;">SYNTHETIC</span>' : '<span class="badge badge-verified">REAL LEAD</span>';
        
        row.innerHTML = `
            <div>
                <div style="font-weight:bold; color:var(--crm-gold);">${r.buyerName || r.company || 'Unknown Buyer'}</div>
                <div style="font-size:11px; color:#8b949e;">${r.product || r.commodity || 'Unknown Product'}</div>
            </div>
            <div style="font-size:13px; font-weight:600;">${r.quantity || r.qty || 'TBD'}</div>
            <div style="font-size:12px; color:#8b949e;">${r.destination || 'Global'}</div>
            <div>${isSynth}</div>
            <div>
                <button onclick="deleteRfq('${r.id}')" class="btn-action" style="background:rgba(239, 68, 68, 0.1); color:#ef4444; border:1px solid #ef4444;">DELETE</button>
            </div>
        `;
        rfqListEl.appendChild(row);
    });
}

window.deleteRfq = async (id) => {
    if(!confirm("Are you sure you want to delete this RFQ?")) return;
    try {
        await deleteDoc(doc(db, "rfqs", id));
        loadRfqs();
    } catch(e) {
        console.error(e);
        alert("Error deleting RFQ.");
    }
};

window.injectManualRfq = async () => {
    const company = document.getElementById('rfqCompany').value;
    const phone = document.getElementById('rfqPhone').value;
    const product = document.getElementById('rfqProduct').value;
    const qty = document.getElementById('rfqQty').value;
    const dest = document.getElementById('rfqDest').value;
    const isSynthetic = document.getElementById('rfqIsSynthetic').value === "true";
    
    if(!company || !phone || !product) {
        alert("Company, Phone, and Product are required!");
        return;
    }
    
    const statusEl = document.getElementById('rfqInjectStatus');
    statusEl.innerText = "Injecting RFQ into Global Network...";
    
    try {
        await addDoc(collection(db, "rfqs"), {
            buyerName: company,
            company: company,
            phone: phone,
            whatsapp: phone,
            product: product,
            commodity: product,
            quantity: qty,
            qty: qty,
            destination: dest,
            isSynthetic: isSynthetic,
            status: "active",
            createdAt: serverTimestamp()
        });
        
        statusEl.innerText = "✅ RFQ Pushed Successfully!";
        
        // Clear inputs
        document.getElementById('rfqCompany').value = '';
        document.getElementById('rfqPhone').value = '';
        document.getElementById('rfqProduct').value = '';
        document.getElementById('rfqQty').value = '';
        document.getElementById('rfqDest').value = '';
        
        setTimeout(() => statusEl.innerText = '', 3000);
        loadRfqs();
        
    } catch (e) {
        console.error("Error injecting RFQ:", e);
        statusEl.innerText = "❌ Error pushing RFQ.";
        statusEl.style.color = "#ef4444";
    }
};
