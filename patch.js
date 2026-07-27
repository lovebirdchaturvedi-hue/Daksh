const fs = require('fs');
const file = 'C:/Users/DELL/.gemini/antigravity/playground/vacant-ride/daksh_repo/admin.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Add null check for user.email
content = content.replace(
    'if (user.email.toLowerCase() !== ADMIN_EMAIL.toLowerCase()) {',
    'if (!user.email || user.email.toLowerCase() !== ADMIN_EMAIL.toLowerCase()) {'
);

// 2. Reduce timeout to 2 seconds so they don't have to wait
content = content.replace(
    'new Promise((_, reject) => setTimeout(() => reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 7000))',
    'new Promise((_, reject) => setTimeout(() => reject(new Error("Firebase Query Timeout - Connection Blocked or Hanging!")), 2000))'
);

fs.writeFileSync(file, content);
console.log('Patched admin.html defensively');
