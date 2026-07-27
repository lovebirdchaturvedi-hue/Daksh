import re

file_path = 'membership.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to grab the 3 MONTH PLAN from where it is right now.
# It is between "Buy 8 Unlocks Now</button>\n    </div>" and "<!-- UNLIMITED PLANS SECTION -->"
# Wait, I just need to move the `</div>` that is immediately BEFORE the `<!-- 3 MONTH PLAN -->` to be immediately AFTER it.

# Current bad structure:
# Buy 8 Unlocks Now</button>
# </div>
# <!-- 3 MONTH PLAN -->
# ...
# </button>
# </div>
# <!-- UNLIMITED PLANS SECTION -->

# New good structure:
# Buy 8 Unlocks Now</button>
# <!-- 3 MONTH PLAN -->
# ...
# </button>
# </div>
# </div>  <-- wait, how many divs are there?
# Let's just do a string replacement.

target_bad = """        <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
    </div>
        
        <!-- 3 MONTH PLAN -->"""

target_good = """        <button class="btn" style="margin-top: auto; background: transparent; border: 2px solid #d4af37; color: #d4af37; margin-bottom: 15px;" onclick="initiatePayment('8 Verified Buyers', 100, 1999)">Buy 8 Unlocks Now</button>
        
        <!-- 3 MONTH PLAN -->"""

html = html.replace(target_bad, target_good)

# And then I need to insert a `</div>` after the 3 month plan block.
# The 3 month plan block ends with:
target_end_bad = """            <button class="btn" style="margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('Growth Program (3 Months)', 249, 19999)">Get 3 Months Growth Access</button>
        </div>

    <!-- UNLIMITED PLANS SECTION -->"""

target_end_good = """            <button class="btn" style="margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;" onclick="initiatePayment('Growth Program (3 Months)', 249, 19999)">Get 3 Months Growth Access</button>
        </div>
    </div>

    <!-- UNLIMITED PLANS SECTION -->"""

html = html.replace(target_end_bad, target_end_good)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed position")
