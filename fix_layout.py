import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I need to find the `<div class="plans" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">` 
# that is immediately before the blinking link, and remove it, along with its closing tag (if it exists, but it probably doesn't exist anymore because my previous replacement wiped out the rest of the structure!)

# Wait, if I remove the opening tag at line 497, I must also make sure that I close the `div` containing the blinking link if it's not closed.
# Let's see:
target_to_replace = """    <div class="plans" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">

        <div style="text-align: center; margin-bottom: 50px; grid-column: 1 / -1;">
            <a href="#unlimited-plans" class="blinking-link" style="font-size: 22px; font-weight: 800; color: #dc2626; text-decoration: underline; background: #fee2e2; padding: 10px 20px; border-radius: 8px; border: 2px solid #dc2626;">🔥 Get Unlimited Buyers Access in 6/12 Months Plan! 🔥</a>
            <style>
                @keyframes blink {
                    0% { opacity: 1; }
                    50% { opacity: 0.3; transform: scale(1.05); }
                    100% { opacity: 1; }
                }
                .blinking-link {
                    display: inline-block;
                    animation: blink 1.5s infinite;
                    transition: all 0.3s;
                }
                .blinking-link:hover {
                    color: #991b1b;
                    border-color: #991b1b;
                    background: #fecaca;
                }
            </style>
        </div>"""

replacement = """
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="#unlimited-plans" class="blinking-link" style="font-size: 22px; font-weight: 800; color: #dc2626; text-decoration: underline; background: #fee2e2; padding: 10px 20px; border-radius: 8px; border: 2px solid #dc2626;">🔥 Get Unlimited Buyers Access in 6/12 Months Plan! 🔥</a>
            <style>
                @keyframes blink {
                    0% { opacity: 1; }
                    50% { opacity: 0.3; transform: scale(1.05); }
                    100% { opacity: 1; }
                }
                .blinking-link {
                    display: inline-block;
                    animation: blink 1.5s infinite;
                    transition: all 0.3s;
                }
                .blinking-link:hover {
                    color: #991b1b;
                    border-color: #991b1b;
                    background: #fecaca;
                }
            </style>
        </div>"""
        
# Actually, wait. Looking at the user's latest requirement, they might not even need the blinking link anymore because the plans are side-by-side in tabs!
# But let's keep it just in case, but remove the outer `<div class="plans">` and the `grid-column: 1 / -1;`.
        
if target_to_replace in html:
    html = html.replace(target_to_replace, replacement)
    
    # Also I should check if there's any stray closing `</div>` that belongs to the now-removed `.plans`.
    # Since my previous regex replaced everything from `<!-- 1 UNLOCK PLAN -->` onwards, it probably means there is NO stray `</div>` because I replaced everything up to the `</div>` closing the old `.plans`!
    # Yes, in my `restructure.py`:
    # `start_replace = html.find('<!-- 1 UNLOCK PLAN -->')`
    # `end_replace = html.find('</div>', html.find('Get 12 Months Enterprise Access</button>')) + 6`
    # `end_replace = html.find('</div>', end_replace) + 6 # close the plans div`
    # Because of this, the `</div>` that was supposed to close the line 497 `.plans` was REMOVED by `restructure.py`.
    # And the OPENING tag `<div class="plans">` at 497 was LEFT BEHIND!
    # Which caused everything below it to become grid items of that `.plans` grid!
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed layout bug")
else:
    print("Target not found. Let me try regex.")
    
