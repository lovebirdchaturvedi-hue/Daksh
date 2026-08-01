import os

membership_path = r"c:\Users\DELL\.gemini\antigravity\playground\vacant-ride\daksh_repo\membership.html"

with open(membership_path, "r", encoding="utf-8") as f:
    content = f.read()

# Cut content at "Inside The APD Membership Portal" or before testimonials section
# Find "<!-- MEMBERSHIP PORTAL VIDEO SHOWCASE -->" or "VERIFIED SUCCESS STORIES"
target_start = "<!-- ============================================================ -->\n  <!-- HIGHLIGHTED GLOBAL CLIENT VIDEO TESTIMONIALS"

# Split content: before testimonials and after broken sections
part_before_testimonials = content.split(target_start)[0]

# Clean Membership Demo Section HTML
clean_membership_demo_html = """    <!-- ============================================================ -->
    <!-- MEMBERSHIP PORTAL VIDEO SHOWCASE -->
    <!-- ============================================================ -->
    <section style="padding: 70px 20px; background: linear-gradient(180deg, #071427 0%, #0a0f1c 100%); border-top: 1px solid rgba(212,175,55,0.2); border-bottom: 1px solid rgba(212,175,55,0.2); margin-bottom: 50px;">
        <div style="max-width: 1200px; margin: 0 auto; text-align: center;">
            <span style="background: rgba(212,175,55,0.15); color: #facc15; padding: 6px 18px; border-radius: 30px; font-size: 0.8rem; font-weight: 800; border: 1px solid rgba(212,175,55,0.4); text-transform: uppercase; letter-spacing: 1px;">MEMBERSHIP PORTAL DEMO</span>
            <h2 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 700; margin: 15px 0 10px;">Inside The APD Membership Portal</h2>
            <p style="color: #94a3b8; font-size: 16px; max-width: 750px; margin: 0 auto 45px;">Watch how our verified membership portal unlocks direct contact access to thousands of active global buyers.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 30px; text-align: left;">
                
                <!-- Video 1: Membership Portal Walkthrough -->
                <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(212,175,55,0.3); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; background: #000;">
                        <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                            <source src="/assets/videos/Membership Best One.mp4" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                    </div>
                    <div style="padding: 20px;">
                        <span style="color: #facc15; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">MEMBERSHIP SYSTEM</span>
                        <h3 style="color: #fff; font-size: 18px; font-weight: 700; margin: 6px 0 8px;">Institutional Buyer Match &amp; RFQ Unlocks</h3>
                        <p style="color: #94a3b8; font-size: 13px; margin: 0;">Step-by-step preview of unlocking verified buyer RFQs, customs data, and direct phone/WhatsApp numbers.</p>
                    </div>
                </div>

                <!-- Video 2: Membership Best 2 -->
                <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(212,175,55,0.3); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; background: #000;">
                        <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                            <source src="/assets/videos/Membership_Best_2_Clean.mp4" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                    </div>
                    <div style="padding: 20px;">
                        <span style="color: #22c55e; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">SUPPLIER DASHBOARD</span>
                        <h3 style="color: #fff; font-size: 18px; font-weight: 700; margin: 6px 0 8px;">Real-Time Buyer Inquiries &amp; CRM Leads</h3>
                        <p style="color: #94a3b8; font-size: 13px; margin: 0;">See how member exporters receive instant notification alerts for newly posted buying requests.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# Clean Testimonial Grid HTML
clean_testimonials_grid_html = """  <!-- ============================================================ -->
  <!-- HIGHLIGHTED GLOBAL CLIENT VIDEO TESTIMONIALS -->
  <!-- ============================================================ -->
  <section style="padding: 60px 20px; background: #020617; text-align: center; border-top: 1px solid rgba(212,175,55,0.2); border-bottom: 1px solid rgba(212,175,55,0.2); margin-bottom: 50px;">
      <div style="max-width: 1240px; margin: 0 auto;">
          <span style="background: rgba(34, 197, 94, 0.15); color: #4ade80; padding: 6px 18px; border-radius: 30px; font-size: 0.8rem; font-weight: 800; border: 1px solid rgba(34, 197, 94, 0.4); text-transform: uppercase; letter-spacing: 1px;">VERIFIED SUCCESS STORIES</span>
          <h2 style="color: #fff; font-family: 'Outfit', sans-serif; font-size: 34px; font-weight: 800; margin: 15px 0 10px;">Hear From Our Global Exporters &amp; Buyers</h2>
          <p style="color: #94a3b8; font-size: 15px; max-width: 720px; margin: 0 auto 40px;">Real business owners and international trade directors sharing their experience with APD Global Trade.</p>

          <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(270px, 1fr)); gap: 20px; text-align: left;">
              
              <!-- 1. Rice Exporter (Indian Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Testimonial 2 Rice Exporter.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Rajesh Kumar</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">CEO, Punjab Grain Exports</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Rice Exporter</span>
                  </div>
              </div>

              <!-- 2. Spice Exporter (Indian Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial 3  Spice - Same face which was in Rice.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Suresh Patel</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Managing Director, Spices Unlimited</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Spice Exporter</span>
                  </div>
              </div>

              <!-- 3. Arabic Buyer (Arab Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial  11 Arabic.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Tariq Al-Mansoor</span> <span style="font-size: 14px;">🇦🇪</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Managing Director, Al-Mansoor Imports</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Dubai Buyer</span>
                  </div>
              </div>

              <!-- 4. Fox Nuts Exporter (Indian Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial  10 Hinglish_–_Fox_Nuts_Makhan.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Vikramaditya Roy</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Founder, Premium Makhana Exporters</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Fox Nuts Exporter</span>
                  </div>
              </div>

              <!-- 5. White Lady (UK Woman) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial  7 White Lady.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Sarah Jenkins</span> <span style="font-size: 14px;">🇬🇧</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Head of Sourcing, Euro Foods UK</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified UK Buyer</span>
                  </div>
              </div>

              <!-- 6. Spanish Buyer (Spanish Woman) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Testimonial 13 Spanish.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Elena Rostova</span> <span style="font-size: 14px;">🇪🇸</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Agri-Trading Director, Spain</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Europe Buyer</span>
                  </div>
              </div>

              <!-- 7. French Buyer (French Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Testimonial 12 French.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Jean-Luc Moreau</span> <span style="font-size: 14px;">🇫🇷</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Commodities Partner, France</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified European Buyer</span>
                  </div>
              </div>

              <!-- 8. Moringa Exporter (Indian Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial  8 Moringa Hindi.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Ramesh Verma</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Organic Moringa Exporter</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Herbal Exporter</span>
                  </div>
              </div>

              <!-- 9. Rice Bengali Exporter (Bengali Woman) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial  9 Rince Bengali.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Ananya Das</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">MD, Bengal Rice &amp; Grain Trade</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Rice Exporter</span>
                  </div>
              </div>

              <!-- 10. Portuguese Buyer (Portuguese Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Testimonial 14 Portuguese.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Mateus Silva</span> <span style="font-size: 14px;">🇵🇹</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Global Sourcing Director</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Portugal Buyer</span>
                  </div>
              </div>

              <!-- 11. Testimonial 4 (Gulf Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial 4.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Carlos Mendez</span> <span style="font-size: 14px;">🇦🇪</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Import Manager, Gulf Distributing</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Gulf Buyer</span>
                  </div>
              </div>

              <!-- 12. Testimonial 5 (Asian Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial 5.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>David Chen</span> <span style="font-size: 14px;">🇸🇬</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Commodities Buyer, Singapore</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Singapore Partner</span>
                  </div>
              </div>

              <!-- 13. Testimonial 6 (Indian Male Exporter) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Tesimonial 6.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Amit Sharma</span> <span style="font-size: 14px;">🇮🇳</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Agri Exporter, Haryana</p>
                      <span style="font-size: 11px; background: rgba(34, 197, 94, 0.2); color: #4ade80; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified Supplier Member</span>
                  </div>
              </div>

              <!-- 14. Testimonial (Arab Male) -->
              <div style="background: #0f172a; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; overflow: hidden; box-shadow: 0 8px 25px rgba(0,0,0,0.4);">
                  <div style="position: relative; width: 100%; padding-bottom: 56.25%; background: #000;">
                      <video controls playsinline webkit-playsinline preload="metadata" style="position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover;">
                          <source src="/assets/videos/Testimonial.mp4" type="video/mp4">
                      </video>
                  </div>
                  <div style="padding: 16px;">
                      <h4 style="color: #fff; font-size: 15px; font-weight: 700; margin: 0 0 4px; display: flex; align-items: center; justify-content: space-between;">
                          <span>Hassan Al-Zahrani</span> <span style="font-size: 14px;">🇸🇦</span>
                      </h4>
                      <p style="color: var(--gold); font-size: 12px; font-weight: 600; margin: 0 0 6px;">Food Logistics Partner, Saudi Arabia</p>
                      <span style="font-size: 11px; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Verified KSA Buyer</span>
                  </div>
              </div>

          </div>
      </div>
  </section>
"""

# Extract Official Business Identity section
part_after_identity = content.split("<!-- OFFICIAL BUSINESS IDENTITY SECTION -->")[1]

# Rebuild clean membership.html content!
new_membership_content = part_before_testimonials + clean_membership_demo_html + "\n" + clean_testimonials_grid_html + "\n<!-- OFFICIAL BUSINESS IDENTITY SECTION -->" + part_after_identity

with open(membership_path, "w", encoding="utf-8") as f:
    f.write(new_membership_content)

print("SUCCESS: Cleaned up membership.html HTML structure completely!")
