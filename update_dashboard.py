import os
import re

def update_dashboard():
    with open('supplier-dashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Timer script
    if 'startMidnightCountdown()' not in html:
        timer_script = '''
  <script>
    function startMidnightCountdown() {
        setInterval(() => {
            const now = new Date();
            const tomorrow = new Date(now);
            tomorrow.setHours(24, 0, 0, 0);
            const diff = tomorrow - now;
            
            const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((diff % (1000 * 60)) / 1000);
            
            const timeStr = `${h.toString().padStart(2, '0')}h : ${m.toString().padStart(2, '0')}m : ${s.toString().padStart(2, '0')}s`;
            
            document.querySelectorAll('.countdown-timer').forEach(el => {
                el.innerText = timeStr;
            });
        }, 1000);
    }
    startMidnightCountdown();
  </script>
</body>
'''
        html = html.replace('</body>', timer_script)

    # 2. Modify the card generation
    # Find `container.appendChild(card);`
    # Replace it with the new upgrade HTML appended to `card.innerHTML`
    pattern_card = r"(\s+</div>\n\s+`;\n\s+container\.appendChild\(card\);)"
    if re.search(pattern_card, html) and 'id="upgrade-section-' not in html:
        upgrade_html = '''</div>
            <div id="upgrade-section-${lead.id}" style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #e2e8f0; width: 100%; text-align: center; display: ${(freeCredits === 0 || (supplierData && supplierData.lastFreeUnlockDate === new Date().toISOString().split('T')[0])) ? 'block' : 'none'};">
                <div id="timer-container-${lead.id}" style="color: #ea580c; font-weight: 700; margin-bottom: 10px; font-size: 13px; display: ${(freeCredits > 0 && supplierData && supplierData.lastFreeUnlockDate === new Date().toISOString().split('T')[0]) ? 'block' : 'none'};">
                    ⏳ Next free unlock in <span class="countdown-timer">--h : --m : --s</span>
                </div>
                <a href="/membership.html" style="display: block; width: 100%; background: #0f172a; color: #facc15; text-align: center; padding: 10px; border-radius: 6px; font-weight: 800; text-decoration: none; font-size: 14px; border: 1px solid #facc15; box-shadow: 0 4px 10px rgba(250, 204, 21, 0.2);">
                    ⭐ Get Unlimited Instant Unlocks — Upgrade Now
                </a>
            </div>
        `;
        container.appendChild(card);'''
        html = re.sub(pattern_card, upgrade_html, html)
        print("Injected Upgrade HTML into cards.")

    # 3. Dynamic unlock logic
    pattern_unlock_success = r"(// Update badge\s+const badge = document\.getElementById\('creditBadge'\);)"
    if re.search(pattern_unlock_success, html) and 'const upgSec = document.getElementById' not in html:
        inject_dynamic_show = '''
                // Show countdown and upgrade buttons on all other locked cards
                leads.forEach(l => {
                    if (l.id !== lead.id) {
                        const upgSec = document.getElementById(`upgrade-section-${l.id}`);
                        const timerCont = document.getElementById(`timer-container-${l.id}`);
                        if (upgSec) upgSec.style.display = 'block';
                        if (timerCont && freeCredits > 0) timerCont.style.display = 'block';
                        if (timerCont && freeCredits === 0) timerCont.style.display = 'none';
                    }
                });

                // Update badge
                const badge = document.getElementById('creditBadge');'''
        html = re.sub(pattern_unlock_success, inject_dynamic_show.replace('\\', '\\\\'), html)
        print("Injected dynamic unlock logic.")

    pattern_reveal = r"(blurDiv\.querySelector\('span'\)\.innerText = '.*UNLOCKED.*';)"
    if re.search(pattern_reveal, html) and 'const thisUpg = document.getElementById' not in html:
        def replace_reveal(m):
            return m.group(1) + '''
                const thisUpg = document.getElementById(`upgrade-section-${lead.id}`);
                if(thisUpg) thisUpg.style.display = 'none';
'''
        html = re.sub(pattern_reveal, replace_reveal, html)
        print("Injected hide unlocked logic.")

    with open('supplier-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_dashboard()
