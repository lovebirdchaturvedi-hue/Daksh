import re

with open('membership.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;"> 
# and replace its inner HTML with our 12 static cards.

grid_start = content.find('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;">')
if grid_start == -1:
    print("Could not find grid start")
    exit(1)

# Find the end of this div. We can search for the start of the next section to narrow it down.
next_section = content.find('</section>', grid_start)
grid_end = content.rfind('</div>', grid_start, next_section)

# Define our 12 cards
cards = [
    {
        "id": "Kouamé Diaby",
        "name": "Kouamé Diaby",
        "flag": "🇨🇮",
        "title": "Cocoa & Cashew Exporter",
        "badge": "Verified Cocoa Exporter",
        "img": "/assets/images/testimonial_franch.jpg",
        "quote": "APD Global Trade connected me with verified buyers in Europe within my first month. The secure payment system is game-changing for our export volume."
    },
    {
        "id": "Li Na",
        "name": "Li Na (李娜)",
        "flag": "🇨🇳",
        "title": "Garlic & Ginger Export Manager",
        "badge": "Verified Garlic Exporter",
        "img": "/assets/images/testimonial_chinese.jpg",
        "quote": "The volume of RFQs we receive on this platform is unmatched. We expanded our ginger exports to 3 new continents this year alone."
    },
    {
        "id": "Muhammad Ibrahim",
        "name": "Muhammad Ibrahim",
        "flag": "🇳🇬",
        "title": "Sesame & Soybean Exporter",
        "badge": "Verified Sesame Exporter",
        "img": "/assets/images/testimonial_nigeria.jpg",
        "quote": "Finally, a platform that understands real commodities trade. The verified buyer badges save us weeks of due diligence."
    },
    {
        "id": "Pinkesh Patel",
        "name": "Pinkesh Patel",
        "flag": "🇮🇳",
        "title": "Cumin Seeds, Coriander & more",
        "badge": "Verified Spices Exporter",
        "img": "/assets/images/testimonial_gujrati.jpg",
        "quote": "Since joining the Institutional Elite plan, our cumin seed exports have grown by 300%. The global reach is simply phenomenal."
    },
    {
        "id": "Tariq Al-Mansoor",
        "name": "Tariq Al-Mansoor",
        "flag": "🇦🇪",
        "title": "Managing Director, Al-Mansoor Imports",
        "badge": "Verified Dubai Buyer",
        "img": "/assets/images/thumb_arabic.jpg",
        "quote": "The level of verification on APD Global is outstanding. We source high-quality agro commodities safely and efficiently."
    },
    {
        "id": "Jean-Luc Moreau",
        "name": "Jean-Luc Moreau",
        "flag": "🇫🇷",
        "title": "Commodities Partner, France",
        "badge": "Verified European Buyer",
        "img": "/assets/images/thumb_french2.jpg",
        "quote": "We found reliable suppliers for organic grains in just 48 hours. The zero-commission model is a huge benefit for our margins."
    },
    {
        "id": "Elena Rostova",
        "name": "Elena Rostova",
        "flag": "🇪🇸",
        "title": "Agri-Trading Director, Spain",
        "badge": "Verified Europe Buyer",
        "img": "/assets/images/thumb_spanish.jpg",
        "quote": "The platform's direct access to verified exporters worldwide has completely streamlined our procurement process."
    },
    {
        "id": "Mateus Silva",
        "name": "Mateus Silva",
        "flag": "🇵🇹",
        "title": "Global Sourcing Director",
        "badge": "Verified Portugal Buyer",
        "img": "/assets/images/thumb_portuguese.jpg",
        "quote": "A truly premium marketplace. We have successfully closed multiple six-figure deals through the Elite network."
    },
    {
        "id": "Sarah Jenkins",
        "name": "Sarah Jenkins",
        "flag": "🇬🇧",
        "title": "Head of Sourcing, Euro Foods UK",
        "badge": "Verified UK Buyer",
        "img": "/assets/images/thumb_uk.jpg",
        "quote": "The background checks give us immense confidence. We only trade with APD Verified Members now."
    },
    {
        "id": "Ananya Das",
        "name": "Ananya Das",
        "flag": "🇮🇳",
        "title": "MD, Bengal Rice & Grain Trade",
        "badge": "Verified Rice Exporter",
        "img": "/assets/images/thumb_bengali.jpg",
        "quote": "Our premium rice exports have skyrocketed. The institutional buyers here are serious and ready to transact."
    },
    {
        "id": "Carlos Mendez",
        "name": "Carlos Mendez",
        "flag": "🇦🇪",
        "title": "Import Manager, Gulf Distributing",
        "badge": "Verified Gulf Buyer",
        "img": "/assets/images/thumb_gulf.jpg",
        "quote": "The seamless RFQ system and direct negotiation channels have cut our sourcing time by over 50%."
    },
    {
        "id": "David Chen",
        "name": "David Chen",
        "flag": "🇸🇬",
        "title": "Commodities Buyer, Singapore",
        "badge": "Verified Singapore Partner",
        "img": "/assets/images/thumb_asian.jpg",
        "quote": "Exceptional platform functionality. The verification process ensures we are always dealing with legitimate businesses."
    }
]

html_cards = []
for b in cards:
    card = f"""
              <!-- {b['id']} -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4); padding: 25px; display: flex; flex-direction: column; align-items: center; text-align: center;">
                  <div style="width: 100px; height: 100px; border-radius: 50%; overflow: hidden; border: 3px solid #FFD700; margin-bottom: 15px; background: #000;">
                      <img src="{b['img']}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 20%;" alt="{b['name']}">
                  </div>
                  <h4 style="color: #fff; font-size: 16px; font-weight: 700; margin: 0 0 5px;">{b['name']} {b['flag']}</h4>
                  <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 15px;">{b['title']}</p>
                  <div style="flex-grow: 1;">
                      <p style="color: #cbd5e1; font-size: 14px; font-style: italic; line-height: 1.5; margin: 0 0 20px;">"{b['quote']}"</p>
                  </div>
                  <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 4px 10px; border-radius: 20px; font-weight: 700; width: 100%; display: block; box-sizing: border-box;">✅ {b['badge']}</span>
              </div>"""
    html_cards.append(card)

grid_header = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;">'
# We have to be careful not to delete too much or too little. 
# A safer way is to use regex or beautiful soup, but let's just do a tight regex replacement for the grid div contents.
pattern = re.compile(r'(<div style="display: grid; grid-template-columns: repeat\(auto-fill, minmax\(270px, 1fr\)\); gap: 20px; text-align: left;">).*?(</section>)', re.DOTALL)
# Wait, the </div> for the grid is before the </section>.
# Let's replace everything between grid start and the closing </div> of the grid.
# Actually, if I just replace everything from grid start up to the first </div> that sits right before </section>

def replacer(match):
    # match.group(1) is the start div. match.group(2) is the </section>.
    # We want to insert the cards, then close the div, then return the section close.
    # Wait, there is a `</div>` for the container and `</div>` for the grid.
    # Let's look at how the file is structured.
    pass

with open('membership.html', 'w', encoding='utf-8') as f:
    pass
