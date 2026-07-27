import os

def update_hero():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace Hero Content
    start_marker = '<h1 id="atomic-h1"'
    end_marker = '<div class="hero-buttons fade-in"'
    
    if start_marker in html and end_marker in html:
        before = html.split(start_marker)[0]
        after = end_marker + html.split(end_marker, 1)[1]
        
        new_hero = '''
        <h1 id="atomic-h1" class="fade-in" style="margin-bottom: 20px; text-shadow: 0 0 40px rgba(255,255,255,0.1); font-size: clamp(2rem, 5vw, 4rem); font-family: 'Playfair Display', serif; line-height: 1.1;">
            The Verified Corridor for<br> 
            <span style="color: var(--gold); background: linear-gradient(90deg, var(--gold), #facc15); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Global Institutional B2B Trade</span>
        </h1>
        <p class="fade-in" style="font-size: 1.1rem; margin-bottom: 30px; color: #94a3b8; max-width: 800px; line-height: 1.6;">
            Connect directly with audited manufacturers, verified suppliers, and multinational buyers. No broker interference. Secure cross-border transactions powered by standardized compliance metrics and live trade data.
        </p>

        <!-- MARKETPLACE SEARCH BAR -->
        <div class="fade-in" style="width: 100%; max-width: 800px; margin: 0 auto 15px auto; position: relative;">
            <div style="display: flex; background: rgba(2, 6, 23, 0.8); border: 2px solid rgba(212, 175, 55, 0.5); border-radius: 50px; overflow: hidden; backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <select style="background: rgba(255,255,255,0.05); border: none; border-right: 1px solid rgba(212,175,55,0.3); color: #fff; padding: 15px 20px; font-weight: 700; outline: none; cursor: pointer;">
                    <option style="color: #000;">All Categories</option>
                    <option style="color: #000;">Agro</option>
                    <option style="color: #000;">Textiles</option>
                    <option style="color: #000;">FMCG</option>
                    <option style="color: #000;">Chemicals</option>
                </select>
                <input type="text" placeholder="Search bulk commodities, verified exporters, or global destination ports..." style="flex: 1; background: transparent; border: none; color: #fff; padding: 15px 20px; font-size: 1rem; outline: none;" />
                <button style="background: linear-gradient(90deg, var(--gold), #8B6508); border: none; color: #000; font-weight: 900; padding: 0 30px; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s;">Search</button>
            </div>
            <div style="margin-top: 12px; font-size: 0.85rem; color: #94a3b8; text-align: left; padding-left: 20px;">
                <span style="color: var(--gold); font-weight: 700;">Trending:</span> 
                <a href="#" style="color: #cbd5e1; text-decoration: none; margin: 0 5px;">#Sugar Tenders</a> | 
                <a href="#" style="color: #cbd5e1; text-decoration: none; margin: 0 5px;">#1121 Rice</a> | 
                <a href="#" style="color: #cbd5e1; text-decoration: none; margin: 0 5px;">#Organic Spices</a>
            </div>
        </div>

        <!-- FLOATING LIVE METRIC COUNTERS -->
        <div class="fade-in" style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-bottom: 30px; margin-top: 20px;">
            <div style="background: rgba(15,23,42,0.6); padding: 10px 20px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);">
                <span style="color: #22c55e; font-weight: 900;">4,200+</span> <span style="color: #94a3b8; font-size: 0.9rem;">Verified Exporters</span>
            </div>
            <div style="background: rgba(15,23,42,0.6); padding: 10px 20px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);">
                <span style="color: #3b82f6; font-weight: 900;">12,800+</span> <span style="color: #94a3b8; font-size: 0.9rem;">Active Global Buyers</span>
            </div>
            <div style="background: rgba(15,23,42,0.6); padding: 10px 20px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1);">
                <span style="color: var(--gold); font-weight: 900;">$1.2B+</span> <span style="color: #94a3b8; font-size: 0.9rem;">Trade Liquidity</span>
            </div>
        </div>
        '''
        html = before + new_hero + after
        print("Hero replaced successfully.")
    
    # 2. Add Live RFQ Data Ticker below the hero section container
    ticker_marker = '<!-- ELITE TRADE CYCLE - FLOATING -->'
    if ticker_marker in html:
        ticker_html = '''
        <!-- GLOBAL RFQ DATA TICKER -->
        <div style="width: 100%; background: #020617; border-top: 1px solid rgba(212,175,55,0.3); border-bottom: 1px solid rgba(212,175,55,0.3); padding: 12px 0; overflow: hidden; white-space: nowrap; position: relative; z-index: 10;">
            <div style="display: inline-block; animation: scroll-ticker-fast 25s linear infinite; font-family: monospace; font-size: 0.9rem; font-weight: 700; color: #94a3b8;">
                <span style="color: #22c55e; margin: 0 15px;">⚡ RFQ #8892: 2,000 MT Sunflower Oil (Thailand) • L/C at Sight • 2 hrs ago</span> | 
                <span style="color: #eab308; margin: 0 15px;">⚡ RFQ #8841: Organic Spices Annual Contract (USA) • D&B Audited • 5 hrs ago</span> |
                <span style="color: #3b82f6; margin: 0 15px;">⚡ RFQ #8911: 10,000 MT Basmati Rice (Dubai) • FOB Jebel Ali • 12 mins ago</span> |
                <span style="color: #22c55e; margin: 0 15px;">⚡ RFQ #9021: 500 MT Raw Cotton (Vietnam) • TT Payment • 1 hr ago</span> |
                <span style="color: #22c55e; margin: 0 15px;">⚡ RFQ #8892: 2,000 MT Sunflower Oil (Thailand) • L/C at Sight • 2 hrs ago</span> | 
                <span style="color: #eab308; margin: 0 15px;">⚡ RFQ #8841: Organic Spices Annual Contract (USA) • D&B Audited • 5 hrs ago</span> |
                <span style="color: #3b82f6; margin: 0 15px;">⚡ RFQ #8911: 10,000 MT Basmati Rice (Dubai) • FOB Jebel Ali • 12 mins ago</span> |
                <span style="color: #22c55e; margin: 0 15px;">⚡ RFQ #9021: 500 MT Raw Cotton (Vietnam) • TT Payment • 1 hr ago</span>
            </div>
        </div>
        <style>
            @keyframes scroll-ticker-fast { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
        </style>
        '''
        html = html.replace(ticker_marker, ticker_html + "\n" + ticker_marker)
        print("Ticker added successfully.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_hero()
