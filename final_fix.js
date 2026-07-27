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

            // Aggressive removal of all old bot artifacts
            const botCssRegex = /<link[^>]+sales-bot\.css[^>]*>/ig;
            if (content.match(botCssRegex)) {
                content = content.replace(botCssRegex, '');
                changed = true;
            }

            const botJsRegex = /<script[^>]+sales-bot\.js[^>]*><\/script>/ig;
            if (content.match(botJsRegex)) {
                content = content.replace(botJsRegex, '');
                changed = true;
            }

            const aiChatbotJsRegex = /<script[^>]+ai-chatbot\.js[^>]*><\/script>/ig;
            if (content.match(aiChatbotJsRegex)) {
                content = content.replace(aiChatbotJsRegex, '');
                changed = true;
            }

            const botRootRegex = /<div id="sales-bot-root"><\/div>/ig;
            if (content.match(botRootRegex)) {
                content = content.replace(botRootRegex, '');
                changed = true;
            }

            // Fix the corrupted tag in index.html specifically if it exists
            if (content.includes('<span style="col  ')) {
                content = content.replace(/<span style="col\s*/g, '');
                changed = true;
            }

            // Global auto-open script injection
            // First, remove old instances
            const autoOpenRegex = /<script id="tidio-auto-open">[\s\S]*?<\/script>\s*/ig;
            if (content.match(autoOpenRegex)) {
                content = content.replace(autoOpenRegex, '');
                changed = true;
            }

            const autoOpenScript = `
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
                content = content.replace(/<\/body>/i, autoOpenScript + '\n</body>');
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Cleaned and injected', fullPath);
            }
        }
    }
}

processFiles(__dirname);
