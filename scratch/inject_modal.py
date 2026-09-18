import glob
import codecs

# 1. Extract rfqModal from index.html
with codecs.open('index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()

start_modal = idx_text.find('<!-- QUICK RFQ MODAL -->')
if start_modal == -1:
    start_modal = idx_text.find('<div id="rfqModal"')

# We know the JS handler is below it, we should include the handler too.
end_modal = idx_text.find('window.handleQuickRFQ = async function(e)')
end_script = idx_text.find('</script>', end_modal) + 9

modal_html = idx_text[start_modal:end_script]

print("Extracted modal length:", len(modal_html))

# 2. Inject into all other HTML files right before </body>
html_files = glob.glob('*.html')
for file in html_files:
    if file == 'index.html':
        continue
        
    try:
        with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            
        # First, restore the onclick buttons we broke
        text = text.replace('href="/create-rfq.html"', 'href="#" onclick="document.getElementById(\'rfqModal\').style.display=\'flex\'; return false;"')
        
        # Inject the modal if it's not already there
        if 'id="rfqModal"' not in text:
            # find </body>
            body_idx = text.rfind('</body>')
            if body_idx != -1:
                text = text[:body_idx] + '\n' + modal_html + '\n' + text[body_idx:]
                
        with codecs.open(file, 'w', encoding='utf-8') as f:
            f.write(text)
            
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("Modal injected into all pages and buttons fixed.")
