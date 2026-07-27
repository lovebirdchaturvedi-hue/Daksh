const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

// Fix duplicate ADMIN_EMAIL
let parts = content.split('const ADMIN_EMAIL = "admin@apdglobaltrade.com";');
if (parts.length > 2) {
    // Keep the first one, replace subsequent ones with empty string
    content = parts[0] + 'const ADMIN_EMAIL = "admin@apdglobaltrade.com";' + parts.slice(1).join('/* duplicate removed */');
}

// Fix imports
content = content.replace(
    /import \{\s*getFirestore,\s*collection,\s*getDocs,\s*doc,\s*updateDoc,\s*deleteDoc\s*\} from "https:\/\/www\.gstatic\.com\/firebasejs\/10\.7\.1\/firebase-firestore\.js";/g,
    'import { getFirestore, collection, getDocs, doc, updateDoc, deleteDoc, query, limit } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";'
);

fs.writeFileSync(file, content);
console.log('Fixed admin.html');

// Now extract script and test syntax
const scriptMatch = content.match(/<script type="module">([\s\S]*?)<\/script>/);
if (scriptMatch) {
    fs.writeFileSync('temp.js', scriptMatch[1]);
    try {
        require('child_process').execSync('node -c temp.js');
        console.log('Syntax Check: PASSED');
    } catch (e) {
        console.error('Syntax Check: FAILED', e.message);
    }
}
