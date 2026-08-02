import re

with open('membership.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the 4 replacement blocks
blocks = [
    {
        "id": "Kouamé Diaby",
        "flag": "🇨🇮",
        "title": "Cocoa & Cashew Exporter",
        "badge": "Verified Cocoa Exporter",
        "img": "/assets/images/testimonial_franch.jpg",
        "quote": "APD Global Trade connected me with verified buyers in Europe within my first month. The secure payment system is game-changing for our export volume.",
        "regex": r'<!-- 1\. Kouam.*?</div>\s*</div>'
    },
    {
        "id": "Li Na",
        "name": "Li Na (李娜)",
        "flag": "🇨🇳",
        "title": "Garlic & Ginger Export Manager",
        "badge": "Verified Garlic Exporter",
        "img": "/assets/images/testimonial_chinese.jpg",
        "quote": "The volume of RFQs we receive on this platform is unmatched. We expanded our ginger exports to 3 new continents this year alone.",
        "regex": r'<!-- 2\. Li Na.*?</div>\s*</div>'
    },
    {
        "id": "Muhammad Ibrahim",
        "flag": "🇳🇬",
        "title": "Sesame & Soybean Exporter",
        "badge": "Verified Sesame Exporter",
        "img": "/assets/images/testimonial_nigeria.jpg",
        "quote": "Finally, a platform that understands real commodities trade. The verified buyer badges save us weeks of due diligence.",
        "regex": r'<!-- 3\. Muhammad Ibrahim.*?</div>\s*</div>'
    },
    {
        "id": "Pinkesh Patel",
        "flag": "🇮🇳",
        "title": "Cumin Seeds, Coriander & more",
        "badge": "Verified Spices Exporter",
        "img": "/assets/images/testimonial_gujrati.jpg",
        "quote": "Since joining the Institutional Elite plan, our cumin seed exports have grown by 300%. The global reach is simply phenomenal.",
        "regex": r'<!-- 4\. Pinkesh Patel.*?</div>\s*</div>'
    }
]

for b in blocks:
    name = b.get("name", b["id"])
    card = f"""<!-- {b['id']} -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4); padding: 25px; display: flex; flex-direction: column; align-items: center; text-align: center;">
                  <div style="width: 100px; height: 100px; border-radius: 50%; overflow: hidden; border: 3px solid #FFD700; margin-bottom: 15px; background: #000;">
                      <img src="{b['img']}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 20%;" alt="{name}">
                  </div>
                  <h4 style="color: #fff; font-size: 16px; font-weight: 700; margin: 0 0 5px;">{name} {b['flag']}</h4>
                  <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 15px;">{b['title']}</p>
                  <div style="flex-grow: 1;">
                      <p style="color: #cbd5e1; font-size: 14px; font-style: italic; line-height: 1.5; margin: 0 0 20px;">"{b['quote']}"</p>
                  </div>
                  <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 4px 10px; border-radius: 20px; font-weight: 700; width: 100%; display: block; box-sizing: border-box;">✅ {b['badge']}</span>
              </div>"""
    
    content = re.sub(b["regex"], card, content, flags=re.DOTALL)

with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced videos with static cards on membership.html")
