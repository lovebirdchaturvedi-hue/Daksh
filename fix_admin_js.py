with open("assets/js/admin-crm.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update showPanel to handle 'rfqs' correctly
old_show_panel = """window.showPanel = (panelId) => {
    document.querySelectorAll('.panel').forEach(p => p.style.display = 'none');
    document.querySelectorAll('.sidebar-item').forEach(i => i.classList.remove('active'));
    
    if (panelId === 'overview') {
        document.getElementById('overviewPanel').style.display = 'block';
        document.getElementById('broadcastPanel').style.display = 'block';
        document.getElementById('databasePanel').style.display = 'block';
    } else {
        const p = document.getElementById(panelId + 'Panel');
        if(p) p.style.display = 'block';
    }
};"""

new_show_panel = """window.showPanel = (panelId) => {
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
};"""

content = content.replace(old_show_panel, new_show_panel)

# 2. Add addDoc to imports if not there. It is not there, let's just add it.
old_import = """import { getFirestore, collection, getDocs, doc, setDoc, updateDoc, deleteDoc, serverTimestamp, query, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";"""
new_import = """import { getFirestore, collection, getDocs, doc, setDoc, updateDoc, addDoc, deleteDoc, serverTimestamp, query, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";"""
content = content.replace(old_import, new_import)

# 3. Add RFQ functions at the end
rfq_logic = """
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
"""

content += "\n" + rfq_logic

with open("assets/js/admin-crm.js", "w", encoding="utf-8") as f:
    f.write(content)

print("admin-crm.js updated successfully!")
