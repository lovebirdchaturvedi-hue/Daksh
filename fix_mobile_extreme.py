import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We will inject an even stronger CSS override block for mobile
# and add a 3D Blinking (Glowing Pulse) effect to the buttons.
mobile_fixes_css = """
  <style>
  /* ====== TOP-NOTCH MOBILE TYPOGRAPHY & 3D BLINK EFFECTS ====== */
  
  /* 3D Blinking/Glowing Animation */
  @keyframes blink3DGold {
      0% { box-shadow: 0 6px 0 #9c7b16, 0 0 5px rgba(250,204,21,0.5), inset 0 2px 0 rgba(255,255,255,0.5); transform: scale(1); }
      50% { box-shadow: 0 6px 0 #9c7b16, 0 0 25px rgba(250,204,21,1), inset 0 2px 0 rgba(255,255,255,0.8); transform: scale(1.02); }
      100% { box-shadow: 0 6px 0 #9c7b16, 0 0 5px rgba(250,204,21,0.5), inset 0 2px 0 rgba(255,255,255,0.5); transform: scale(1); }
  }

  @keyframes blink3DGreen {
      0% { box-shadow: 0 6px 0 #15803d, 0 0 5px rgba(37,211,102,0.5), inset 0 2px 0 rgba(255,255,255,0.4); transform: scale(1); }
      50% { box-shadow: 0 6px 0 #15803d, 0 0 25px rgba(37,211,102,1), inset 0 2px 0 rgba(255,255,255,0.8); transform: scale(1.02); }
      100% { box-shadow: 0 6px 0 #15803d, 0 0 5px rgba(37,211,102,0.5), inset 0 2px 0 rgba(255,255,255,0.4); transform: scale(1); }
  }

  @media (max-width: 768px) {
      /* ENFORCE ABSOLUTE NO OVERFLOW AND PROPER BOX SIZING */
      * {
          box-sizing: border-box !important;
      }
      body, html {
          overflow-x: hidden !important;
          max-width: 100vw !important;
      }

      /* Fix the squashed text boxes in the hero section */
      .hero-container-mobile {
          width: 100vw !important;
          max-width: 100vw !important;
          padding-left: 10px !important;
          padding-right: 10px !important;
          overflow: hidden !important;
      }
      
      .hero-container-mobile > div.fade-in {
          padding: 15px 10px !important;
          margin-left: 0 !important;
          margin-right: 0 !important;
          width: 100% !important;
          max-width: 100% !important;
          box-sizing: border-box !important;
      }
      
      /* Make sure the text inside the boxes scales down SIGNIFICANTLY */
      .hero-container-mobile > div.fade-in h3 {
          font-size: 1rem !important; /* Smaller */
          line-height: 1.3 !important;
          padding: 0 !important;
          white-space: normal !important;
      }
      .hero-container-mobile > div.fade-in p, 
      .hero-container-mobile > div.fade-in span {
          font-size: 0.8rem !important; /* Smaller */
          line-height: 1.4 !important;
          padding: 0 !important;
          display: block !important;
          white-space: normal !important;
      }
      
      /* Optimize the massive buttons */
      .hero-buttons {
          padding: 0 !important;
          margin-left: 0 !important;
          margin-right: 0 !important;
          gap: 12px !important;
          margin-bottom: 20px !important;
          width: 100% !important;
          display: flex !important;
          flex-direction: column !important;
      }
      .hero-buttons .btn {
          width: 100% !important;
          padding: 12px !important; /* Smaller padding */
          font-size: 0.9rem !important; /* Smaller font */
          box-sizing: border-box !important;
          white-space: normal !important;
          line-height: 1.2 !important;
      }

      /* Fix the overflowing 3D text at the bottom of the hero */
      .promise-3d {
          font-size: 1.2rem !important; /* VERY Small now */
          padding: 0 10px !important;
          line-height: 1.2 !important;
          margin-top: 10px !important;
          width: 100% !important;
          white-space: normal !important;
      }

      /* General hero adjustments */
      #atomic-h1 {
          font-size: 1.8rem !important; /* Smaller */
          padding: 0 10px !important;
      }

      /* Apply Blinking 3D Effect to Bottom Sticky Action Bar Buttons */
      .btn-3d-gold {
          animation: blink3DGold 2.5s infinite !important;
      }
      .btn-3d-green {
          animation: blink3DGreen 2.5s infinite !important;
          animation-delay: 1.25s !important; /* Offset the green pulse */
      }
      
      /* Also apply 3D pulse to the main hero Apply button */
      .hero-buttons .btn[href="/membership.html"] {
          animation: blink3DGold 2.5s infinite !important;
          box-shadow: 0 6px 0 #9c7b16, 0 10px 20px rgba(0,0,0,0.5), inset 0 2px 0 rgba(255,255,255,0.4) !important;
      }
  }
  </style>
</head>
"""

# Replace the previous injection if it exists
if "/* ====== TOP-NOTCH MOBILE TYPOGRAPHY & LAYOUT FIXES ====== */" in content:
    # We remove the old block and replace it
    content = re.sub(r'<style>\s*/\* ====== TOP-NOTCH MOBILE TYPOGRAPHY & LAYOUT FIXES ====== \*/.*?</style>\s*</head>', mobile_fixes_css, content, flags=re.DOTALL)
else:
    content = content.replace("</head>", mobile_fixes_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected extreme mobile font shrinking, width containment, and 3D Blinking CSS.")
