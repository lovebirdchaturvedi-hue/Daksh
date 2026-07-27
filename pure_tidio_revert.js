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
            if (content.match(/or:\s*rgba/gi)) {
                content = content.replace(/or:\s*rgba/gi, '<span style="color: rgba');
                changed = true;
            }

            // Remove the Custom AI Launcher and scripts entirely
            if (content.includes('<!-- Custom APD AI Launcher -->')) {
                content = content.replace(/<!-- Custom APD AI Launcher -->[\s\S]*?<\/script>\s*/ig, '');
                changed = true;
            }

            // Remove any old Tidio hacks if they somehow survived
            if (content.includes('<style id="tidio-force-left">')) {
                content = content.replace(/<style id="tidio-force-left">[\s\S]*?<\/style>\s*/ig, '');
                changed = true;
            }
            if (content.includes('<script id="tidio-auto-open">')) {
                content = content.replace(/<script id="tidio-auto-open">[\s\S]*?<\/script>\s*/ig, '');
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Cleaned up', fullPath);
            }
        }
    }
}

processFiles(__dirname);
