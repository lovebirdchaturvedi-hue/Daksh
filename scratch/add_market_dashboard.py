import sys

MARKET_DATA_SECTION = """
  <!-- ADVANCED MARKET DATA DASHBOARD -->
  <section style="padding: 60px 20px; background: #0f172a; border-top: 1px solid rgba(212,175,55,0.2);">
      <div style="max-width: 1240px; margin: 0 auto;">
          <div style="text-align: center; margin-bottom: 40px;">
              <span style="background: rgba(212, 175, 55, 0.15); color: var(--gold); padding: 6px 18px; border-radius: 30px; font-size: 0.8rem; font-weight: 800; border: 1px solid rgba(212, 175, 55, 0.4); text-transform: uppercase; letter-spacing: 1px;">REAL-TIME MARKET INTELLIGENCE</span>
              <h2 style="color: #fff; font-family: 'Outfit', sans-serif; font-size: 34px; font-weight: 800; margin: 15px 0 10px;">Global Trade Dashboard</h2>
              <p style="color: #94a3b8; font-size: 15px; max-width: 720px; margin: 0 auto;">Monitor major commodities, forex crosses, and global indices in real-time to make informed export and import decisions.</p>
          </div>
          
          <div style="background: #020617; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); padding: 20px;">
              <!-- TradingView Widget BEGIN -->
              <div class="tradingview-widget-container" style="height: 500px; width: 100%;">
                <div class="tradingview-widget-container__widget" style="height: calc(100% - 32px); width: 100%;"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
                {
                "colorTheme": "dark",
                "dateRange": "12M",
                "showChart": true,
                "locale": "en",
                "width": "100%",
                "height": "100%",
                "largeChartUrl": "",
                "isTransparent": true,
                "showSymbolLogo": true,
                "showFloatingTooltip": false,
                "tabs": [
                  {
                    "title": "Commodities",
                    "symbols": [
                      { "s": "TVC:GOLD", "d": "Gold" },
                      { "s": "TVC:SILVER", "d": "Silver" },
                      { "s": "TVC:USOIL", "d": "WTI Crude Oil" },
                      { "s": "TVC:UKOIL", "d": "Brent Crude" },
                      { "s": "CBOT:ZC1!", "d": "Corn" },
                      { "s": "CBOT:ZW1!", "d": "Wheat" }
                    ],
                    "originalTitle": "Commodities"
                  },
                  {
                    "title": "Forex",
                    "symbols": [
                      { "s": "FX:EURUSD", "d": "EUR/USD" },
                      { "s": "FX:GBPUSD", "d": "GBP/USD" },
                      { "s": "FX:USDJPY", "d": "USD/JPY" },
                      { "s": "FX:USDINR", "d": "USD/INR" },
                      { "s": "FX:AUDUSD", "d": "AUD/USD" },
                      { "s": "FX:USDCAD", "d": "USD/CAD" }
                    ],
                    "originalTitle": "Forex"
                  },
                  {
                    "title": "Global Indices",
                    "symbols": [
                      { "s": "OANDA:SPX500USD", "d": "S&P 500" },
                      { "s": "OANDA:NAS100USD", "d": "Nasdaq 100" },
                      { "s": "OANDA:US30USD", "d": "Dow Jones" },
                      { "s": "OANDA:UK100GBP", "d": "FTSE 100" },
                      { "s": "OANDA:EU50EUR", "d": "Euro Stoxx 50" }
                    ],
                    "originalTitle": "Indices"
                  }
                ]
              }
                </script>
              </div>
              <!-- TradingView Widget END -->
          </div>
      </div>
  </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

marker = '<!-- HIGHLIGHTED GLOBAL CLIENT VIDEO TESTIMONIALS (TOP POSITION) -->'
if marker in content:
    content = content.replace(marker, MARKET_DATA_SECTION + "\n\n  " + marker)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Added Market Overview dashboard!")
else:
    print("ERROR: Testimonials marker not found.")
