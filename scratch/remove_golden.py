import re

membership_file = 'membership.html'
with open(membership_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Special Golden Plan
start = content.find('<!-- SPECIAL GOLDEN PLAN -->')
if start != -1:
    # Find the end of this div. 
    # The structure is: <div class="plan" ...> ... </div>
    # It's followed by </div> (which closes the .plans container)
    end_marker = "</div>\n    </div>\n\n    <!-- ============================================================ -->"
    end = content.find('<!-- ============================================================ -->\n    <!-- APD GLOBAL TRADE NEXUS™', start)
    if end != -1:
        # We need to preserve the closing </div> for the .plans container
        # Let's just find the closing </div> of the SPECIAL GOLDEN PLAN
        # It's before the Nexus block. Let's find the closing </div>\n        </div>
        # Actually, let's use regex to remove the specific block.
        pattern = r'<!-- SPECIAL GOLDEN PLAN -->.*?Get Custom Quote</button>\n            </div>'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        with open(membership_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Special Golden Plan removed.")
    else:
        print("End marker not found for Golden Plan.")
