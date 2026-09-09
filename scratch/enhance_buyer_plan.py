with open('membership.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the buyer plan section's style to add the glowing animation and update the button
old_section_start = '<section id="buyer-plan" style="padding: 60px 20px; max-width: 1200px; margin: 0 auto;">\n        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 2px solid #ef4444; border-radius: 24px; padding: 40px; position: relative; overflow: hidden; margin-bottom: 50px;">'
new_section_start = """
    <style>
        @keyframes buyerGlow {
            0%   { border-color: #ef4444; box-shadow: 0 0 15px rgba(239, 68, 68, 0.3); }
            50%  { border-color: #fca5a5; box-shadow: 0 0 35px rgba(239, 68, 68, 0.7); }
            100% { border-color: #ef4444; box-shadow: 0 0 15px rgba(239, 68, 68, 0.3); }
        }
        @keyframes pulseButton {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    </style>
    <section id="buyer-plan" style="padding: 60px 20px; max-width: 1200px; margin: 0 auto;">
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 2px solid #ef4444; border-radius: 24px; padding: 40px; position: relative; overflow: hidden; margin-bottom: 50px; animation: buyerGlow 2.5s infinite alternate;">"""

old_button = '<a href="#" onclick="initiatePayment(\'Verified Buyer Membership (1 Year)\', 2500, 210000); return false;" style="display: inline-block; background: #ef4444; color: #fff; padding: 16px 40px; border-radius: 50px; font-weight: 800; font-size: 16px; text-decoration: none; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; box-shadow: 0 10px 25px rgba(239, 68, 68, 0.4);">Pay Now to Become a Verified Buyer</a>'
new_button = '<a href="#" onclick="initiatePayment(\'Verified Buyer Membership (1 Year)\', 2500, 210000); return false;" style="display: inline-block; background: linear-gradient(90deg, #ef4444, #dc2626); color: #fff; padding: 16px 40px; border-radius: 50px; font-weight: 800; font-size: 16px; text-decoration: none; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s; box-shadow: 0 10px 25px rgba(239, 68, 68, 0.6); animation: pulseButton 2s infinite;">Pay Now to Become a Verified Buyer <span style="font-size: 11px; background: rgba(0,0,0,0.3); padding: 4px 10px; border-radius: 6px; margin-left: 8px; vertical-align: middle;">PayPal / BHIM</span></a>'

html = html.replace(old_section_start, new_section_start)
html = html.replace(old_button, new_button)

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Buyer Plan design.")
