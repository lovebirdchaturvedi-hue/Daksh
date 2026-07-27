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

            // 1. REPAIR THE CSS DAMAGE
            // My previous regex replaced `or: #` with `<span style="color:#`
            // which broke valid CSS `color: #` into `col<span style="color:#`
            if (content.includes('col<span style="color:')) {
                content = content.replace(/col<span style="color:/g, 'color: ');
                changed = true;
            }

            // 2. FIX TIDIO BOT AUTO-OPEN AND HIDING
            // The CSS `#tidio-chat-iframe { display: none !important; }` hid the actual chat window too!
            if (content.includes('#tidio-chat-iframe { display: none !important; }')) {
                content = content.replace('#tidio-chat-iframe { display: none !important; }', '/* Button hidden via API instead of CSS */');
                changed = true;
            }
            
            // Fix the custom launcher logic
            const oldScript = `  <script>
    document.addEventListener("tidioChat-ready", function() {
      // Hide Tidio's default button
      window.tidioChatApi.hide();
      
      // Auto-open logic for specific pages
      const currentPath = window.location.pathname;
      if (currentPath === '/' || currentPath.includes('index.html') || currentPath.includes('membership.html') || currentPath.includes('franchise.html')) {
        setTimeout(function() {
          window.tidioChatApi.open();
        }, 2000);
      }
      
      // When chat is closed, we need to hide Tidio again so our custom launcher shows
      window.tidioChatApi.on("close", function() {
        window.tidioChatApi.hide();
      });
    });
  </script>`;

            const newScript = `  <script>
    document.addEventListener("tidioChat-ready", function() {
      // Hide Tidio's default button initially
      window.tidioChatApi.hide();
      
      // Auto-open logic for specific pages
      const currentPath = window.location.pathname;
      if (currentPath === '/' || currentPath.includes('index.html') || currentPath.includes('membership.html') || currentPath.includes('franchise.html')) {
        setTimeout(function() {
          window.tidioChatApi.show();
          window.tidioChatApi.open();
        }, 2000);
      }
      
      // When chat is closed, hide the default button again
      window.tidioChatApi.on("close", function() {
        window.tidioChatApi.hide();
      });
    });
  </script>`;

            if (content.includes(oldScript)) {
                content = content.replace(oldScript, newScript);
                changed = true;
            }
            
            // Also fix the onclick in the html button
            const oldOnClick = 'onclick="if(window.tidioChatApi){ window.tidioChatApi.open(); }"';
            const newOnClick = 'onclick="if(window.tidioChatApi){ window.tidioChatApi.show(); window.tidioChatApi.open(); }"';
            if (content.includes(oldOnClick)) {
                content = content.replace(oldOnClick, newOnClick);
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Repaired CSS & Bot in', fullPath);
            }
        }
    }
}

processFiles(__dirname);
