const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin-crm.html';
if (fs.existsSync(file)) {
    let content = fs.readFileSync(file, 'utf8');
    content = content.replace('max-width:1200px;', 'max-width:98%;');
    if (!content.includes('<th>Phone</th>')) {
        content = content.replace('<th>Email</th>', '<th>Email</th>\n<th>Phone</th>');
    }
    content = content.replace(/colspan="7"/g, 'colspan="8"');
    content = content.replace(/colspan='7'/g, 'colspan=\\\'8\\\'');
    fs.writeFileSync(file, content);
}
