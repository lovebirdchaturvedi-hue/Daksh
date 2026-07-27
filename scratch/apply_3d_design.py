import os

index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Inject Premium 3D / Glassmorphism Styles
premium_styles = """
    <style>
        /* PREMIUM 3D & GLASSMORPHISM OVERRIDES */
        body {
            background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
            position: relative;
        }
        
        /* Animated High-Tech Grid Background */
        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background-image: 
                linear-gradient(rgba(212, 175, 55, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(212, 175, 55, 0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -1;
            animation: gridMove 20s linear infinite;
        }
        @keyframes gridMove {
            0% { transform: translateY(0); }
            100% { transform: translateY(50px); }
        }

        /* Glassmorphism Cards */
        .pricing-card, .how-step, .highlight-box {
            background: rgba(15, 23, 42, 0.4) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(212, 175, 55, 0.15) !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        /* 3D Hover Levitation */
        .pricing-card:hover, .how-step:hover {
            transform: translateY(-15px) scale(1.03) !important;
            box-shadow: 0 25px 50px rgba(212, 175, 55, 0.15) !important;
            border-color: rgba(212, 175, 55, 0.5) !important;
            z-index: 10;
        }

        /* Golden Glowing Buttons */
        .btn, button {
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        .btn:hover {
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.6) !important;
            transform: translateY(-2px);
        }

        /* 3D Text Effect for Headlines */
        h1, h2 {
            text-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 20px rgba(212, 175, 55, 0.2);
        }
    </style>
"""

if "PREMIUM 3D" not in index_html:
    index_html = index_html.replace('</head>', premium_styles + '\n</head>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
