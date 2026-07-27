import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

vanta_scripts = """
  <!-- 3D ULTRA-PREMIUM VANTA GLOBE JS -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.globe.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function() {
        if(document.getElementById("globe-container")) {
            VANTA.GLOBE({
              el: "#globe-container",
              mouseControls: true,
              touchControls: true,
              gyroControls: false,
              minHeight: 200.00,
              minWidth: 200.00,
              scale: 1.00,
              scaleMobile: 1.00,
              color: 0xc9a44a,       /* APD Gold */
              color2: 0x0b1d36,      /* Deep Navy Accent */
              size: 0.80,
              backgroundColor: 0x020617 /* Deep Obsidian Background */
            });
        }
    });
  </script>
"""

# Check if Vanta is already injected to avoid duplicates
if "vanta.globe.min.js" not in index_html:
    index_html = index_html.replace('</body>', vanta_scripts + '\n</body>')

# Also, let's ensure the #globe-container has the correct CSS to show up.
# Currently premium.css has:
# #globe-container { position: absolute; top: 0; left: 0; width: 100% !important; height: 100% !important; z-index: 2; opacity: 0.9; }
# This is perfect.

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
