import os
import re

# 1. REWRITE ABOUT-US.HTML
about_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\about-us.html"

about_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>About Us | APD Global Trade</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    body { margin: 0; font-family: 'Inter', sans-serif; background: #020617; color: #e5e7eb; line-height: 1.6; }
    header { background: #071427; padding: 18px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(212, 175, 55, .15); }
    .logo { font-family: 'Playfair Display', serif; color: #d4af37; font-size: 20px; font-weight: bold; text-decoration: none; }
    nav a { color: #cbd5e1; text-decoration: none; margin-left: 25px; font-size: 14px; }
    nav a:hover { color: #d4af37 }
    .container { max-width: 900px; margin: 0 auto; padding: 80px 20px; }
    h1 { font-family: 'Playfair Display', serif; font-size: 48px; color: #d4af37; text-align: center; margin-bottom: 20px; }
    h2 { font-family: 'Playfair Display', serif; font-size: 32px; color: #fff; margin-top: 60px; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; }
    h3 { font-size: 20px; color: #d4af37; margin-top: 30px; }
    p { font-size: 16px; color: #9ca3af; margin-bottom: 20px; }
    .highlight-box { background: rgba(2, 6, 23, 0.8); border: 1px solid rgba(212, 175, 55, 0.3); padding: 40px; border-radius: 15px; margin-top: 60px; text-align: center; }
    .trust-bar { display: flex; justify-content: center; gap: 40px; margin-top: 60px; padding: 30px; background: #071427; border-radius: 10px; flex-wrap: wrap; }
    .trust-logo { font-weight: bold; font-size: 18px; color: #cbd5e1; display: flex; align-items: center; gap: 10px; }
  </style>
</head>
<body>

<header>
  <a href="/index.html" class="logo">APD Global Trade</a>
  <nav>
    <a href="/index.html">Home</a>
    <a href="/how-to-export.html">How to Export</a>
    <a href="/membership.html">Membership</a>
    <a href="/supplier-login.html" style="background: #d4af37; color: #000; padding: 8px 16px; border-radius: 4px; font-weight: bold;">Login</a>
  </nav>
</header>

<div class="container">
  <h1>Bridging the Gap in Global Trade</h1>
  <p style="text-align: center; font-size: 20px; max-width: 700px; margin: 0 auto;">At APD Global Trade, we don't just list products; we build the trust infrastructure that allows Indian exporters to reach the world with confidence.</p>

  <h2>Our Mission</h2>
  <p>To empower mid-sized Indian exporters—with a special focus on the Agro and Spices sector—by connecting them with vetted, high-intent global buyers. We believe that global trade shouldn't be a gamble; it should be a transparent, secure, and profitable journey.</p>

  <h2>The APD Trust Standard</h2>
  <p>We know the biggest fear in global trade is fraud and unverified leads. That’s why we’ve built APD Global Trade on three core pillars of trust:</p>
  <ul>
    <li style="margin-bottom: 15px;"><strong style="color: #fff;">Verified Identities:</strong> We manually check the GST, IEC (Import Export Code), and APEDA/FSSAI certifications of our Premium Suppliers to ensure they are export-ready.</li>
    <li style="margin-bottom: 15px;"><strong style="color: #fff;">Buyer Vetting:</strong> Our team filters through thousands of inquiries to ensure that when a supplier receives a lead, it comes from a buyer with real purchase intent and a verified phone number.</li>
    <li style="margin-bottom: 15px;"><strong style="color: #fff;">Human-Centric Support:</strong> We are not just a software; we are your trade partners. Every premium member has direct access to our founding team and dedicated account managers to help navigate the complexities of international trade.</li>
  </ul>

  <h2>Why Choose APD Global Trade?</h2>
  <p><strong>🌍 Global Reach:</strong> Access importers from the EU, Middle East, and SE Asia.</p>
  <p><strong>🌾 Agro-Focused Expertise:</strong> We understand the seasonal risks and quality standards of the agricultural industry.</p>
  <p><strong>🎯 Zero-Fluff Leads:</strong> We prioritize quality over quantity. One real buyer is worth more than 100 spam messages.</p>

  <div class="highlight-box">
    <div style="width: 120px; height: 120px; background: #1e293b; border-radius: 50%; margin: 0 auto 20px; border: 2px solid #d4af37; display: flex; align-items: center; justify-content: center; color: #64748b; font-size: 12px;">[Insert Professional Photo]</div>
    <h3 style="margin-top: 0;">Meet The Founder</h3>
    <p style="font-style: italic; color: #fff; font-size: 18px; line-height: 1.8;">"I noticed that while the internet made the world smaller, it also made it noisier. For every 100 trade inquiries an Indian exporter receives, 99 are often spam or unverified. This 'noise' costs our exporters time, money, and missed opportunities.</p>
    <p style="font-style: italic; color: #fff; font-size: 18px; line-height: 1.8;">I started APD Global Trade with one goal: <strong>To be the Filter, not just the Funnel.</strong> I wanted to create a platform where an exporter doesn't have to guess if a buyer is real. We do the vetting so you can focus on the shipping."</p>
    <p style="color: #d4af37; font-weight: bold; margin-top: 20px;">— Founder & CEO</p>
  </div>

  <div class="trust-bar">
    <div class="trust-logo">🇮🇳 Supporting Digital India</div>
    <div class="trust-logo">📑 GST Verified Network</div>
    <div class="trust-logo">🚢 IEC Compliant Exporters</div>
  </div>
</div>

<footer style="background: #020617; border-top: 1px solid rgba(212, 175, 55, 0.2); padding: 40px 20px; text-align: center; margin-top: 80px;">
    <p style="color: #6b7280; font-size: 14px;">Contact: ceo@apdglobaltrade.com | +91 98984 70743</p>
    <p style="color: #6b7280; font-size: 14px;">
        <a href="https://linkedin.com" target="_blank" style="color: #0077b5; text-decoration: none; font-weight: bold;">Connect with Founder on LinkedIn</a>
    </p>
    <p style="color: #6b7280; font-size: 12px; margin-top: 20px;">© 2026 APD Global Trade. All rights reserved.</p>
</footer>

</body>
</html>
"""

with open(about_path, "w", encoding="utf-8") as f:
    f.write(about_content)


# 2. UPDATE INDEX.HTML (Add Platform Stats)
index_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

platform_stats = """
  <!-- PLATFORM TRANSPARENCY STATS -->
  <section style="padding: 60px 5%; background: #0f172a; border-bottom: 1px solid rgba(212, 175, 55, 0.1);">
      <div class="container" style="display: flex; justify-content: space-around; flex-wrap: wrap; text-align: center; gap: 30px;">
          <div>
              <div style="font-family: 'Playfair Display', serif; font-size: 48px; color: var(--gold); font-weight: bold;">15+</div>
              <div style="font-size: 14px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px;">Countries Reached</div>
          </div>
          <div>
              <div style="font-family: 'Playfair Display', serif; font-size: 48px; color: var(--gold); font-weight: bold;">500+</div>
              <div style="font-size: 14px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px;">Verified Importers</div>
          </div>
          <div>
              <div style="font-family: 'Playfair Display', serif; font-size: 48px; color: var(--gold); font-weight: bold;">₹2.5Cr+</div>
              <div style="font-size: 14px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px;">Trade Value Facilitated</div>
          </div>
      </div>
  </section>
"""

if "PLATFORM TRANSPARENCY STATS" not in index_html:
    index_html = index_html.replace('<!-- VERIFIED SUCCESS STORIES -->', platform_stats + '\n<!-- VERIFIED SUCCESS STORIES -->')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# 3. UPDATE MEMBERSHIP.HTML (Add Trust Sidebar Icons & Account Manager)
mem_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"
with open(mem_path, "r", encoding="utf-8") as f:
    mem_html = f.read()

trust_sidebar = """
        <!-- TRUST HACKS SIDEBAR -->
        <div style="max-width: 800px; margin: 60px auto 0; background: rgba(255,255,255,0.02); border: 1px solid rgba(212, 175, 55, 0.2); border-radius: 12px; padding: 30px;">
            <h3 style="text-align: center; color: var(--gold); font-family: 'Playfair Display', serif; margin-top: 0; margin-bottom: 30px; font-size: 24px;">The APD Institutional Standard</h3>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
                <div style="flex: 1; min-width: 200px; text-align: center;">
                    <div style="font-size: 30px; margin-bottom: 10px;">🛡️</div>
                    <div style="font-weight: bold; color: #fff; margin-bottom: 5px;">Manual Verification</div>
                    <div style="font-size: 13px; color: #9ca3af;">Every buyer inquiry is manually checked for phone number validity and purchase intent.</div>
                </div>
                <div style="flex: 1; min-width: 200px; text-align: center;">
                    <div style="font-size: 30px; margin-bottom: 10px;">📞</div>
                    <div style="font-weight: bold; color: #fff; margin-bottom: 5px;">Direct Buyer Contact</div>
                    <div style="font-size: 13px; color: #9ca3af;">Get direct access to purchase managers. No anonymous messages, no middlemen.</div>
                </div>
                <div style="flex: 1; min-width: 200px; text-align: center;">
                    <div style="font-size: 30px; margin-bottom: 10px;">👨‍💼</div>
                    <div style="font-weight: bold; color: #fff; margin-bottom: 5px;">Dedicated Trade Consultant</div>
                    <div style="font-size: 13px; color: #9ca3af;">Direct 24/7 WhatsApp access to our founders for verification help and deal support.</div>
                </div>
            </div>
        </div>
"""

if "TRUST HACKS SIDEBAR" not in mem_html:
    # Insert it right before the SECURE PAYMENT LOGOS
    mem_html = mem_html.replace('<!-- SECURE PAYMENT LOGOS -->', trust_sidebar + '\n<!-- SECURE PAYMENT LOGOS -->')

with open(mem_path, "w", encoding="utf-8") as f:
    f.write(mem_html)

