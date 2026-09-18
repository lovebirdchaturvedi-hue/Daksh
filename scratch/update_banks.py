import re

with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_bank_grid = """
        <div class="bank-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto;">
            
            <!-- SWIFT (Currency Cloud) -->
            <div class="bank-card gold" style="grid-column: 1 / -1; max-width: 800px; margin: 0 auto; width: 100%; text-align: left; padding: 30px; background: rgba(212,175,55,0.05); border: 1px solid var(--gold); border-radius: 15px;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 40px;">🌐</div>
                    <div>
                        <div class="bank-name" style="color: var(--gold); font-size: 24px; font-weight: 800;">Global SWIFT Account</div>
                        <div class="bank-location" style="color: #94a3b8; font-size: 14px;">The Currency Cloud Limited (London, UK)</div>
                    </div>
                </div>
                <div style="background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px; font-family: monospace; font-size: 15px; color: #cbd5e1;">
                    <div style="margin-bottom: 8px;"><span style="color: #64748b; display: inline-block; width: 150px;">Beneficiary:</span> <strong style="color: #fff;">APD GLOBAL TRADE</strong></div>
                    <div style="margin-bottom: 8px;"><span style="color: #64748b; display: inline-block; width: 150px;">Account Number (IBAN):</span> <strong style="color: #fff;">GB82TCCL04143422806894</strong></div>
                    <div style="margin-bottom: 8px;"><span style="color: #64748b; display: inline-block; width: 150px;">SWIFT / BIC:</span> <strong style="color: #fff;">TCCLGB3L</strong></div>
                    <div><span style="color: #64748b; display: inline-block; width: 150px;">Bank Address:</span> 1 Sheldon Square, London, W2 6TT, UK</div>
                </div>
            </div>

            <!-- USD Account -->
            <div class="bank-card" style="text-align: left; padding: 25px; background: #0f172a; border: 1px solid rgba(255,255,255,0.05); border-radius: 15px; transition: 0.3s;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 30px;">🇺🇸</div>
                    <div>
                        <div class="bank-name" style="color: #fff; font-size: 18px; font-weight: 700;">USD Account (ACH)</div>
                        <div class="bank-location" style="color: #64748b; font-size: 13px;">Community Federal Savings Bank, NY</div>
                    </div>
                </div>
                <div style="font-family: monospace; font-size: 14px; color: #cbd5e1;">
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Account:</span> <strong style="color: #fff;">8302840763</strong></div>
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Routing (ACH):</span> <strong style="color: #fff;">026073150</strong></div>
                    <div><span style="color: #64748b;">Beneficiary:</span> APD GLOBAL TRADE</div>
                </div>
            </div>

            <!-- EUR Account -->
            <div class="bank-card" style="text-align: left; padding: 25px; background: #0f172a; border: 1px solid rgba(255,255,255,0.05); border-radius: 15px; transition: 0.3s;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 30px;">🇪🇺</div>
                    <div>
                        <div class="bank-name" style="color: #fff; font-size: 18px; font-weight: 700;">EUR Account (SEPA)</div>
                        <div class="bank-location" style="color: #64748b; font-size: 13px;">Banking Circle Germany</div>
                    </div>
                </div>
                <div style="font-family: monospace; font-size: 14px; color: #cbd5e1;">
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">IBAN:</span> <strong style="color: #fff;">DE41202208000048040137</strong></div>
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">BIC / SWIFT:</span> <strong style="color: #fff;">SXPYDEHH</strong></div>
                    <div><span style="color: #64748b;">Beneficiary:</span> APD GLOBAL TRADE</div>
                </div>
            </div>

            <!-- GBP Account -->
            <div class="bank-card" style="text-align: left; padding: 25px; background: #0f172a; border: 1px solid rgba(255,255,255,0.05); border-radius: 15px; transition: 0.3s;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 30px;">🇬🇧</div>
                    <div>
                        <div class="bank-name" style="color: #fff; font-size: 18px; font-weight: 700;">GBP Account (FPS)</div>
                        <div class="bank-location" style="color: #64748b; font-size: 13px;">Banking Circle S.A. UK</div>
                    </div>
                </div>
                <div style="font-family: monospace; font-size: 14px; color: #cbd5e1;">
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Account:</span> <strong style="color: #fff;">48040137</strong></div>
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Sort Code:</span> <strong style="color: #fff;">608382</strong></div>
                    <div><span style="color: #64748b;">Beneficiary:</span> APD GLOBAL TRADE</div>
                </div>
            </div>

            <!-- CAD Account -->
            <div class="bank-card" style="text-align: left; padding: 25px; background: #0f172a; border: 1px solid rgba(255,255,255,0.05); border-radius: 15px; transition: 0.3s;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 30px;">🇨🇦</div>
                    <div>
                        <div class="bank-name" style="color: #fff; font-size: 18px; font-weight: 700;">CAD Account (EFT)</div>
                        <div class="bank-location" style="color: #64748b; font-size: 13px;">Digital Commerce Bank, CA</div>
                    </div>
                </div>
                <div style="font-family: monospace; font-size: 14px; color: #cbd5e1;">
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Account:</span> <strong style="color: #fff;">962668612</strong></div>
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Routing:</span> <strong style="color: #fff;">035210009</strong></div>
                    <div><span style="color: #64748b;">Beneficiary:</span> APD GLOBAL TRADE</div>
                </div>
            </div>

            <!-- AUD Account -->
            <div class="bank-card" style="text-align: left; padding: 25px; background: #0f172a; border: 1px solid rgba(255,255,255,0.05); border-radius: 15px; transition: 0.3s;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 30px;">🇦🇺</div>
                    <div>
                        <div class="bank-name" style="color: #fff; font-size: 18px; font-weight: 700;">AUD Account (NPP)</div>
                        <div class="bank-location" style="color: #64748b; font-size: 13px;">BC Payments Australia</div>
                    </div>
                </div>
                <div style="font-family: monospace; font-size: 14px; color: #cbd5e1;">
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Account:</span> <strong style="color: #fff;">048040138</strong></div>
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">BSB Number:</span> <strong style="color: #fff;">252000</strong></div>
                    <div><span style="color: #64748b;">Beneficiary:</span> APD GLOBAL TRADE</div>
                </div>
            </div>

            <!-- DKK Account -->
            <div class="bank-card" style="text-align: left; padding: 25px; background: #0f172a; border: 1px solid rgba(255,255,255,0.05); border-radius: 15px; transition: 0.3s;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div class="bank-currency" style="font-size: 30px;">🇩🇰</div>
                    <div>
                        <div class="bank-name" style="color: #fff; font-size: 18px; font-weight: 700;">DKK Account (Local)</div>
                        <div class="bank-location" style="color: #64748b; font-size: 13px;">Banking Circle Denmark</div>
                    </div>
                </div>
                <div style="font-family: monospace; font-size: 14px; color: #cbd5e1;">
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">Account:</span> <strong style="color: #fff;">DK6189000048040137</strong></div>
                    <div style="margin-bottom: 5px;"><span style="color: #64748b;">BIC / SWIFT:</span> <strong style="color: #fff;">SXPYDKKK</strong></div>
                    <div><span style="color: #64748b;">Beneficiary:</span> APD GLOBAL TRADE</div>
                </div>
            </div>
            
        </div>
"""

# Replace the old bank grid with the new detailed one
html = re.sub(r'<div class="bank-grid">.*?</div>\s*</section>', new_bank_grid + '\n    </section>', html, flags=re.DOTALL)

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated membership.html with actual bank details!")
