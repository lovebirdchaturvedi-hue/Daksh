import re

html_injection = """
          <!-- DYNAMIC 4D/8D TESTIMONIAL CAROUSEL -->
          <style>
              /* 4D/8D Transition Animations */
              @keyframes ani-flip {
                  0% { transform: perspective(1200px) rotateY(90deg); opacity: 0; }
                  100% { transform: perspective(1200px) rotateY(0deg); opacity: 1; }
              }
              @keyframes ani-scale {
                  0% { transform: perspective(1200px) translateZ(-800px) scale(0.5); opacity: 0; }
                  100% { transform: perspective(1200px) translateZ(0) scale(1); opacity: 1; }
              }
              @keyframes ani-slide-3d {
                  0% { transform: perspective(1200px) translateY(100px) rotateX(-45deg); opacity: 0; }
                  100% { transform: perspective(1200px) translateY(0) rotateX(0deg); opacity: 1; }
              }
              @keyframes ani-swing {
                  0% { transform: perspective(1200px) rotateX(-90deg); transform-origin: top; opacity: 0; }
                  100% { transform: perspective(1200px) rotateX(0deg); transform-origin: top; opacity: 1; }
              }
              @keyframes pulse-gold {
                  0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.4); }
                  50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.8), 0 0 60px rgba(255, 215, 0, 0.4); }
                  100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.4); }
              }
              
              .testi-dynamic-container {
                  width: 100%;
                  max-width: 900px;
                  margin: 0 auto;
                  min-height: 450px;
                  position: relative;
                  display: flex;
                  align-items: center;
                  justify-content: center;
              }
              
              .testi-card-8d {
                  background: rgba(15, 23, 42, 0.85);
                  backdrop-filter: blur(16px);
                  -webkit-backdrop-filter: blur(16px);
                  border: 1px solid rgba(255, 215, 0, 0.3);
                  border-radius: 24px;
                  padding: 40px;
                  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), inset 0 0 20px rgba(255, 215, 0, 0.05);
                  display: flex;
                  flex-direction: column;
                  align-items: center;
                  text-align: center;
                  width: 100%;
                  will-change: transform, opacity;
              }
              
              .testi-avatar-8d {
                  width: 160px;
                  height: 160px;
                  border-radius: 50%;
                  overflow: hidden;
                  border: 4px solid #FFD700;
                  margin-bottom: 25px;
                  background: #000;
                  animation: pulse-gold 3s infinite ease-in-out;
              }
              
              .testi-avatar-8d img {
                  width: 100%;
                  height: 100%;
                  object-fit: cover;
                  object-position: center 20%;
              }

              .anim-flip { animation: ani-flip 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
              .anim-scale { animation: ani-scale 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
              .anim-slide { animation: ani-slide-3d 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
              .anim-swing { animation: ani-swing 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
          </style>

          <div class="testi-dynamic-container" id="dynamic-testimonial-wrapper">
              <!-- JS WILL INJECT CARDS HERE -->
          </div>

          <script>
              const testimonials = [
                  {
                      name: "Kouamé Diaby 🇨🇮",
                      title: "Cocoa & Cashew Exporter",
                      img: "/assets/images/testimonial_franch.jpg",
                      badge: "Verified Cocoa Exporter",
                      quote: "APD Global Trade connected me with verified buyers in Europe within my first month. The secure payment system and deep market analytics completely changed how we handle bulk commodities. By utilizing their institutional elite framework, our cocoa and cashew export volumes have seen a 45% increase year-over-year. The zero-commission structure is truly a game-changing asset."
                  },
                  {
                      name: "Li Na (李娜) 🇨🇳",
                      title: "Garlic & Ginger Export Manager",
                      img: "/assets/images/testimonial_chinese.jpg",
                      badge: "Verified Garlic Exporter",
                      quote: "The volume of RFQs we receive on this premium platform is simply unmatched in the industry. Thanks to the stringent verification checks, we never have to worry about fraudulent buyers. We successfully expanded our ginger exports to 3 new continents this year alone. It is an indispensable tool for serious international trade managers."
                  },
                  {
                      name: "Muhammad Ibrahim 🇳🇬",
                      title: "Sesame & Soybean Exporter",
                      img: "/assets/images/testimonial_nigeria.jpg",
                      badge: "Verified Sesame Exporter",
                      quote: "Finally, a platform that understands real commodities trade at scale. The verified buyer badges save our team weeks of due diligence. When we negotiate a 500-ton sesame shipment, we do it with absolute confidence knowing APD has vetted the other party's financials. Unparalleled trust and efficiency."
                  },
                  {
                      name: "Pinkesh Patel 🇮🇳",
                      title: "Cumin Seeds, Coriander & more",
                      img: "/assets/images/testimonial_gujrati.jpg",
                      badge: "Verified Spices Exporter",
                      quote: "Since joining the Institutional Elite plan, our cumin seed exports have grown by 300%. The global reach and institutional dashboard give us a bird's-eye view of real-time market demands. We replaced three different brokers just by using this direct networking system. It is simply phenomenal."
                  },
                  {
                      name: "Tariq Al-Mansoor 🇦🇪",
                      title: "Managing Director, Al-Mansoor Imports",
                      img: "/assets/images/thumb_arabic.jpg",
                      badge: "Verified Dubai Buyer",
                      quote: "The level of verification on APD Global is outstanding. We source high-quality agro commodities safely and efficiently for the UAE market. Being able to view real-time compliance metrics before issuing a Letter of Credit has streamlined our import cycle by almost 60%. Highly recommended for elite buyers."
                  },
                  {
                      name: "Jean-Luc Moreau 🇫🇷",
                      title: "Commodities Partner, France",
                      img: "/assets/images/thumb_french2.jpg",
                      badge: "Verified European Buyer",
                      quote: "We found reliable suppliers for organic grains in just 48 hours. The zero-commission model is a huge benefit for our margins. European procurement requires strict traceability, and the transparency provided by APD Global's verified exporter profiles gives us exactly what we need to execute multi-million euro deals securely."
                  },
                  {
                      name: "Elena Rostova 🇪🇸",
                      title: "Agri-Trading Director, Spain",
                      img: "/assets/images/thumb_spanish.jpg",
                      badge: "Verified Europe Buyer",
                      quote: "The platform's direct access to verified exporters worldwide has completely streamlined our procurement process. We used to spend a massive amount of capital on sourcing agents across South America and Asia. Now, the Elite network brings the most reputable suppliers straight to our dashboard with zero hassle."
                  },
                  {
                      name: "Mateus Silva 🇵🇹",
                      title: "Global Sourcing Director",
                      img: "/assets/images/thumb_portuguese.jpg",
                      badge: "Verified Portugal Buyer",
                      quote: "A truly premium marketplace. We have successfully closed multiple six-figure deals through the Elite network. The intuitive interface combined with 100% verified members ensures that every RFQ we post receives serious, high-quality bids. APD has become the backbone of our global sourcing strategy."
                  },
                  {
                      name: "Sarah Jenkins 🇬🇧",
                      title: "Head of Sourcing, Euro Foods UK",
                      img: "/assets/images/thumb_uk.jpg",
                      badge: "Verified UK Buyer",
                      quote: "The background checks give us immense confidence. We only trade with APD Verified Members now. Sourcing bulk commodities for the UK food sector requires absolute reliability. Having a direct line to top-tier, compliant suppliers across the globe without paying hidden broker fees is revolutionary."
                  },
                  {
                      name: "Ananya Das 🇮🇳",
                      title: "MD, Bengal Rice & Grain Trade",
                      img: "/assets/images/thumb_bengali.jpg",
                      badge: "Verified Rice Exporter",
                      quote: "Our premium rice exports have skyrocketed since we launched our profile. The institutional buyers here are serious and ready to transact. Unlike other B2B platforms cluttered with spam inquiries, APD provides a curated, high-end environment where genuine trade happens rapidly and securely."
                  },
                  {
                      name: "Carlos Mendez 🇦🇪",
                      title: "Import Manager, Gulf Distributing",
                      img: "/assets/images/thumb_gulf.jpg",
                      badge: "Verified Gulf Buyer",
                      quote: "The seamless RFQ system and direct negotiation channels have cut our sourcing time by over 50%. Gulf Distributing handles massive volumes daily, and the ability to instantly connect with verified agricultural producers on a visually stunning, secure platform is exactly the upgrade our procurement team needed."
                  },
                  {
                      name: "David Chen 🇸🇬",
                      title: "Commodities Buyer, Singapore",
                      img: "/assets/images/thumb_asian.jpg",
                      badge: "Verified Singapore Partner",
                      quote: "Exceptional platform functionality and hyper-premium design. The verification process ensures we are always dealing with legitimate, capable businesses in the APAC region. The transition to APD Global Trade has modernized our entire commodities purchasing flow, saving us thousands in traditional commission fees."
                  }
              ];

              const animations = ['anim-flip', 'anim-scale', 'anim-slide', 'anim-swing'];
              let currentIndex = 0;
              const wrapper = document.getElementById('dynamic-testimonial-wrapper');

              function renderTestimonial() {
                  const t = testimonials[currentIndex];
                  const animClass = animations[Math.floor(Math.random() * animations.length)];
                  
                  const html = `
                      <div class="testi-card-8d ${animClass}">
                          <div class="testi-avatar-8d">
                              <img src="${t.img}" alt="${t.name}">
                          </div>
                          <h4 style="color: #fff; font-size: 26px; font-weight: 800; margin: 0 0 8px; font-family: 'Outfit', sans-serif;">${t.name}</h4>
                          <p style="color: var(--gold); font-size: 16px; font-weight: 700; margin: 0 0 25px; text-transform: uppercase; letter-spacing: 1px;">${t.title}</p>
                          <div style="flex-grow: 1; max-width: 800px;">
                              <p style="color: #cbd5e1; font-size: 19px; font-style: italic; line-height: 1.7; margin: 0 0 35px; font-weight: 300;">"${t.quote}"</p>
                          </div>
                          <span style="font-size: 14px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 8px 24px; border-radius: 30px; font-weight: 800; border: 1px solid rgba(34,197,94,0.4); text-transform: uppercase; letter-spacing: 1px;">✅ ${t.badge}</span>
                      </div>
                  `;
                  
                  wrapper.innerHTML = html;
                  currentIndex = (currentIndex + 1) % testimonials.length;
              }

              // Initial render
              renderTestimonial();
              
              // Rotate every 10 seconds
              setInterval(renderTestimonial, 10000);
          </script>
"""

def replace_grid(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;">'
    start_idx = content.find(start_str)
    if start_idx == -1:
        print(f"Start string not found in {filepath}")
        return
        
    next_section = content.find('</section>', start_idx)
    end_idx = content.rfind('</div>', start_idx, next_section)
    if end_idx == -1:
        print(f"End string not found in {filepath}")
        return
        
    # include the closing div
    end_idx += 6
    
    new_content = content[:start_idx] + html_injection + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully injected 4D dynamic carousel into {filepath}")

replace_grid('membership.html')
replace_grid('index.html')
