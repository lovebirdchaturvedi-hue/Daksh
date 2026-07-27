import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I need to insert a `</div>` after the 8 Unlocks Plan's button.
# And I need to verify how many `</div>` are at the end of the 3 Month Plan.

target_8_unlock_button = """        <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
        
        <!-- 3 MONTH PLAN -->"""
        
replacement_8_unlock = """        <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
      </div>
        
        <!-- 3 MONTH PLAN -->"""

html = html.replace(target_8_unlock_button, replacement_8_unlock)

# Now, let's look at the end of 3 Month Plan.
# It should end with its own `</div>`, AND THEN the `.plans` container should close with another `</div>`.
target_3_month_end = """            <button class="btn" style="margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('Growth Program (3 Months)', 249, 19999)">Get 3 Months Growth Access</button>
        </div>
    </div>

    <!-- UNLIMITED PLANS SECTION -->"""

# Currently, in the file it is:
#         </div>
#         
#     </div>
#
#     <!-- UNLIMITED PLANS SECTION -->

# Actually, I'll just use Regex to perfectly format the area between "Get 3 Months Growth Access" and "Unlimited Access Plans".
# We want exactly TWO `</div>`s there. One for the 3 Month Plan, one for the `.plans` container.
html = re.sub(r'Get 3 Months Growth Access</button>\s*</div>\s*</div>\s*<!-- UNLIMITED PLANS SECTION -->',
              r'Get 3 Months Growth Access</button>\n        </div>\n    </div>\n\n    <!-- UNLIMITED PLANS SECTION -->', html)
              
# Wait, if there are extra divs, let's just make sure.
# Let me write it back.
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Repaired structure.")
