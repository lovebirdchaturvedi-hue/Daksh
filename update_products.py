import os
import re

def update_products():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the start of the pricing section
    start_marker = '<section id="pricing"'
    # Find the start of the next section
    end_marker = '<!-- HOW IT WORKS (MODERNIZED) -->'
    
    if start_marker in html and end_marker in html:
        before = html.split(start_marker)[0]
        after = end_marker + html.split(end_marker, 1)[1]
        
        product_grid_html = '''
    <!-- LIVE MARKETPLACE PRODUCT GRID -->
    <section id="marketplace-products" style="padding: 100px 8%; background: #020617; color: white;">
        <div class="container">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 40px; flex-wrap: wrap; gap: 20px;">
                <div>
                    <h2 style="font-size: 2.5rem; margin-bottom: 10px; font-family: 'Playfair Display', serif;">Live Trade Liquidity</h2>
                    <p style="color: #94a3b8; font-size: 1.1rem; max-width: 600px;">Explore verified active wholesale commodities ready for immediate global export.</p>
                </div>
                <a href="/suppliers.html" style="color: var(--gold); font-weight: 700; text-decoration: none; border: 1px solid var(--gold); padding: 10px 20px; border-radius: 30px; transition: 0.3s;" onmouseover="this.style.background='var(--gold)'; this.style.color='#000';" onmouseout="this.style.background='transparent'; this.style.color='var(--gold)';">View All Commodities →</a>
            </div>

            <style>
                .product-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 25px;
                }
                .product-card {
                    background: rgba(15, 23, 42, 0.6);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 12px;
                    overflow: hidden;
                    transition: all 0.3s ease;
                    position: relative;
                }
                .product-card:hover {
                    transform: translateY(-10px);
                    border-color: rgba(212, 175, 55, 0.5);
                    box-shadow: 0 15px 30px rgba(0,0,0,0.5), 0 0 20px rgba(212, 175, 55, 0.1);
                }
                .product-img {
                    width: 100%;
                    height: 200px;
                    object-fit: cover;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
                }
                .verified-badge {
                    position: absolute;
                    top: 15px;
                    right: 15px;
                    background: rgba(2, 6, 23, 0.8);
                    backdrop-filter: blur(5px);
                    border: 1px solid #22c55e;
                    color: #22c55e;
                    padding: 4px 10px;
                    border-radius: 20px;
                    font-size: 0.7rem;
                    font-weight: 800;
                    display: flex;
                    align-items: center;
                    gap: 5px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
                }
                .product-content {
                    padding: 20px;
                }
                .product-category {
                    color: #94a3b8;
                    font-size: 0.75rem;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    margin-bottom: 5px;
                }
                .product-title {
                    font-size: 1.1rem;
                    font-weight: 700;
                    margin-bottom: 15px;
                    line-height: 1.4;
                    color: #fff;
                }
                .product-meta {
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 10px;
                    font-size: 0.85rem;
                }
                .product-meta-label { color: #64748b; }
                .product-meta-value { color: #e2e8f0; font-weight: 600; }
                .product-price {
                    font-size: 1.2rem;
                    font-weight: 900;
                    color: var(--gold);
                    margin-bottom: 20px;
                    padding-bottom: 15px;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
                }
                .inquire-btn {
                    display: block;
                    width: 100%;
                    text-align: center;
                    background: linear-gradient(90deg, #1e293b, #0f172a);
                    border: 1px solid rgba(212, 175, 55, 0.3);
                    color: var(--gold);
                    padding: 12px;
                    border-radius: 8px;
                    font-weight: 700;
                    text-decoration: none;
                    transition: 0.3s;
                }
                .product-card:hover .inquire-btn {
                    background: var(--gold);
                    color: #000;
                }
            </style>

            <div class="product-grid">
                <!-- Card 1 -->
                <div class="product-card">
                    <div class="verified-badge">🛡️ Govt Verified</div>
                    <img src="https://images.unsplash.com/photo-1586201375761-83865001e8ac?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="1121 Basmati Rice" class="product-img">
                    <div class="product-content">
                        <div class="product-category">Agro • Grains</div>
                        <h3 class="product-title">Premium 1121 Sella Basmati Rice (XXL)</h3>
                        <div class="product-meta">
                            <span class="product-meta-label">Origin:</span>
                            <span class="product-meta-value">Mundra Port, India</span>
                        </div>
                        <div class="product-meta">
                            <span class="product-meta-label">MOQ:</span>
                            <span class="product-meta-value">25 MT (1 FCL)</span>
                        </div>
                        <div class="product-price">FOB $890 - $940 / MT</div>
                        <a href="https://chat.whatsapp.com/BRSKIkuYO6LCVM2WhRyczq" target="_blank" class="inquire-btn">Inquire Now</a>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="product-card">
                    <div class="verified-badge">🛡️ Govt Verified</div>
                    <img src="https://images.unsplash.com/photo-1596647413665-2b47d0d0249f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Refined Sugar ICUMSA 45" class="product-img">
                    <div class="product-content">
                        <div class="product-category">Agro • Sugar</div>
                        <h3 class="product-title">Refined Sugar ICUMSA 45 (White)</h3>
                        <div class="product-meta">
                            <span class="product-meta-label">Origin:</span>
                            <span class="product-meta-value">Nhava Sheva, India</span>
                        </div>
                        <div class="product-meta">
                            <span class="product-meta-label">MOQ:</span>
                            <span class="product-meta-value">100 MT</span>
                        </div>
                        <div class="product-price">FOB $460 - $480 / MT</div>
                        <a href="https://chat.whatsapp.com/BRSKIkuYO6LCVM2WhRyczq" target="_blank" class="inquire-btn">Inquire Now</a>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="product-card">
                    <div class="verified-badge">🛡️ Govt Verified</div>
                    <img src="https://images.unsplash.com/photo-1621213076722-19eeb6f1eaf7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Cumin Seeds" class="product-img">
                    <div class="product-content">
                        <div class="product-category">Agro • Spices</div>
                        <h3 class="product-title">Organic Whole Cumin Seeds (Jeera)</h3>
                        <div class="product-meta">
                            <span class="product-meta-label">Origin:</span>
                            <span class="product-meta-value">Kandla Port, India</span>
                        </div>
                        <div class="product-meta">
                            <span class="product-meta-label">MOQ:</span>
                            <span class="product-meta-value">14 MT</span>
                        </div>
                        <div class="product-price">FOB $3,100 - $3,300 / MT</div>
                        <a href="https://chat.whatsapp.com/BRSKIkuYO6LCVM2WhRyczq" target="_blank" class="inquire-btn">Inquire Now</a>
                    </div>
                </div>

                <!-- Card 4 -->
                <div class="product-card">
                    <div class="verified-badge">🛡️ Govt Verified</div>
                    <img src="https://images.unsplash.com/photo-1595187127453-6258071869de?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="CM Husk Powder" class="product-img">
                    <div class="product-content">
                        <div class="product-category">Agro • Feed</div>
                        <h3 class="product-title">CM Husk Powder (Cattle Feed Grade)</h3>
                        <div class="product-meta">
                            <span class="product-meta-label">Origin:</span>
                            <span class="product-meta-value">Kolkata Port, India</span>
                        </div>
                        <div class="product-meta">
                            <span class="product-meta-label">MOQ:</span>
                            <span class="product-meta-value">20 MT</span>
                        </div>
                        <div class="product-price">FOB $150 - $180 / MT</div>
                        <a href="https://chat.whatsapp.com/BRSKIkuYO6LCVM2WhRyczq" target="_blank" class="inquire-btn">Inquire Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    '''
        html = before + product_grid_html + "\n" + after
        print("Pricing section successfully replaced with Product Grid.")
    else:
        print("Markers not found!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_products()
