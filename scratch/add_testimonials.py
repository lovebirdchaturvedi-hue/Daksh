import sys

NEW_TESTIMONIALS = """
              <!-- 1. Kouamé Diaby -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000; overflow: hidden;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; transform: scale(1.15);">
                          <source src="/assets/videos/Testimonial Franch.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Kouamé Diaby</span> <span style="font-size: 14px;">🇨🇮</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Cocoa & Cashew Exporter</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Cocoa Exporter</span>
                  </div>
              </div>

              <!-- 2. Li Na -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000; overflow: hidden;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; transform: scale(1.15);">
                          <source src="/assets/videos/Testimonial Chiienese.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Li Na (李娜)</span> <span style="font-size: 14px;">🇨🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Garlic & Ginger Export Manager</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Garlic Exporter</span>
                  </div>
              </div>

              <!-- 3. Muhammad Ibrahim -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000; overflow: hidden;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; transform: scale(1.15);">
                          <source src="/assets/videos/Testimonial Nigeria.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Muhammad Ibrahim</span> <span style="font-size: 14px;">🇳🇬</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Sesame & Soybean Exporter</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Sesame Exporter</span>
                  </div>
              </div>

              <!-- 4. Pinkesh Patel -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000; overflow: hidden;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; transform: scale(1.15);">
                          <source src="/assets/videos/Gujrati Testimonial.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Pinkesh Patel</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Cumin Seeds, Coriander & more</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Spices Exporter</span>
                  </div>
              </div>
"""

for fname in ['index.html', 'membership.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to insert this right after the opening div of the grid
    # In index.html: <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;">
    grid_start_pattern = 'grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;">'
    pos = content.find(grid_start_pattern)
    if pos != -1:
        insert_pos = pos + len(grid_start_pattern)
        content = content[:insert_pos] + "\n" + NEW_TESTIMONIALS + content[insert_pos:]
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESS: Added 4 testimonials to {fname}")
    else:
        print(f"Grid start not found in {fname}")
