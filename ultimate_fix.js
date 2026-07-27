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

            // 1. FIX THE CORRUPTED SPAN TAGS (CRITICAL FIX)
            // Revert `or:` followed by `#` or `var` back to `<span style="color:`
            if (content.match(/or:\s*(#|var)/g)) {
                content = content.replace(/or:\s*(#|var)/g, '<span style="color:$1');
                changed = true;
            }

            // 2. WHATSAPP STRICTLY ON THE RIGHT
            if (content.match(/class="desktop-wa-btn"[^>]+(left|right):\s*20px/ig)) {
                content = content.replace(/(class="desktop-wa-btn" style="position: fixed; bottom: 20px;) (left|right): 20px;/ig, '$1 right: 20px;');
                changed = true;
            }

            // 3. MEMBERSHIP.HTML TEXT CHANGE
            if (path.basename(fullPath) === 'membership.html') {
                if (content.includes('Unlock Any 1 Premium Lead')) {
                    content = content.replace(/Unlock Any 1 Premium Lead/g, 'Unlock Any 1 Verified Buyer');
                    changed = true;
                }
                if (content.includes('Unlock Any 3 Premium Leads')) {
                    content = content.replace(/Unlock Any 3 Premium Leads/g, 'Unlock Any 3 Verified Buyers');
                    changed = true;
                }
            }

            // 4. INJECT THE TOP-NOTCH CUSTOM LAUNCHER ON THE LEFT
            content = content.replace(/<style id="tidio-force-left">[\s\S]*?<\/style>\s*/ig, '');
            content = content.replace(/<script id="tidio-auto-open">[\s\S]*?<\/script>\s*/ig, '');
            content = content.replace(/<!-- Custom APD AI Launcher -->[\s\S]*?<\/script>\s*/ig, '');
            
            const customLauncherHtml = `
  <!-- Custom APD AI Launcher -->
  <style>
    /* Hide Tidio's default launcher but keep the chat window working */
    #tidio-chat-iframe { display: none !important; }
       
    .custom-tidio-launcher {
      position: fixed;
      bottom: 20px;
      left: 20px;
      z-index: 99999;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .custom-tidio-launcher:hover {
      transform: scale(1.05) translateY(-5px);
    }
    .custom-tidio-badge {
      background: linear-gradient(90deg, var(--gold), #facc15);
      color: #000;
      font-weight: 900;
      font-size: 13px;
      padding: 6px 14px;
      border-radius: 50px;
      box-shadow: 0 4px 15px rgba(212,175,55,0.4);
      animation: customPulse 2s infinite;
      white-space: nowrap;
    }
    .custom-tidio-circle {
      width: 65px;
      height: 65px;
      border-radius: 50%;
      background: #3a56e4;
      border: 3px solid #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 5px 20px rgba(0,0,0,0.5);
      overflow: hidden;
      padding: 10px;
    }
    .custom-tidio-circle img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    @keyframes customPulse {
      0% { box-shadow: 0 0 0 0 rgba(212,175,55,0.7); }
      70% { box-shadow: 0 0 0 10px rgba(212,175,55,0); }
      100% { box-shadow: 0 0 0 0 rgba(212,175,55,0); }
    }
    
    /* Make sure Tidio's chat window itself (when opened) is forced to the left */
    @media (min-width: 768px) {
      div#tidio-chat iframe {
        left: 20px !important;
        right: auto !important;
        display: block !important;
      }
    }
  </style>

  <div class="custom-tidio-launcher" onclick="if(window.tidioChatApi){ window.tidioChatApi.open(); }">
    <div class="custom-tidio-badge">We Are Here! 👋</div>
    <div class="custom-tidio-circle">
      <!-- Premium AI Robot Icon -->
      <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" alt="AI Agent">
    </div>
  </div>

  <script>
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
  </script>
`;

            if (content.match(/<\/body>/i)) {
                content = content.replace(/<\/body>/i, customLauncherHtml + '\n</body>');
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Fixed up', fullPath);
            }
        }
    }
}

processFiles(__dirname);
