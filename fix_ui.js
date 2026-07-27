const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Fix container width
content = content.replace('max-width:1200px;', 'max-width:98%;');

// 2. Add Phone header
content = content.replace('<th>Email</th>', '<th>Email</th>\n<th>Phone</th>');

// 3. Fix colspans
content = content.replace(/colspan="7"/g, 'colspan="8"');
content = content.replace(/colspan='7'/g, 'colspan=\\\'8\\\'');

fs.writeFileSync(file, content);
console.log('Fixed UI in admin.html');
