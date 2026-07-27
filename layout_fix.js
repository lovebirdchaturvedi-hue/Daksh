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

            // Make sure WhatsApp is ALWAYS on the right
            if (content.match(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; (left|right): 20px;/i)) {
                content = content.replace(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; (left|right): 20px;/ig, 'class="desktop-wa-btn" style="position: fixed; bottom: 20px; right: 20px;');
                changed = true;
            }

            // Remove previous instances of the auto-open and force-left scripts to avoid duplicates
            content = content.replace(/<script id="tidio-auto-open">[\s\S]*?<\/script>\s*/ig, '');
            content = content.replace(/<style id="tidio-force-left">[\s\S]*?<\/style>\s*/ig, '');

            // Inject the global force-left CSS and the auto-open script
            const globalTidioConfig = `
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
            
            if (content.match(/<\/body>/i)) {
                content = content.replace(/<\/body>/i, globalTidioConfig + '\n</body>');
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Applied global layout to', fullPath);
            }
        }
    }
}

processFiles(__dirname);
