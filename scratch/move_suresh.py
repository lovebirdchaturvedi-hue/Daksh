import sys
sys.stdout.reconfigure(encoding='utf-8')

SURESH_BLOCK = """
              <!-- 2. Spice Exporter (Indian Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial 3  Spice - Same face which was in Rice.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Suresh Patel</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Managing Director, Spices Unlimited</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Spice Exporter</span>
                  </div>
              </div>
"""

# The exact block to remove (including the comment and trailing newline)
REMOVE_BLOCK = """\r\n              <!-- 2. Spice Exporter (Indian Male) -->\r\n              <div style=\"background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);\">\r\n                  <div style=\"position: relative; width: 100%; padding-bottom: 56.25%; background: #000;\">\r\n                      <video controls playsinline webkit-playsinline preload=\"metadata\" style=\"position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;\">\r\n                          <source src=\"/assets/videos/Tesimonial 3  Spice - Same face which was in Rice.mp4\" type=\"video/mp4\">\r\n                      </video>\r\n                  </div>\r\n                  <div style=\"padding: 16px;\">\r\n                      <h4 style=\"color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;\">\r\n                          <span>Suresh Patel</span> <span style=\"font-size: 14px;\">🇮🇳</span>\r\n                      </h4>\r\n                      <p style=\"color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;\">Managing Director, Spices Unlimited</p>\r\n                      <span style=\"font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;\">Verified Spice Exporter</span>\r\n                  </div>\r\n              </div>\r\n"""

# What to insert at the end — right before closing </div></div></section>
# We'll find the last </div> before </section> in the testimonials grid
LAST_CARD_END_INDEX = "<!-- 2. Spice Exporter (Indian Male) -->"
LAST_CARD_ALT = "Suresh Patel"

for fname in ['index.html', 'membership.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    if LAST_CARD_ALT not in content:
        print(f"SKIP {fname}: Suresh Patel not found")
        continue

    # Step 1: Remove Suresh Patel block from current position
    if REMOVE_BLOCK in content:
        content = content.replace(REMOVE_BLOCK, "\r\n", 1)
        print(f"{fname}: Removed Suresh Patel from position 2")
    else:
        print(f"WARNING {fname}: Could not find exact REMOVE_BLOCK, trying manual approach")
        # Try to find and remove it line by line
        lines = content.splitlines(keepends=True)
        suresh_start = None
        suresh_end = None
        for i, line in enumerate(lines):
            if '<!-- 2. Spice Exporter (Indian Male) -->' in line:
                suresh_start = i
            if suresh_start is not None and i > suresh_start and '</div>' in line and suresh_end is None:
                # Count nested divs to find the right closing div
                pass
        # Simpler: find the block between the comment and the blank line after it
        import re
        pattern = r'\r?\n\s*<!-- 2\. Spice Exporter \(Indian Male\) -->.*?</div>\r?\n\s*</div>\r?\n'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content[:match.start()] + '\r\n' + content[match.end():]
            print(f"{fname}: Removed via regex")
        else:
            print(f"ERROR {fname}: Could not remove block")
            continue

    # Step 2: Find the closing tag of the testimonials grid div to insert Suresh at end
    # The grid div ends with multiple </div> - find the one before </section>
    # Look for the pattern: last testimonial card closing </div>\n\n        </div> (grid close)
    # We'll insert before the grid-closing </div>
    
    # Find "<!-- HIGHLIGHTED GLOBAL CLIENT" section area  
    # Strategy: find the last </div> that closes a testimonial card before </div></section>
    # Insert our block just before the second-to-last </div>

    # Reliable: find where we removed the block and count to find the grid close
    # Better: search for a unique marker near the end of the grid
    # The grid close is followed by </div> and then </section>
    
    # Insert before: "        </div>\n      </div>\n    </section>" pattern
    # Let's use the closing </div>\n\n        </div>\n      </div>\n    </section> near testimonials

    SURESH_APPEND = """\r\n              <!-- Suresh Patel — moved to last -->\r\n              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">\r\n                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">\r\n                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">\r\n                          <source src="/assets/videos/Tesimonial 3  Spice - Same face which was in Rice.mp4" type="video/mp4">\r\n                      </video>\r\n                  </div>\r\n                  <div style="padding: 16px;">\r\n                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">\r\n                          <span>Suresh Patel</span> <span style="font-size: 14px;">🇮🇳</span>\r\n                      </h4>\r\n                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Managing Director, Spices Unlimited</p>\r\n                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Spice Exporter</span>\r\n                  </div>\r\n              </div>\r\n"""

    # Find the closing of the testimonial grid — the </div> that closes the grid container
    # In index.html it's: "          </div>\r\n      </div>\r\n  </section>"
    # In membership.html: "          </div>\r\n          </div>\r\n      </section>"
    
    # Most reliable: find the LAST occurrence of the last non-Suresh testimonial name,
    # then find the </div></div> that follows it
    import re
    
    # Find all testimonial card closing patterns and insert after the LAST one
    # Pattern: </div>\r\n              </div>\r\n\r\n (end of a card)
    # Then find what comes AFTER all cards (the grid close)
    
    # Find the section with VERIFIED SUCCESS STORIES
    section_start = content.find('VERIFIED SUCCESS STORIES')
    if section_start == -1:
        section_start = content.find('Global Exporter S')  # membership.html fallback
    
    # Find the grid div within this section
    grid_match = re.search(r'display: grid[^>]*>', content[section_start:section_start+500])
    if not grid_match:
        grid_match = re.search(r'grid-template-columns[^>]*>', content[section_start:section_start+500])
    
    if grid_match:
        grid_pos = section_start + grid_match.end()
        # Find the closing </div> of this grid
        # Count nested divs
        depth = 1
        pos = grid_pos
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
                    # Insert our block BEFORE this closing </div>
                    content = content[:next_close] + SURESH_APPEND + content[next_close:]
                    print(f"{fname}: Appended Suresh Patel at end of grid")
                    break
                pos = next_close + 6
    else:
        print(f"ERROR {fname}: Could not find grid div")

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"SUCCESS {fname}: Suresh Patel moved to last position!")
