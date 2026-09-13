import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

mobile_btn_html = '''
    <style>
        .mobile-post-btn { display: none !important; }
        @media(max-width: 768px) {
            .mobile-post-btn { 
                display: flex !important; 
                background: linear-gradient(180deg, #22c55e, #166534); 
                color: #fff !important; 
                padding: 6px 12px; 
                font-weight: 800; 
                font-size: 0.75rem; 
                border-radius: 50px; 
                text-decoration: none;
                align-items: center;
                white-space: nowrap;
                box-shadow: 0 4px 10px rgba(34, 197, 94, 0.3);
            }
        }
    </style>
    <div style="display: flex; align-items: center; gap: 10px;">
        <a href="#" onclick="document.getElementById('rfqModal').style.display='flex'; return false;" class="mobile-post-btn">
            POST LIVE
        </a>
    </div>
  </header>'''

text = text.replace('</header>', mobile_btn_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added Mobile sticky POST LIVE button to index.html')
