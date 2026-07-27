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

            // 1. Remove old custom AI bot completely
            if (content.includes('sales-bot.css')) {
                content = content.replace(/<link rel="stylesheet" href="[^"]*sales-bot\.css[^"]*">\s*/g, '');
                changed = true;
            }
            if (content.includes('sales-bot.js')) {
                content = content.replace(/<script src="[^"]*sales-bot\.js[^"]*" type="module"><\/script>\s*/g, '');
                changed = true;
            }

            // 2. Fix membership.html text
            if (file === 'membership.html') {
                if (content.includes('Premium Lead(s)')) {
                    content = content.replace(/Premium Lead\(s\)/g, 'Verified Buyer(s)');
                    changed = true;
                }
                if (content.includes('Unlock Leads')) {
                    content = content.replace(/Unlock Leads/g, 'Unlock Verified Buyers');
                    changed = true;
                }
                if (content.includes('Unlock leads')) {
                    content = content.replace(/Unlock leads/g, 'Unlock Verified Buyers');
                    changed = true;
                }
                if (content.includes('Unlock Leads') || content.includes('unlock leads')) {
                     content = content.replace(/unlock leads/gi, 'Unlock Verified Buyers');
                     changed = true;
                }
            }

            // 3. Inject auto-open for Tidio strictly on key pages
            if (['index.html', 'membership.html', 'franchise.html'].includes(file)) {
                if (!content.includes('tidio-auto-open')) {
                    const autoOpenScript = `
<script id="tidio-auto-open">
  document.addEventListener("tidioChat-ready", function() {
      setTimeout(function() {
          window.tidioChatApi.open();
      }, 2000);
  });
</script>
</body>`;
                    content = content.replace(/<\/body>/i, autoOpenScript);
                    changed = true;
                }
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Fixed cleanly', fullPath);
            }
        }
    }
}

processFiles(__dirname);
