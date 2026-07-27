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
            const filename = path.basename(fullPath);

            // Default: WhatsApp on the LEFT (Tidio is default RIGHT)
            let waReplacement = 'class="desktop-wa-btn" style="position: fixed; bottom: 20px; left: 20px;';
            
            // If membership.html, WhatsApp goes on the RIGHT (because Tidio goes on the LEFT)
            if (filename === 'membership.html') {
                waReplacement = 'class="desktop-wa-btn" style="position: fixed; bottom: 20px; right: 20px;';
            }

            // Apply WhatsApp position
            if (content.match(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; (left|right): 20px;/i)) {
                content = content.replace(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; (left|right): 20px;/ig, waReplacement);
                changed = true;
            }
            
            // Clean up old scripts
            content = content.replace(/<script id="tidio-auto-open">[\s\S]*?<\/script>\s*/ig, '');
            content = content.replace(/<style id="tidio-force-left">[\s\S]*?<\/style>\s*/ig, '');

            // Inject auto-open for specific pages
            if (['index.html', 'membership.html', 'franchise.html'].includes(filename)) {
                let autoOpenScript = `
  <script id="tidio-auto-open">
    document.addEventListener("tidioChat-ready", function() {
      setTimeout(function() {
        if (window.tidioChatApi) {
          window.tidioChatApi.open();
        }
      }, 2000);
    });
  </script>
`;
                // If membership.html, also force Tidio to the left side
                if (filename === 'membership.html') {
                    autoOpenScript += `
  <style id="tidio-force-left">
    @media (min-width: 768px) {
      #tidio-chat iframe {
        left: 20px !important;
        right: auto !important;
      }
      #tidio-chat-iframe {
        left: 20px !important;
        right: auto !important;
      }
    }
  </style>
`;
                }

                if (content.match(/<\/body>/i)) {
                    content = content.replace(/<\/body>/i, autoOpenScript + '</body>');
                    changed = true;
                }
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Updated', fullPath);
            }
        }
    }
}

processFiles(__dirname);
