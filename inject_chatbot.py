import glob

def inject():
    files = ['buyer-rfqs.html', 'create-rfq.html', 'suppliers.html']
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if '/assets/js/ai-chatbot.js' not in html:
            html = html.replace('</body>', '  <script src="/assets/js/ai-chatbot.js"></script>\n</body>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Injected into {file}")

inject()
