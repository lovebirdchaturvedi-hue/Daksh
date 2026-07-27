const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

const badLine = '${isLegacy ? "<button class=\\\'ban\\\' style=\\\'background:#000\\\' onclick=\\\'del(\\\\\\"" + d.id + "\\\\\\")\\\'>Delete</button>" : ""}';

// Let's just find the exact line and replace it.
const lines = content.split('\n');
for (let i=0; i<lines.length; i++) {
    if (lines[i].includes('isLegacy ?')) {
        lines[i] = "            ${isLegacy ? `<button class='ban' style='background:#000' onclick='del(\"${d.id}\")'>Delete</button>` : ''}";
        break;
    }
}

fs.writeFileSync(file, lines.join('\n'));
console.log('Fixed syntax error in admin.html');
