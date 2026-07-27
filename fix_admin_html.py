import re

with open("admin-crm.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add sidebar item
old_sidebar = """<div class="sidebar-item" onclick="showPanel('broadcast')">📢 WhatsApp Broadcaster</div>"""
new_sidebar = """<div class="sidebar-item" onclick="showPanel('broadcast')">📢 WhatsApp Broadcaster</div>
        <div class="sidebar-item" onclick="showPanel('rfqs')">🛍️ Buyer RFQ Management</div>"""

content = content.replace(old_sidebar, new_sidebar)

# 2. Add RFQ Panel
old_panel_end = """<!-- 👥 DATABASE -->"""

new_rfq_panel = """
            <!-- 🛍️ RFQ MANAGEMENT -->
            <div id="rfqsPanel" class="panel" style="display: none;">
                <h3 style="color: var(--crm-gold); margin-top: 0;">🛍️ Buyer RFQ Management</h3>
                <p style="font-size: 12px; color: #8b949e;">Manually inject real verified leads into the live supplier portal.</p>
                
                <div class="broadcast-panel">
                    <h4 style="color: #fff; margin-top: 0; margin-bottom:15px;">Inject Manual Buyer RFQ</h4>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                        <input type="text" id="rfqCompany" placeholder="Buyer / Company Name (e.g. ALGERO-LIBYA/TRADE_EXPORT)">
                        <input type="text" id="rfqPhone" placeholder="Contact Number (e.g. +218 93-0259378)">
                        <input type="text" id="rfqProduct" placeholder="Commodity Required (e.g. Edible Oil)">
                        <input type="text" id="rfqQty" placeholder="Quantity (e.g. 5x20ft Containers)">
                        <input type="text" id="rfqDest" placeholder="Destination Port (e.g. Dakar Port, Senegal)">
                        <select id="rfqIsSynthetic">
                            <option value="false">✅ REAL VERIFIED LEAD</option>
                            <option value="true">🤖 Synthetic/Generated Lead</option>
                        </select>
                    </div>
                    <button onclick="injectManualRfq()" class="btn-gold" style="width: 100%; padding: 15px; border-radius: 8px;">PUSH RFQ TO LIVE PORTAL</button>
                    <div id="rfqInjectStatus" style="margin-top: 15px; color: #16a34a; font-size: 13px; text-align:center;"></div>
                </div>

                <div class="grid-header" style="grid-template-columns: 2fr 1fr 1fr 1fr 1fr;">
                    <div>Buyer / Commodity</div>
                    <div>Quantity</div>
                    <div>Destination</div>
                    <div>Lead Type</div>
                    <div>Status</div>
                </div>
                <div id="rfqAdminList">
                    <div style="padding: 40px; text-align: center; color: #8b949e;">Loading Active RFQs...</div>
                </div>
            </div>

            <!-- 👥 DATABASE -->"""

content = content.replace(old_panel_end, new_rfq_panel)

with open("admin-crm.html", "w", encoding="utf-8") as f:
    f.write(content)

print("admin-crm.html updated successfully!")
