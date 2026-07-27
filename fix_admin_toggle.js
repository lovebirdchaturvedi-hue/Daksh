const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

const newHeader = `<header>
  <h2>Admin – Supplier Management</h2>
  <div style="display:flex; gap: 20px; align-items:center;">
    <label style="cursor:pointer; display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; color:#cbd5e1; background:rgba(255,255,255,0.1); padding:8px 12px; border-radius:8px;">
      <input type="checkbox" id="hideBulkToggle" checked style="width:16px; height:16px; cursor:pointer;" onchange="loadSuppliers()"> 
      Hide Bulk CRM Leads
    </label>
    <button id="logoutBtn">Logout</button>
  </div>
</header>`;

content = content.replace(/<header>[\s\S]*?<\/header>/, newHeader);

// Now update loadSuppliers
const oldLimit = `const q = query(collection(db, "suppliers"), limit(500));`;
const newLimit = `const q = query(collection(db, "suppliers"), limit(3000));`;
content = content.replace(oldLimit, newLimit);

const oldForEach = `snap.forEach(d => {
      const s = d.data();`;
const newForEach = `snap.forEach(d => {
      const s = d.data();
      
      const hideBulk = document.getElementById('hideBulkToggle')?.checked;
      if (hideBulk && (s.isBulkLead || d.id.startsWith("bulk_"))) return;`;
content = content.replace(oldForEach, newForEach);

fs.writeFileSync(file, content);
console.log('admin.html updated successfully');
