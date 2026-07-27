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

            // Remove old sales-bot
            if (content.match(/<link[^>]*href="[^"]*sales-bot\.css"[^>]*>/i)) {
                content = content.replace(/<link[^>]*href="[^"]*sales-bot\.css"[^>]*>\s*/ig, '');
                changed = true;
            }
            if (content.match(/<script[^>]*src="[^"]*sales-bot\.js"[^>]*><\/script>/i)) {
                content = content.replace(/<script[^>]*src="[^"]*sales-bot\.js"[^>]*><\/script>\s*/ig, '');
                changed = true;
            }
            if (content.match(/<div id="sales-bot-root"><\/div>/i)) {
                content = content.replace(/<div id="sales-bot-root"><\/div>\s*/ig, '');
                changed = true;
            }
            
            // Move WhatsApp to the left
            if (content.match(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; right: 20px;/i)) {
                content = content.replace(/class="desktop-wa-btn" style="position: fixed; bottom: 20px; right: 20px;/ig, 'class="desktop-wa-btn" style="position: fixed; bottom: 20px; left: 20px;');
                changed = true;
            }

            // Remove any existing Tidio script to prevent duplicates
            content = content.replace(/<script src="\/\/code\.tidio\.co\/zs195w58z0vrzcknn4gkbosvrnn63xfe\.js" async><\/script>\s*/ig, '');

            // Inject custom Tidio launcher and script before </body>
            const tidioCustomLauncher = `
  <!-- Custom Tidio Launcher -->
  <style>
    .custom-tidio-launcher {
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 9999;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .custom-tidio-launcher:hover {
      transform: scale(1.05);
    }
    .custom-tidio-avatar {
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: linear-gradient(135deg, #0f172a, #1e293b);
      border: 2px solid var(--gold);
      box-shadow: 0 10px 25px rgba(0,0,0,0.5), 0 0 15px rgba(212,175,55,0.4);
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }
    .custom-tidio-avatar img {
      width: 35px;
      height: 35px;
      object-fit: contain;
    }
    .custom-tidio-pulse {
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      border: 2px solid var(--gold);
      animation: customPulse 2s infinite;
      opacity: 0;
    }
    .custom-tidio-badge {
      background: linear-gradient(90deg, var(--gold), #facc15);
      color: #000;
      padding: 8px 15px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 800;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      position: relative;
      animation: customFloat 3s ease-in-out infinite;
    }
    .custom-tidio-badge::after {
      content: '';
      position: absolute;
      right: -8px;
      top: 50%;
      transform: translateY(-50%);
      border-width: 6px 0 6px 8px;
      border-style: solid;
      border-color: transparent transparent transparent #facc15;
    }
    @keyframes customPulse {
      0% { transform: scale(1); opacity: 0.8; }
      100% { transform: scale(1.5); opacity: 0; }
    }
    @keyframes customFloat {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-5px); }
    }
    @media (max-width: 768px) {
      .custom-tidio-badge { display: none; }
    }
  </style>
  <div class="custom-tidio-launcher" onclick="window.tidioChatApi && window.tidioChatApi.open()">
    <div class="custom-tidio-badge">We Are Here!</div>
    <div class="custom-tidio-avatar">
      <div class="custom-tidio-pulse"></div>
      <img src="/assets/images/logo.png" alt="Bot">
    </div>
  </div>
  <script src="//code.tidio.co/zs195w58z0vrzcknn4gkbosvrnn63xfe.js" async></script>
  <script>
    document.addEventListener("tidioChat-ready", function() {
      window.tidioChatApi.hide();
    });
    document.addEventListener("tidioChat-close", function() {
      window.tidioChatApi.hide();
    });
  </script>
`;
            
            if (content.match(/<\/body>/i)) {
                content = content.replace(/<\/body>/i, tidioCustomLauncher + '\n</body>');
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Updated', fullPath);
            }
        }
    }
}

processFiles(__dirname);
