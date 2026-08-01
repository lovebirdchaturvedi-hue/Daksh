import os, re

membership_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"

with open(membership_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix extra closing tags after 14th testimonial section
target_block = """              <!-- 14. Testimonial (Arab Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Testimonial.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Hassan Al-Zahrani</span> <span style="font-size: 14px;">🇸🇦</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Food Logistics Partner, Saudi Arabia</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified KSA Buyer</span>
                  </div>
              </div>

          </div>
      </div>
  </section>"""

# Replace any malformed trailing section end with clean block
if target_block in content:
    # Find what follows target_block up to Official Business Identity
    parts = content.split(target_block)
    identity_start = "<!-- OFFICIAL BUSINESS IDENTITY SECTION -->"
    if identity_start in parts[1]:
        clean_after = "\n\n" + identity_start + parts[1].split(identity_start)[1]
        content = parts[0] + target_block + clean_after
        with open(membership_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Cleaned up trailing section tags!")
