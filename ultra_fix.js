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

            // 1. Fix the Top Bar Fonts in all HTML files
            if (content.includes('clamp(12px, 1.2vw, 16px)')) {
                content = content.replace(/clamp\(12px,\s*1\.2vw,\s*16px\)/g, '13px');
                changed = true;
            }
            if (content.includes('clamp(11px, 1.1vw, 14px)')) {
                content = content.replace(/clamp\(11px,\s*1\.1vw,\s*14px\)/g, '11.5px');
                changed = true;
            }

            // 2. Add Tidio script if missing
            if (['index.html', 'membership.html', 'franchise.html'].includes(file)) {
                if (!content.includes('code.tidio.co/zs195w58z0vrzcknn4gkbosvrnn63xfe.js')) {
                    const tidioScript = `
<script src="//code.tidio.co/zs195w58z0vrzcknn4gkbosvrnn63xfe.js" async></script>
</body>`;
                    content = content.replace(/<\/body>/i, tidioScript);
                    changed = true;
                }
            }

            // 3. Fix double Google Translate
            if (content.includes('//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit')) {
                // Remove the second instance if there are two, or just replace one of them
                let matches = content.match(/<script type="text\/javascript"[^>]*src="[^"]*translate\.google\.com\/translate_a\/element\.js\?cb=googleTranslateElementInit"><\/script>/gi);
                if (matches && matches.length > 1) {
                    // Remove all but the first match
                    let count = 0;
                    content = content.replace(/<script type="text\/javascript"[^>]*src="[^"]*translate\.google\.com\/translate_a\/element\.js\?cb=googleTranslateElementInit"><\/script>/gi, (match) => {
                        count++;
                        return count === 1 ? match : '';
                    });
                    changed = true;
                }
            }

            // Remove duplicate google_translate_element divs
            if (content.match(/id="google_translate_element"/g) && content.match(/id="google_translate_element"/g).length > 1) {
                let divCount = 0;
                content = content.replace(/<div id="google_translate_element"[^>]*><\/div>/gi, (match) => {
                    divCount++;
                    return divCount === 1 ? match : '';
                });
                changed = true;
            }

            // Remove duplicate initialization scripts
            if (content.match(/function googleTranslateElementInit/g) && content.match(/function googleTranslateElementInit/g).length > 1) {
                let initCount = 0;
                content = content.replace(/function googleTranslateElementInit\(\) \{[\s\S]*?\}/gi, (match) => {
                    initCount++;
                    return initCount === 1 ? match : '';
                });
                changed = true;
            }

            if (changed) {
                fs.writeFileSync(fullPath, content);
                console.log('Ultra Fixed', fullPath);
            }
        }
    }
}

processFiles(__dirname);
