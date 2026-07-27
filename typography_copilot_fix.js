const fs = require('fs');
const path = require('path');

const dir = __dirname;
const htmlFiles = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

for (const file of htmlFiles) {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    let changed = false;

    // 1. Sleeker Typography for Nav Links
    if (content.includes('font-size: 0.85rem !important;')) {
        content = content.replace(/font-size:\s*0\.85rem\s*!important;/g, 'font-size: 0.7rem !important;');
        changed = true;
    }
    
    // 2. Sleeker Typography for Logo Text
    if (content.includes('font-size: 24px; color: #fff; letter-spacing: 1px;">APD <span style="color: var(--gold);">Global</span> Trade</span>')) {
        content = content.replace(/font-size:\s*24px;\s*color:\s*#fff;\s*letter-spacing:\s*1px;">APD <span style="color: var\(--gold\);">Global<\/span> Trade<\/span>/g, 'font-size: 20px; color: #fff; letter-spacing: 1.5px;">APD <span style="color: var(--gold);">Global</span> Trade</span>');
        changed = true;
    }
    
    // 3. Restore Copilot AI to specific pages
    if (['membership.html', 'supplier-login.html', 'supplier-dashboard.html'].includes(file)) {
        if (!content.includes('sales-bot.js')) {
            const copilotInjection = `
<!-- Trade Copilot Integration -->
<link rel="stylesheet" href="/assets/css/sales-bot.css?v=1.5">
<script src="/assets/js/sales-bot.js?v=1.5" type="module"></script>
</body>`;
            content = content.replace(/<\/body>/i, copilotInjection);
            changed = true;
        }
    }

    if (changed) {
        fs.writeFileSync(path.join(dir, file), content);
        console.log(`Updated typography & restored Copilot to ${file}`);
    }
}

// 4. Update sales-bot.js text to be "Trade Copilot"
const salesBotPath = path.join(dir, 'assets', 'js', 'sales-bot.js');
if (fs.existsSync(salesBotPath)) {
    let sbContent = fs.readFileSync(salesBotPath, 'utf8');
    let sbChanged = false;

    if (sbContent.includes("APD AI Sales BOT")) {
        sbContent = sbContent.replace(/APD AI Sales BOT/g, "Trade Copilot");
        sbChanged = true;
    }
    
    if (sbContent.includes("ACTIVE SALES AGENT")) {
        sbContent = sbContent.replace(/ACTIVE SALES AGENT/g, "AI INVOICE & TRADE ASSISTANT");
        sbChanged = true;
    }
    
    if (sbContent.includes("APD Senior Sales Assistant")) {
        sbContent = sbContent.replace(/APD Senior Sales Assistant/g, "Trade Copilot");
        sbChanged = true;
    }

    if (sbChanged) {
        fs.writeFileSync(salesBotPath, sbContent);
        console.log('Updated sales-bot.js to Trade Copilot');
    }
}
