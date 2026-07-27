const fs = require('fs');
const path = require('path');

function processFiles(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            if (file !== 'node_modules' && file !== '.git') {
                processFiles(fullPath);
            }
        } else if (fullPath.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            let changed = false;

            // Fix the rgba issue
            if (content.includes('or: rgba')) {
                content = content.replace(/or:\s*rgba/g, '<span style="color: rgba');
                changed = true;
            }
            if (content.includes('or:rgba')) {
                content = content.replace(/or:\s*rgba/g, '<span style="color: rgba');
                changed = true;
            }

            // Force Tidio iframe to the left
            if (content.includes('/* Make sure Tidio\'s chat window itself') && !content.includes('#tidio-chat-iframe { left: 20px !important; right: auto !important; }')) {
                content = content.replace('/* Make sure Tidio\'s chat window itself', '#tidio-chat-iframe { left: 20px !important; right: auto !important; bottom: 20px !important; }\n    /* Make sure Tidio\'s chat window itself');
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Fixed', fullPath);
            }
        }
    }
}

processFiles(__dirname);
