repo = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"
membership_path = repo + r"\membership.html"

with open(membership_path, "r", encoding="utf-8") as f:
    content = f.read()

# The Nexus card + Enterprise Matrix + Form HTML to insert
NEXUS_BLOCK = """
    <!-- ============================================================ -->
    <!-- APD GLOBAL TRADE NEXUS™ — ULTRA-PREMIUM SOVEREIGN PASS -->
    <!-- ============================================================ -->
    <style>
    @keyframes nexusGoldGlow {
        0%   { border-color: #d97706; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5), 0 0 20px rgba(217,119,6,0.25); }
        50%  { border-color: #fbbf24; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5), 0 0 40px rgba(251,191,36,0.5); }
        100% { border-color: #d97706; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5), 0 0 20px rgba(217,119,6,0.25); }
    }
    .apd-nexus-card-active {
        animation: nexusGoldGlow 4s infinite ease-in-out;
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .apd-nexus-card-active:hover { transform: translateY(-4px) scale(1.005); }
    </style>

    <section id="nexus-plan" style="padding: 60px 20px; max-width: 1200px; margin: 0 auto;">
        <!-- Section Header -->
        <div style="text-align: center; margin-bottom: 40px;">
            <span style="background: rgba(217,119,6,0.15); color: #fbbf24; padding: 6px 20px; border-radius: 30px; font-size: 0.75rem; font-weight: 800; border: 1px solid rgba(217,119,6,0.4); text-transform: uppercase; letter-spacing: 2px;">ULTRA-PREMIUM TIER</span>
            <h2 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 700; margin: 15px 0 10px;">The APD Global Trade Nexus™</h2>
            <p style="color: #94a3b8; font-size: 15px; max-width: 650px; margin: 0 auto;">Engineered exclusively for trading houses & institutional brokers who simultaneously buy, source, and export across global markets.</p>
        </div>

        <!-- NEXUS CARD -->
        <div class="apd-nexus-card-active" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 2px solid #d97706; border-radius: 24px; padding: 40px; position: relative; overflow: hidden; margin-bottom: 50px;">
            <!-- Decorative glow orb -->
            <div style="position: absolute; top: -60px; right: -60px; width: 220px; height: 220px; background: radial-gradient(circle, rgba(217,119,6,0.15) 0%, transparent 70%); border-radius: 50%; pointer-events: none;"></div>
            <div style="position: absolute; bottom: -60px; left: -60px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(251,191,36,0.1) 0%, transparent 70%); border-radius: 50%; pointer-events: none;"></div>

            <!-- Tier badge + Price -->
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start; gap: 25px; margin-bottom: 35px;">
                <div>
                    <div style="display: inline-block; background: linear-gradient(90deg, #d97706, #f59e0b); color: #fff; font-size: 11px; font-weight: 800; padding: 6px 18px; border-radius: 30px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">Dual-Network Institutional Tier</div>
                    <h3 style="font-size: 30px; color: #fff; margin: 0 0 8px 0; font-weight: 800; letter-spacing: -0.5px;">APD Global Trade Nexus™</h3>
                    <p style="color: #94a3b8; font-size: 15px; margin: 0; max-width: 600px;">The omni-directional sovereign pass for enterprises that operate on both sides of the global trade corridor simultaneously.</p>
                </div>
                <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); padding: 20px 28px; border-radius: 16px; text-align: right; min-width: 210px; flex-shrink: 0;">
                    <div style="font-size: 38px; font-weight: 900; color: #fbbf24; line-height: 1;">$4,999 <span style="font-size: 16px; color: #94a3b8; font-weight: 400;">/ Year</span></div>
                    <div style="font-size: 22px; font-weight: 700; color: #e2e8f0; margin-top: 6px;">₹4,50,000 <span style="font-size: 12px; color: #94a3b8; font-weight: 400;">INR</span></div>
                    <div style="color: #34d399; font-size: 11px; font-weight: 700; margin-top: 8px; text-transform: uppercase; letter-spacing: 0.5px;">● Full Sovereign Execution Active</div>
                </div>
            </div>

            <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.08); margin-bottom: 35px;">

            <!-- 3-column features -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 30px; margin-bottom: 40px;">
                <div>
                    <h4 style="color: #fbbf24; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 15px 0; display: flex; align-items: center; gap: 8px;">📥 Sovereign Sourcing Power</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; font-size: 14px; color: #cbd5e1; line-height: 2.2;">
                        <li>✅ APD Institutional Verified Buyer Status</li>
                        <li>✅ KYC Access to 4,200+ Elite Exporters</li>
                        <li>✅ Top-Priority Multi-RFQ Broadcast</li>
                        <li>✅ Bank Reference Escrow Screening</li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #fbbf24; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 15px 0; display: flex; align-items: center; gap: 8px;">📤 Global Export Acceleration</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; font-size: 14px; color: #cbd5e1; line-height: 2.2;">
                        <li>✅ Unlimited RFQ Bidding — All Tenders</li>
                        <li>✅ Verified Gold Seller Badge</li>
                        <li>✅ EU, GCC & ASEAN Buyer Pipeline</li>
                        <li>✅ Pre-Shipment Compliance Support</li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #34d399; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 15px 0; display: flex; align-items: center; gap: 8px;">🛡 Elite Macro-Intelligence</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; font-size: 14px; color: #cbd5e1; line-height: 2.2;">
                        <li>✅ Custom WhatsApp Volatility Alerts</li>
                        <li>✅ 1-on-1 Dedicated Trade Director</li>
                        <li>✅ UN/CEFACT Compliance Routing</li>
                        <li>✅ Multi-Language Deal Negotiation</li>
                    </ul>
                </div>
            </div>

            <!-- CTA -->
            <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 20px; background: rgba(255,255,255,0.03); padding: 20px 28px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.06);">
                <div style="color: #94a3b8; font-size: 13px; max-width: 550px;">
                    ⚠️ <strong style="color: #e2e8f0;">Verification Notice:</strong> All Nexus tier applicants must clear our mandatory AML, background, and international company register checks before activation.
                </div>
                <a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20APD%20Global%20Trade%20Nexus%20Sovereign%20Pass%20at%20%244%2C999%2FYear.%20Please%20initiate%20my%20verification." target="_blank" style="background: #fff; color: #0f172a; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; white-space: nowrap; transition: transform 0.2s; box-shadow: 0 4px 20px rgba(255,255,255,0.15);">Apply for Nexus Pass →</a>
            </div>
        </div>

        <!-- ENTERPRISE BESPOKE MATRIX (shown inside a separate clean box) -->
        <div style="background: #0f172a; border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; padding: 40px; margin-bottom: 50px;">
            <div style="text-align: center; margin-bottom: 30px;">
                <span style="background: rgba(212,175,55,0.1); color: #facc15; padding: 5px 15px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">4th Tier — Custom Enterprise</span>
                <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 12px 0 8px; font-family: 'Playfair Display', serif;">Bespoke Enterprise Pricing Matrix</h3>
                <p style="color: #94a3b8; font-size: 14px; margin: 0;">For large conglomerates & bulk exporters. Pricing is mapped to your annual trade volume and container capacity.</p>
            </div>
            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; font-size: 14px; min-width: 500px;">
                    <thead>
                        <tr style="background: rgba(212,175,55,0.1); border-bottom: 1px solid rgba(212,175,55,0.3);">
                            <th style="padding: 14px 20px; text-align: left; color: #facc15; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Annual Turnover</th>
                            <th style="padding: 14px 20px; text-align: left; color: #facc15; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Containers / Year</th>
                            <th style="padding: 14px 20px; text-align: left; color: #facc15; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Custom Annual Fee</th>
                            <th style="padding: 14px 20px; text-align: left; color: #facc15; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <td style="padding: 16px 20px; color: #e2e8f0;">₹5 Cr – ₹20 Cr <span style="color: #94a3b8; font-size: 12px;">($600K – $2.5M)</span></td>
                            <td style="padding: 16px 20px; color: #94a3b8;">10 – 50 Containers</td>
                            <td style="padding: 16px 20px; color: #4ade80; font-weight: 700;">₹1,50,000 / $1,800</td>
                            <td style="padding: 16px 20px;"><a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%205-20%20Crore." target="_blank" style="color: #facc15; text-decoration: none; font-weight: 700; font-size: 13px;">Request Quote →</a></td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(255,255,255,0.02);">
                            <td style="padding: 16px 20px; color: #e2e8f0;">₹20 Cr – ₹100 Cr <span style="color: #94a3b8; font-size: 12px;">($2.5M – $12M)</span></td>
                            <td style="padding: 16px 20px; color: #94a3b8;">50 – 200 Containers</td>
                            <td style="padding: 16px 20px; color: #fbbf24; font-weight: 700;">₹3,50,000 / $4,200</td>
                            <td style="padding: 16px 20px;"><a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%2020-100%20Crore." target="_blank" style="color: #facc15; text-decoration: none; font-weight: 700; font-size: 13px;">Request Quote →</a></td>
                        </tr>
                        <tr>
                            <td style="padding: 16px 20px; color: #e2e8f0;">Above ₹100 Cr <span style="color: #94a3b8; font-size: 12px;">($12M+ Conglomerate)</span></td>
                            <td style="padding: 16px 20px; color: #94a3b8;">200+ / Bulk Vessels</td>
                            <td style="padding: 16px 20px; color: #f87171; font-weight: 700;">₹7,00,000+ / $8,500+</td>
                            <td style="padding: 16px 20px;"><a href="https://wa.me/919266418868?text=I%20am%20interested%20in%20the%20Custom%20Enterprise%20Plan.%20My%20turnover%20is%20above%20100%20Crore." target="_blank" style="color: #facc15; text-decoration: none; font-weight: 700; font-size: 13px;">Request Quote →</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- ENTERPRISE QUALIFICATION FORM -->
        <div style="background: #0f172a; border: 2px solid rgba(37,99,235,0.4); border-radius: 20px; padding: 40px; max-width: 700px; margin: 0 auto 60px;">
            <div style="text-align: center; margin-bottom: 28px; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 20px;">
                <span style="color: #60a5fa; font-weight: 800; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: 6px;">Enterprise Solutions Desk</span>
                <h3 style="font-size: 22px; color: #fff; margin: 0; font-weight: 800;">Request Custom Corporate Pricing</h3>
                <p style="color: #94a3b8; font-size: 14px; margin-top: 8px;">Share your trade metrics and we'll generate a bespoke corporate access plan within 24 hours.</p>
            </div>
            <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" style="display: flex; flex-direction: column; gap: 18px;">
                <input type="hidden" name="_subject" value="APD Enterprise Qualification Lead">
                <div>
                    <label style="display: block; font-size: 13px; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">Corporate Email *</label>
                    <input type="email" name="email" required placeholder="name@company.com" style="width: 100%; padding: 12px 14px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; font-size: 14px; color: #fff; box-sizing: border-box; outline: none; transition: border 0.2s;" onfocus="this.style.borderColor='#3b82f6'" onblur="this.style.borderColor='rgba(255,255,255,0.1)'">
                </div>
                <div>
                    <label style="display: block; font-size: 13px; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">WhatsApp Number (with Country Code) *</label>
                    <input type="tel" name="phone" required placeholder="+91 98765 43210" style="width: 100%; padding: 12px 14px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; font-size: 14px; color: #fff; box-sizing: border-box; outline: none; transition: border 0.2s;" onfocus="this.style.borderColor='#3b82f6'" onblur="this.style.borderColor='rgba(255,255,255,0.1)'">
                </div>
                <div>
                    <label style="display: block; font-size: 13px; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">Core Commodities You Trade *</label>
                    <input type="text" name="commodities" required placeholder="e.g., 1121 Basmati Rice, ICUMSA 45 Sugar, Polymers" style="width: 100%; padding: 12px 14px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; font-size: 14px; color: #fff; box-sizing: border-box; outline: none; transition: border 0.2s;" onfocus="this.style.borderColor='#3b82f6'" onblur="this.style.borderColor='rgba(255,255,255,0.1)'">
                </div>
                <div>
                    <label style="display: block; font-size: 13px; font-weight: 700; color: #cbd5e1; margin-bottom: 6px;">Annual Corporate Turnover *</label>
                    <select name="turnover" required style="width: 100%; padding: 12px 14px; background: #1e293b; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; font-size: 14px; color: #fff; box-sizing: border-box; outline: none;">
                        <option value="" disabled selected>Select your turnover scale</option>
                        <option value="Below ₹5 Crores / Under $600K">Below ₹5 Crores (Under $600K USD)</option>
                        <option value="₹5–20 Cr / $600K–$2.5M">₹5 Crores – ₹20 Crores ($600K – $2.5M USD)</option>
                        <option value="₹20–100 Cr / $2.5M–$12M">₹20 Crores – ₹100 Crores ($2.5M – $12M USD)</option>
                        <option value="Above ₹100 Crores / $12M+">Above ₹100 Crores ($12M+ Conglomerate)</option>
                    </select>
                </div>
                <div>
                    <label style="display: block; font-size: 13px; font-weight: 700; color: #cbd5e1; margin-bottom: 10px;">Export Document Status *</label>
                    <div style="display: flex; flex-direction: column; gap: 10px; font-size: 14px; color: #94a3b8;">
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="radio" name="documents" value="Full Suite (IEC, GST, MSME)" required style="accent-color: #3b82f6;"> Full compliance suite (IEC Code, GSTIN, MSME)</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="radio" name="documents" value="Partial - Need Help" style="accent-color: #3b82f6;"> Partial documents (need assistance)</label>
                        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;"><input type="radio" name="documents" value="New Entity" style="accent-color: #3b82f6;"> New entity starting from scratch</label>
                    </div>
                </div>
                <button type="submit" style="width: 100%; margin-top: 8px; background: linear-gradient(135deg, #1d4ed8, #2563eb); color: #fff; border: none; padding: 15px; border-radius: 8px; font-size: 15px; font-weight: 800; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 20px rgba(37,99,235,0.4);" onmouseover="this.style.background='linear-gradient(135deg, #2563eb, #3b82f6)'" onmouseout="this.style.background='linear-gradient(135deg, #1d4ed8, #2563eb)'">
                    Submit for Enterprise Evaluation →
                </button>
                <p style="text-align: center; color: #64748b; font-size: 12px; margin: 0;">We respond to all enterprise queries within 24 business hours via WhatsApp or email.</p>
            </form>
        </div>
    </section>
"""

# Insert AFTER the closing of tab-memberships div (after </div> that closes tab-memberships)
# Find the closing of the plans container
INSERTION_MARKER = '</div>\n    </div>\n\n    <div id="tab-trials"'

if INSERTION_MARKER in content and "APD GLOBAL TRADE NEXUS" not in content:
    content = content.replace(
        INSERTION_MARKER,
        '</div>\n    </div>\n' + NEXUS_BLOCK + '\n    <div id="tab-trials"'
    )
    with open(membership_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Nexus card + Enterprise Matrix + Form added to membership.html!")
elif "APD GLOBAL TRADE NEXUS" in content:
    print("SKIP: Nexus block already exists")
else:
    print("ERROR: Insertion marker not found")
    # Debug: show nearby content
    idx = content.find('tab-trials')
    if idx > 0:
        print("Nearby content:", repr(content[idx-200:idx+50]))
