import sys, re
sys.stdout.reconfigure(encoding='utf-8')

SURESH_CARD = """\r\n              <!-- Suresh Patel — Spice Exporter (moved to last) -->\r\n              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">\r\n                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">\r\n                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">\r\n                          <source src="/assets/videos/Tesimonial 3  Spice - Same face which was in Rice.mp4" type="video/mp4">\r\n                      </video>\r\n                  </div>\r\n                  <div style="padding: 16px;">\r\n                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">\r\n                          <span>Suresh Patel</span> <span style="font-size: 14px;">🇮🇳</span>\r\n                      </h4>\r\n                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Managing Director, Spices Unlimited</p>\r\n                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Spice Exporter</span>\r\n                  </div>\r\n              </div>\r\n"""

# For index.html — insert before the Arab Male (Testimonial 4 Gulf Male) comment
# which is now card #11 in the grid (after Suresh was removed from card #2)
# Best approach: append right before the CLOSING of the testimonial grid div

for fname in ['index.html', 'membership.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'Suresh Patel' in content:
        print(f'SKIP {fname}: Suresh already exists')
        continue

    # Find the last testimonial card in the grid and insert after it
    # Unique markers: the last </div>\r\n before the grid closes
    # In index.html the grid is inside VERIFIED SUCCESS STORIES section
    # In membership.html same

    # Strategy: find "<!-- 11." or last card comment, then insert after its card block
    # Safer: find all card closing patterns and insert before the grid's outer </div>

    # Find the testimonials grid opening
    marker_index = content.find('VERIFIED SUCCESS STORIES')
    if marker_index == -1:
        marker_index = content.find('Global Exporter S')
    if marker_index == -1:
        print(f'ERROR {fname}: cannot find testimonials section')
        continue

    # Find the grid div (display: grid) after the marker
    grid_open = content.find('display: grid', marker_index)
    if grid_open == -1:
        print(f'ERROR {fname}: grid not found')
        continue

    # Find the ">" that closes the opening grid div tag
    grid_tag_end = content.find('>', grid_open)

    # Now walk forward counting divs to find the matching close
    depth = 1
    pos = grid_tag_end + 1
    grid_close_pos = -1
    while pos < len(content) and depth > 0:
        next_open = content.find('<div', pos)
        next_close = content.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                grid_close_pos = next_close
            pos = next_close + 6

    if grid_close_pos == -1:
        print(f'ERROR {fname}: could not find grid closing div')
        continue

    # Insert Suresh card RIGHT BEFORE the grid closing </div>
    content = content[:grid_close_pos] + SURESH_CARD + content[grid_close_pos:]
    print(f'SUCCESS {fname}: Suresh Patel added at last position (before grid close at pos {grid_close_pos})')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done!')
