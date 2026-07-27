import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

mobile_fixes_css = """
  <style>
  /* ====== TOP-NOTCH MOBILE TYPOGRAPHY & LAYOUT FIXES ====== */
  @media (max-width: 768px) {
      /* Fix the squashed text boxes in the hero section */
      .hero-container-mobile > div.fade-in {
          padding: 18px 15px !important;
          margin-left: 15px !important;
          margin-right: 15px !important;
          width: calc(100% - 30px) !important;
          box-sizing: border-box !important;
      }
      
      /* Make sure the text inside the boxes scales down */
      .hero-container-mobile > div.fade-in h3 {
          font-size: 1.25rem !important;
          line-height: 1.4 !important;
          padding: 0 !important;
      }
      .hero-container-mobile > div.fade-in p, 
      .hero-container-mobile > div.fade-in span {
          font-size: 0.95rem !important;
          line-height: 1.5 !important;
          padding: 0 !important;
          display: block !important;
      }
      
      /* Optimize the massive buttons */
      .hero-buttons {
          padding: 0 15px !important;
          gap: 12px !important;
          margin-bottom: 30px !important;
      }
      .hero-buttons .btn {
          width: 100% !important;
          padding: 16px !important;
          font-size: 1rem !important;
          box-sizing: border-box !important;
          white-space: normal !important;
          line-height: 1.3 !important;
      }

      /* Fix the overflowing 3D text at the bottom of the hero */
      .promise-3d {
          font-size: 1.6rem !important; /* Scale down from 2.8rem */
          padding: 0 20px !important;
          line-height: 1.3 !important;
          margin-top: 10px !important;
      }

      /* General hero adjustments */
      .hero-premium {
          min-height: auto !important;
          padding-bottom: 80px !important;
      }
      #atomic-h1 {
          font-size: 2.2rem !important;
      }
  }
  </style>
</head>
"""

content = content.replace("</head>", mobile_fixes_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected mobile layout fixes.")
