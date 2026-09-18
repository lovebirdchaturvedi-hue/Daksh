import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Quick Links SEO Footer
quick_links = """
<div class="seo-quick-links" style="background: #000; padding: 40px 8%; border-top: 1px solid rgba(255,255,255,0.1); color: #64748b; font-size: 13px; line-height: 1.8;">
    <div class="container">
        <h4 style="color: #fff; margin-bottom: 20px; font-family: 'Outfit', sans-serif; font-size: 20px;">Quick Links &amp; Popular Searches</h4>
        <div style="margin-bottom: 15px;">
            <strong style="color: #94a3b8;">Agro Commodity:</strong> 
            <a href="#" style="color: #64748b; text-decoration: none;">Basmati Rice</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Wheat</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Long Grain Rice</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Sugar</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Spices</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Pulses</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Edible Oils</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Dry Fruits</a>
        </div>
        <div style="margin-bottom: 15px;">
            <strong style="color: #94a3b8;">Top Searches:</strong> 
            <a href="#" style="color: #64748b; text-decoration: none;">Buy Rice in Bulk</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Rice Importers in Saudi Arabia</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Brazilian Sugar Exporters</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Export Agro Industries</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Top 10 Cement Manufacturers</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Steel Billets Export</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Best Spice Exporter in India</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Sella Basmati Rice</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Wheat Importing Countries</a>
        </div>
        <div style="margin-bottom: 15px;">
            <strong style="color: #94a3b8;">Spices &amp; Pulses:</strong> 
            <a href="#" style="color: #64748b; text-decoration: none;">Black Pepper</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Cumin Seeds</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Turmeric</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Red Chilli</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Red Kidney Beans</a> | 
            <a href="#" style="color: #64748b; text-decoration: none;">Chickpeas</a>
        </div>
    </div>
</div>
"""

# 2. Business Associate Partners
partners_html = """
<section style="padding: 50px 8%; background: #0f172a; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05);">
    <h3 style="color: #94a3b8; font-size: 16px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 40px;">Business Associate Partners</h3>
    <div style="display: flex; gap: 50px; justify-content: center; flex-wrap: wrap; opacity: 0.5; filter: grayscale(100%); align-items: center;">
        <h2 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 28px; margin:0;">KRBL Limited</h2>
        <h2 style="color: #fff; font-family: 'Arial', sans-serif; font-size: 28px; font-weight: 900; margin:0;">WONDER CEMENT</h2>
        <h2 style="color: #fff; font-family: 'Times New Roman', serif; font-size: 28px; font-style: italic; margin:0;">Al Maha Foods</h2>
        <h2 style="color: #fff; font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; margin:0;">SAIL</h2>
        <h2 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 28px; margin:0;">GLOBAL AGRO</h2>
    </div>
</section>
"""

# 3. Recent Blogs / Insights
blogs_html = """
<section style="padding: 80px 8%; background: #020617;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <h2 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 36px; margin-bottom: 15px;">Recent Blogs &amp; Market Insights</h2>
            <p style="color: #94a3b8; font-size: 1.1rem;">Stay updated with global trade trends and commodity analytics.</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            
            <div style="background: #0f172a; border-radius: 15px; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); transition: 0.3s; cursor: pointer;">
                <div style="height: 200px; background: url('https://images.unsplash.com/photo-1586201375761-83865001e8ac?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover;"></div>
                <div style="padding: 25px;">
                    <span style="color: var(--gold); font-size: 12px; font-weight: 700; text-transform: uppercase;">Rice Export</span>
                    <h3 style="color: #fff; font-size: 20px; margin: 10px 0 15px; font-family: 'Outfit', sans-serif;">Buy Sella Basmati Rice in Bulk from Verified Indian Suppliers</h3>
                    <div style="color: #64748b; font-size: 13px; display: flex; justify-content: space-between;">
                        <span>By Trade Analytics</span>
                        <span>18-Sep-2026</span>
                    </div>
                </div>
            </div>

            <div style="background: #0f172a; border-radius: 15px; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); transition: 0.3s; cursor: pointer;">
                <div style="height: 200px; background: url('https://images.unsplash.com/photo-1621317581373-f931d8c1c4f5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover;"></div>
                <div style="padding: 25px;">
                    <span style="color: var(--gold); font-size: 12px; font-weight: 700; text-transform: uppercase;">Pulses &amp; Beans</span>
                    <h3 style="color: #fff; font-size: 20px; margin: 10px 0 15px; font-family: 'Outfit', sans-serif;">Global Shortage: Procuring Red Kidney Beans for Middle East Markets</h3>
                    <div style="color: #64748b; font-size: 13px; display: flex; justify-content: space-between;">
                        <span>By Trade Analytics</span>
                        <span>16-Sep-2026</span>
                    </div>
                </div>
            </div>

            <div style="background: #0f172a; border-radius: 15px; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); transition: 0.3s; cursor: pointer;">
                <div style="height: 200px; background: url('https://images.unsplash.com/photo-1542838132-92c53300491e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80') center/cover;"></div>
                <div style="padding: 25px;">
                    <span style="color: var(--gold); font-size: 12px; font-weight: 700; text-transform: uppercase;">Market Trends</span>
                    <h3 style="color: #fff; font-size: 20px; margin: 10px 0 15px; font-family: 'Outfit', sans-serif;">Indian Agri Exports to Global Markets: 2026 Q4 Forecast</h3>
                    <div style="color: #64748b; font-size: 13px; display: flex; justify-content: space-between;">
                        <span>By Trade Analytics</span>
                        <span>12-Sep-2026</span>
                    </div>
                </div>
            </div>

        </div>
    </div>
</section>
"""

# Inject Partners and Blogs above Global Banking Partners
idx_banking = text.find('Global Banking Partners')
if idx_banking != -1:
    section_start = text.rfind('<section', 0, idx_banking)
    if section_start != -1:
        text = text[:section_start] + partners_html + '\n' + blogs_html + '\n' + text[section_start:]
        print('Injected Partners and Blogs above Global Banking Partners')

# Inject Quick links above footer
idx_footer = text.find('<footer')
if idx_footer != -1:
    text = text[:idx_footer] + quick_links + '\n' + text[idx_footer:]
    print('Injected Quick Links above Footer')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html!')
