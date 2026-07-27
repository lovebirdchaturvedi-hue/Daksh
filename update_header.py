import os
import re

def update_header():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Make header sticky
    target_header = '<header>'
    replacement_header = '<header id="main-header" style="position: sticky; top: 0; z-index: 10000; background: #020617; transition: all 0.3s ease;">'
    if target_header in html:
        html = html.replace(target_header, replacement_header, 1)

    # Insert mini search bar inside nav, hidden by default
    nav_end = '</nav>'
    mini_search = '''
      <!-- MINI SEARCH BAR (Shown on scroll via JS) -->
      <div id="mini-search" class="desktop-only" style="display: none; align-items: center; background: rgba(255,255,255,0.05); border: 1px solid rgba(212,175,55,0.3); border-radius: 30px; overflow: hidden; margin-left: 20px; transition: all 0.3s ease;">
          <input type="text" placeholder="Search commodities..." style="background: transparent; border: none; color: #fff; padding: 8px 15px; font-size: 0.85rem; outline: none; width: 200px;">
          <button style="background: var(--gold); border: none; padding: 8px 15px; cursor: pointer; font-weight: 800; font-size: 0.85rem; color: #000;">🔎</button>
      </div>
    </nav>
    '''
    if nav_end in html:
        html = html.replace(nav_end, mini_search, 1)

    # Add the scroll JS logic before </body>
    body_end = '</body>'
    scroll_js = '''
  <script>
      // Sticky Header Mini Search Logic
      window.addEventListener('scroll', () => {
          const header = document.getElementById('main-header');
          const miniSearch = document.getElementById('mini-search');
          if (window.scrollY > 150) {
              header.style.boxShadow = '0 10px 30px rgba(0,0,0,0.8)';
              if (window.innerWidth > 1024 && miniSearch) {
                  miniSearch.style.display = 'flex';
              }
          } else {
              header.style.boxShadow = 'none';
              if (miniSearch) {
                  miniSearch.style.display = 'none';
              }
          }
      });
  </script>
</body>
'''
    if body_end in html:
        html = html.replace(body_end, scroll_js, 1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Header updated successfully.")

update_header()
