import os

with open('create-rfq.html', 'r', encoding='utf-8') as f:
    text = f.read()

tracking_html = '''    <div style="margin-bottom: 25px; padding: 10px; background: rgba(220, 38, 38, 0.1); border: 1px solid rgba(220, 38, 38, 0.3); border-radius: 8px; display: flex; align-items: center; gap: 10px;">
        <span style="display: inline-block; width: 8px; height: 8px; background: #ef4444; border-radius: 50%; box-shadow: 0 0 8px #ef4444; animation: pulse 1.5s infinite;"></span>
        <span style="color: #fca5a5; font-size: 13px; font-weight: 600;" id="liveViewerCount">-- Exporters currently active and ready to quote</span>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const countEl = document.getElementById("liveViewerCount");
            if(countEl) {
                const isHigh = Math.random() > 0.7; 
                const count = isHigh ? Math.floor(Math.random() * 500) + 1000 : Math.floor(Math.random() * 800) + 100;
                countEl.innerText = count.toLocaleString() + " Exporters currently active and ready to quote";
            }
        });
    </script>'''

text = text.replace('<h3>Buyer Contact Details</h3>', tracking_html + '\n    <h3>Buyer Contact Details</h3>')

with open('create-rfq.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated create-rfq.html')
