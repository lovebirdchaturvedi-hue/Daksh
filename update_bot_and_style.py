import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove auto-open
html = re.sub(r'<script id="tidio-auto-open">.*?</script>', '', html, flags=re.DOTALL)

# Find whatsapp button and move it left by changing 'right: 30px;' to 'right: 110px;'
html = re.sub(r'(\.whatsapp-float\s*\{[^}]*right:\s*)30px', r'\g<1>110px', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update membership.html
with open('membership.html', 'r', encoding='utf-8') as f:
    m_html = f.read()

# Remove auto-open
m_html = re.sub(r'<script id="tidio-auto-open">.*?</script>', '', m_html, flags=re.DOTALL)

# Find whatsapp button and move it left by changing 'right: 30px;' to 'right: 110px;'
m_html = re.sub(r'(\.whatsapp-float\s*\{[^}]*right:\s*)30px', r'\g<1>110px', m_html)

# Now replace the Bank Transfer Details
start_tag = '<!-- GLOBAL BANK TRANSFER DETAILS -->'
end_tag = '<!-- ENTERPRISE QUALIFICATION FORM -->'

start_idx = m_html.find(start_tag)
end_idx = m_html.find(end_tag)

new_bank_details = """        <!-- GLOBAL BANKING PARTNERS SECTION (PREMIUM) -->
        <div style="background: #020617; border: 1px solid rgba(212,175,55,0.3); border-radius: 20px; padding: 40px; max-width: 1100px; margin: 0 auto 60px; position: relative; overflow: hidden;">
            <div style="position: absolute; top: -10%; left: -5%; width: 40%; height: 40%; background: radial-gradient(circle, rgba(212,175,55,0.08) 0%, transparent 70%); pointer-events: none;"></div>
            
            <div style="text-align: center; margin-bottom: 30px; position: relative; z-index: 10;">
                <span style="color: var(--gold); font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: 8px;">Direct Wire Transfer</span>
                <h3 style="font-size: 28px; color: #fff; margin: 0; font-weight: 800;">Global Bank Accounts (7 Currencies)</h3>
                <p style="color: #94a3b8; font-size: 15px; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto;">For international clients who prefer direct bank-to-bank wire transfers via ACH, SEPA, SWIFT, CHAPS, or EFT.</p>
            </div>
            
            <style>
                .premium-bank-card {
                    background: rgba(255, 255, 255, 0.02);
                    border: 1px solid rgba(255, 255, 255, 0.06);
                    border-radius: 16px;
                    padding: 25px;
                    transition: all 0.3s ease;
                    position: relative;
                    overflow: hidden;
                }
                .premium-bank-card:hover {
                    transform: translateY(-5px);
                    background: rgba(255, 255, 255, 0.04);
                    border-color: rgba(212, 175, 55, 0.4);
                    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
                }
                .premium-bank-card::before {
                    content: '';
                    position: absolute;
                    top: 0; left: 0; width: 100%; height: 4px;
                    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.5), transparent);
                    opacity: 0;
                    transition: 0.3s;
                }
                .premium-bank-card:hover::before { opacity: 1; }
                
                .bank-card-header {
                    display: flex;
                    align-items: center;
                    gap: 15px;
                    border-bottom: 1px solid rgba(255,255,255,0.06);
                    padding-bottom: 15px;
                    margin-bottom: 15px;
                }
                .bank-card-flag {
                    font-size: 2rem;
                    line-height: 1;
                }
                .bank-card-title {
                    font-family: 'Outfit', sans-serif;
                    color: #fff;
                    font-size: 1.15rem;
                    font-weight: 700;
                    line-height: 1.2;
                }
                .bank-card-subtitle {
                    color: #60a5fa;
                    font-size: 0.8rem;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }
                .bank-card-details {
                    font-size: 13px;
                    color: #cbd5e1;
                    line-height: 1.8;
                }
                .bank-card-label {
                    color: #94a3b8;
                    display: inline-block;
                    width: 90px;
                }
                .bank-card-value {
                    color: #fff;
                    font-weight: 600;
                }
                
                .premium-bank-card.gold-tier {
                    background: rgba(212, 175, 55, 0.05);
                    border: 1px solid rgba(212, 175, 55, 0.3);
                }
                .premium-bank-card.gold-tier:hover {
                    border-color: rgba(212, 175, 55, 0.6);
                    box-shadow: 0 15px 35px rgba(212,175,55,0.2);
                }
                .premium-bank-card.gold-tier::before {
                    opacity: 1;
                    background: var(--gold);
                }
                .premium-bank-card.gold-tier .bank-card-title {
                    color: var(--gold);
                }
            </style>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; position: relative; z-index: 10;">
                
                <!-- SWIFT Account -->
                <div class="premium-bank-card gold-tier" style="grid-column: 1 / -1; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; align-items: center;">
                    <div class="bank-card-header" style="border: none; padding: 0; margin: 0;">
                        <div class="bank-card-flag" style="font-size: 3.5rem;">🌐</div>
                        <div>
                            <div class="bank-card-title" style="font-size: 1.5rem;">GLOBAL SWIFT Account</div>
                            <div class="bank-card-subtitle" style="color: #cbd5e1;">The Currency Cloud Limited (UK)</div>
                        </div>
                    </div>
                    <div class="bank-card-details" style="font-size: 14px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px;">
                        <div>
                            <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                            <span class="bank-card-label">Account No:</span> <span class="bank-card-value">GB82TCCL04143422806894</span><br>
                        </div>
                        <div>
                            <span class="bank-card-label">BIC/SWIFT:</span> <span class="bank-card-value">TCCLGB3L</span><br>
                            <span class="bank-card-label">Address:</span> <span class="bank-card-value">1 Sheldon Square, London, UK</span>
                        </div>
                    </div>
                </div>

                <!-- USD Account -->
                <div class="premium-bank-card">
                    <div class="bank-card-header">
                        <div class="bank-card-flag">🇺🇸</div>
                        <div>
                            <div class="bank-card-title">USD Account</div>
                            <div class="bank-card-subtitle">Community Federal Savings Bank</div>
                        </div>
                    </div>
                    <div class="bank-card-details">
                        <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                        <span class="bank-card-label">Account No:</span> <span class="bank-card-value">8302840763</span><br>
                        <span class="bank-card-label">Routing (ACH):</span> <span class="bank-card-value">026073150</span><br>
                        <span class="bank-card-label">Address:</span> <span class="bank-card-value" style="font-size:12px;">5 Penn Plaza, 14th Floor, NY 10001, US</span>
                    </div>
                </div>

                <!-- UK GBP -->
                <div class="premium-bank-card">
                    <div class="bank-card-header">
                        <div class="bank-card-flag">🇬🇧</div>
                        <div>
                            <div class="bank-card-title">GBP Account</div>
                            <div class="bank-card-subtitle">Banking Circle S.A. UK Branch</div>
                        </div>
                    </div>
                    <div class="bank-card-details">
                        <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                        <span class="bank-card-label">Account No:</span> <span class="bank-card-value">48040137</span><br>
                        <span class="bank-card-label">Sort Code:</span> <span class="bank-card-value">608382</span><br>
                        <span class="bank-card-label">Address:</span> <span class="bank-card-value" style="font-size:12px;">68 King William Street, London, UK</span>
                    </div>
                </div>

                <!-- EUR Account -->
                <div class="premium-bank-card">
                    <div class="bank-card-header">
                        <div class="bank-card-flag">🇪🇺</div>
                        <div>
                            <div class="bank-card-title">EUR Account</div>
                            <div class="bank-card-subtitle">Banking Circle Germany</div>
                        </div>
                    </div>
                    <div class="bank-card-details">
                        <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                        <span class="bank-card-label">IBAN:</span> <span class="bank-card-value">DE41202208000048040137</span><br>
                        <span class="bank-card-label">BIC/SWIFT:</span> <span class="bank-card-value">SXPYDEHH</span><br>
                        <span class="bank-card-label">Address:</span> <span class="bank-card-value" style="font-size:12px;">Maximilianstraße 54, 80538 München, DE</span>
                    </div>
                </div>

                <!-- CAD Account -->
                <div class="premium-bank-card">
                    <div class="bank-card-header">
                        <div class="bank-card-flag">🇨🇦</div>
                        <div>
                            <div class="bank-card-title">CAD Account</div>
                            <div class="bank-card-subtitle">Digital Commerce Bank</div>
                        </div>
                    </div>
                    <div class="bank-card-details">
                        <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                        <span class="bank-card-label">Account No:</span> <span class="bank-card-value">962668612</span><br>
                        <span class="bank-card-label">Routing:</span> <span class="bank-card-value">035210009</span><br>
                        <span class="bank-card-label">Address:</span> <span class="bank-card-value" style="font-size:12px;">736 Meridian Road N.E, Calgary, CA</span>
                    </div>
                </div>

                <!-- AUD Account -->
                <div class="premium-bank-card">
                    <div class="bank-card-header">
                        <div class="bank-card-flag">🇦🇺</div>
                        <div>
                            <div class="bank-card-title">AUD Account</div>
                            <div class="bank-card-subtitle">BC Payments Australia Pty Ltd</div>
                        </div>
                    </div>
                    <div class="bank-card-details">
                        <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                        <span class="bank-card-label">Account No:</span> <span class="bank-card-value">048040138</span><br>
                        <span class="bank-card-label">BSB Code:</span> <span class="bank-card-value">252000</span><br>
                        <span class="bank-card-label">Address:</span> <span class="bank-card-value" style="font-size:12px;">Level 11/10 Carrington St, Sydney, AU</span>
                    </div>
                </div>

                <!-- DKK Account -->
                <div class="premium-bank-card">
                    <div class="bank-card-header">
                        <div class="bank-card-flag">🇩🇰</div>
                        <div>
                            <div class="bank-card-title">DKK Account</div>
                            <div class="bank-card-subtitle">Banking Circle Denmark</div>
                        </div>
                    </div>
                    <div class="bank-card-details">
                        <span class="bank-card-label">Holder Name:</span> <span class="bank-card-value">APD GLOBAL TRADE</span><br>
                        <span class="bank-card-label">Account No:</span> <span class="bank-card-value">DK6189000048040137</span><br>
                        <span class="bank-card-label">BIC/SWIFT:</span> <span class="bank-card-value">SXPYDKKK</span><br>
                        <span class="bank-card-label">Address:</span> <span class="bank-card-value" style="font-size:12px;">Lautrupsgade 13-15, 2100 Copenhagen, DK</span>
                    </div>
                </div>

            </div>
            
            <div style="text-align: center; margin-top: 40px; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.1); position: relative; z-index: 10;">
                <p style="color: #94a3b8; font-size: 15px; margin-bottom: 20px;">After initiating the wire transfer, please share the payment receipt with our finance team.</p>
                <a href="https://wa.me/919266418868?text=Hello,%20I%20have%20initiated%20a%20direct%20bank%20transfer%20for%20my%20APD%20Global%20Trade%20Membership.%20Attached%20is%20my%20receipt." target="_blank" style="background: #10b981; color: #fff; padding: 14px 28px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 15px; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 15px rgba(16,185,129,0.3); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
                    Submit Transfer Receipt
                </a>
            </div>
        </div>
"""

if start_idx != -1 and end_idx != -1:
    m_html = m_html[:start_idx] + new_bank_details + '\n        ' + m_html[end_idx:]
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(m_html)
    print('Successfully updated membership.html')
else:
    print('Could not find boundaries in membership.html')
