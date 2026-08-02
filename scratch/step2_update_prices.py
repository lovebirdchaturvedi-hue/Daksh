import re

repo = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo"
membership_path = repo + r"\membership.html"

with open(membership_path, "r", encoding="utf-8") as f:
    content = f.read()

# =============================================
# UPDATE PLAN PRICES & NAMES
# =============================================

# 3-Month Plan: $249 -> $349, ₹19,999 -> ₹29,500
# Also: strikethrough $599 -> $699, ₹51,000 -> ₹59,000
content = content.replace(
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">$599</s> $249",
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">$699</s> $349"
)
content = content.replace(
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">₹51,000</s> ₹19,999",
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">₹59,000</s> ₹29,500"
)
# Button payment values 3-month
content = content.replace(
    "initiatePayment('Growth Program (3 Months)', 249, 19999)",
    "initiatePayment('Professional Pass (3 Months)', 349, 29500)"
)

# 6-Month Plan: $599 -> $799, ₹51,000 -> ₹75,000
# strikethrough $1,199 -> $1,599, ₹1,19,000 -> ₹1,50,000
content = content.replace(
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">$1,199</s> $599",
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">$1,599</s> $799"
)
content = content.replace(
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">₹1,19,000</s> ₹51,000",
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">₹1,50,000</s> ₹75,000"
)
# Button payment values 6-month
content = content.replace(
    "initiatePayment('Institutional Elite (6 Months)', 599, 51000)",
    "initiatePayment('Institutional Elite (6 Months)', 799, 75000)"
)

# 12-Month Plan: $999 -> $1499, ₹1,19,000 -> ₹1,49,000
# strikethrough $1,999 -> $2,999, ₹2,50,000 -> ₹2,99,000
content = content.replace(
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">$1,999</s> $999",
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">$2,999</s> $1,499"
)
content = content.replace(
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">₹2,50,000</s> ₹1,19,000",
    "<s style=\"font-size: 18px; color: #64748b; font-weight: 500;\">₹2,99,000</s> ₹1,49,000"
)
# Button payment values 12-month
content = content.replace(
    "initiatePayment('Global Enterprise (12 Months)', 999, 119000)",
    "initiatePayment('Global Enterprise (12 Months)', 1499, 149000)"
)

# Plan names
content = content.replace(
    "<h3 style=\"font-size: 26px; margin-bottom: 10px; color: #fff;\">Growth Program</h3>",
    "<h3 style=\"font-size: 26px; margin-bottom: 10px; color: #6ab0f5;\">Professional Pass</h3>"
)
content = content.replace(
    "<p style=\"color: #94a3b8; font-size: 14px; margin-bottom: 20px;\">3 Months Access</p>\n            <div class=\"price\" style=\"font-size: 42px; color: #fff;",
    "<p style=\"color: #94a3b8; font-size: 13px; margin-bottom: 4px;\">Trial Package</p>\n            <p style=\"color: #94a3b8; font-size: 14px; margin-bottom: 20px;\">3 Months Access</p>\n            <div class=\"price\" style=\"font-size: 42px; color: #fff;"
)
content = content.replace(
    "<p style=\"color: #94a3b8; font-size: 13px; margin-bottom: 30px;\">For exporters ready to explore</p>",
    "<p style=\"color: #94a3b8; font-size: 13px; margin-bottom: 30px;\">Get 25 verified buyers — any commodity you want</p>"
)
content = content.replace(
    "<li style=\"margin-bottom: 15px;\">100% Verified Global Buyers <span style=\"background: #facc15; color: #000; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: 700; margin-left: 5px;\">25 Limit</span></li>",
    "<li style=\"margin-bottom: 15px;\">✅ 25 Verified Global Buyers — Any Commodity <span style=\"background: #6ab0f5; color: #000; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: 700; margin-left: 5px;\">YOUR CHOICE</span></li>"
)
content = content.replace(
    "<button class=\"btn\" style=\"margin-top: auto; background: #facc15; color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;\" onclick=\"initiatePayment('Professional Pass (3 Months)', 349, 29500)\">Get 3 Months Growth Access</button>",
    "<button class=\"btn\" style=\"margin-top: auto; background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: #fff; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s;\" onclick=\"initiatePayment('Professional Pass (3 Months)', 349, 29500)\">Start Trial — Professional Pass</button>"
)

# 12-month: upgrade description
content = content.replace(
    "<p style=\"color: #94a3b8; font-size: 13px; margin-bottom: 30px;\">Maximum authority package</p>",
    "<p style=\"color: #facc15; font-size: 13px; margin-bottom: 30px; font-weight: 700;\">🏆 Best for Long-Term Export Growth</p>"
)
content = content.replace(
    "<button class=\"btn\" style=\"margin-top: auto; background: transparent; color: var(--gold); font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: 2px solid var(--gold); cursor: pointer; transition: 0.3s; margin-bottom: 15px;\" onclick=\"initiatePayment('Global Enterprise (12 Months)', 1499, 149000)\">Get 12 Months Enterprise Access</button>",
    "<button class=\"btn\" style=\"margin-top: auto; background: linear-gradient(135deg, #d97706, #f59e0b, #fbbf24); color: #000; font-weight: 800; padding: 15px; width: 100%; border-radius: 50px; border: none; cursor: pointer; transition: 0.3s; margin-bottom: 15px; box-shadow: 0 8px 25px rgba(217,119,6,0.4);\" onclick=\"initiatePayment('Global Enterprise (12 Months)', 1499, 149000)\">🏆 Get 12 Months Enterprise Access</button>"
)

with open(membership_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Pricing plans updated with new prices and names!")
