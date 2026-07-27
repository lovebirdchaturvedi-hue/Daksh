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

            // Remove Custom Launcher
            const launcherRegex = /<!-- Custom Tidio Launcher -->[\s\S]*?(?=<script src="\/\/code\.tidio\.co)/i;
            if (content.match(launcherRegex)) {
                content = content.replace(launcherRegex, '');
                changed = true;
            }

            // Remove tidioChatApi hide script
            const hideScriptRegex = /<script>\s*document\.addEventListener\("tidioChat-ready"[\s\S]*?<\/script>/i;
            if (content.match(hideScriptRegex)) {
                content = content.replace(hideScriptRegex, '');
                changed = true;
            }

            // Ensure WhatsApp is on the right
            if (content.match(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; left: 20px;/i)) {
                content = content.replace(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; left: 20px;/ig, 'class="desktop-wa-btn" style="position: fixed; bottom: 20px; right: 20px;');
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
