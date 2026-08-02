import os, re

repo = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"

# ============================================================
# STEP 1: Add Live Market Ticker ABOVE testimonials in index.html
# ============================================================

ticker_html = """
  <!-- ============================================================ -->
  <!-- APD LIVE MARKET TICKER - GLOBAL TRADE INDICES -->
  <!-- ============================================================ -->
  <div style="width: 100%; background: #0a0f1c; border-top: 1px solid rgba(212,175,55,0.3); border-bottom: 1px solid rgba(212,175,55,0.3); overflow: hidden; position: relative; z-index: 999;">
      <div style="background: #020617; padding: 6px 20px; display: flex; align-items: center; gap: 15px; justify-content: center; flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none;">
          <!-- Ticker Label -->
          <span style="color: #facc15; font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap; flex-shrink: 0;">
              📊 LIVE TRADE DESK
          </span>
          <span style="color: rgba(255,255,255,0.2); flex-shrink: 0;">|</span>
          <!-- TradingView Ticker Widget -->
          <div class="tradingview-widget-container" style="flex: 1; min-width: 0;">
              <div class="tradingview-widget-container__widget"></div>
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
              {
                "symbols": [
                  {"proName": "FX_IDC:DXY", "title": "USD Index"},
                  {"proName": "FX:USDINR", "title": "USD/INR"},
                  {"proName": "FX:USDINR", "title": "USD/INR"},
                  {"proName": "TVC:UKOIL", "title": "Brent Crude"},
                  {"proName": "ICEUS:SB1!", "title": "Sugar Futures"},
                  {"proName": "COMEX:STIL1!", "title": "US Steel"},
                  {"proName": "FX:EURUSD", "title": "EUR/USD"},
                  {"proName": "FX:USDAED", "title": "USD/AED"},
                  {"proName": "NYMEX:CL1!", "title": "Crude Oil"}
                ],
                "showSymbolLogo": true,
                "isTransparent": true,
                "displayMode": "adaptive",
                "colorTheme": "dark",
                "locale": "en"
              }
              </script>
          </div>
          <span style="color: rgba(255,255,255,0.2); flex-shrink: 0;">|</span>
          <span style="background: #ef4444; color: #fff; font-size: 9px; font-weight: 800; padding: 3px 8px; border-radius: 20px; animation: livePulse 2s infinite; white-space: nowrap; flex-shrink: 0;">● LIVE</span>
      </div>
  </div>
  <style>
  @keyframes livePulse { 0%,100%{opacity:1;} 50%{opacity:0.5;} }
  .tradingview-widget-container__widget { height: 46px; }
  </style>

"""

with open(os.path.join(repo, "index.html"), "r", encoding="utf-8") as f:
    content = f.read()

TESTIMONIAL_MARKER = "<!-- HIGHLIGHTED GLOBAL CLIENT VIDEO TESTIMONIALS (TOP POSITION) -->"

if TESTIMONIAL_MARKER in content and "APD LIVE MARKET TICKER" not in content:
    content = content.replace(TESTIMONIAL_MARKER, ticker_html + "\n  " + TESTIMONIAL_MARKER)
    with open(os.path.join(repo, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Live Market Ticker added above testimonials in index.html")
elif "APD LIVE MARKET TICKER" in content:
    print("SKIP: Ticker already exists in index.html")
else:
    print("ERROR: Testimonial marker not found in index.html")
