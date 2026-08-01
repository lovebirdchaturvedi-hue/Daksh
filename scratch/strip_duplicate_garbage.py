import os

membership_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"

with open(membership_path, "r", encoding="utf-8") as f:
    content = f.read()

# Marker 1: End of Testimonials section
t_end_marker = "<!-- 14. Testimonial (Arab Male) -->"
# Marker 2: Official Business Identity Section title
identity_marker = 'Official Business Identity & Registrations</h2>'

if t_end_marker in content and identity_marker in content:
    # Get part 1 up to end of 14th testimonial section block
    part1_split = content.split(t_end_marker)[1]
    sub_section_end = part1_split.split("</section>")[0] + "</section>\n      </div>\n  </section>\n"
    
    part1 = content.split(t_end_marker)[0] + t_end_marker + sub_section_end
    
    # Get part 2 starting from Official Business Identity Section
    part2 = '<!-- OFFICIAL BUSINESS IDENTITY SECTION -->\n  <section style="background: #0f172a; border-top: 1px solid rgba(212, 175, 55, 0.2); border-bottom: 1px solid rgba(212, 175, 55, 0.2); padding: 40px 20px;">\n    <div class="container" style="max-width: 1200px; margin: 0 auto;">\n          <h2 style="text-align: center; color: var(--gold); font-family: \'Playfair Display\', serif; font-size: 26px; margin-bottom: 30px;">' + content.split(identity_marker)[1]
    
    clean_membership = part1 + "\n\n" + part2
    
    with open(membership_path, "w", encoding="utf-8") as f:
        f.write(clean_membership)
    print("SUCCESS: Stripped all duplicate broken sections from membership.html!")
else:
    print("ERROR: Markers not found!")
