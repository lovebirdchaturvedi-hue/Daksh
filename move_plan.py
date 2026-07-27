import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# The block for the 3 MONTH PLAN starts with:
#         <!-- 3 MONTH PLAN -->
#         <div class="plan" style="display: flex; flex-direction: column; background: #111827; border: 1px solid rgba(255,255,255,0.05); padding: 40px; border-radius: 20px; text-align: left; display: flex; flex-direction: column;">
# ...
#             <button class="btn" style="margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('Growth Program (3 Months)', 249, 19999)">Get 3 Months Growth Access</button>
#         </div>

# And it is followed by:
#         <!-- 6 MONTH PLAN -->

# Regex to extract the 3 MONTH PLAN block
pattern = re.compile(r'(\s*<!-- 3 MONTH PLAN -->\s*<div class="plan" style="display: flex; flex-direction: column; background: #111827;.*?Get 3 Months Growth Access</button>\s*</div>\s*)(?=<!-- 6 MONTH PLAN -->)', re.DOTALL)

match = pattern.search(html)
if match:
    block = match.group(1)
    
    # Remove it from its current position
    html = html.replace(block, '\n        ')
    
    # We want to insert it at the end of the FIRST plans div.
    # The first plans div ends with:
    #         <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
    #     </div>
    # 
    #     <!-- UNLIMITED PLANS SECTION -->
    
    insertion_target = '''        <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
    </div>'''
    
    replacement = f'''        <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
    </div>{block}
    </div>'''
    
    html = html.replace(insertion_target, replacement)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Plan moved.")
else:
    print("Could not find the 3 Month Plan block.")
