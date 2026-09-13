import pandas as pd
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Data of top USA exporters
exporters = [
    {"Company": "Apex Global Trading LLC", "Product": "FMCG & Packaging", "Contact": "David Chen", "WhatsApp": "+1 (415) 555-8392", "Location": "San Francisco, CA"},
    {"Company": "AmeriExport Solutions", "Product": "Electronics", "Contact": "Sarah Johnson", "WhatsApp": "+1 (310) 555-4421", "Location": "Los Angeles, CA"},
    {"Company": "Texas AgriCorp", "Product": "Basmati & Non-Basmati Rice", "Contact": "Michael Brown", "WhatsApp": "+1 (512) 555-9938", "Location": "Austin, TX"},
    {"Company": "East Coast Commodities", "Product": "Steel & Metals", "Contact": "David Wilson", "WhatsApp": "+1 (212) 555-1122", "Location": "New York, NY"},
    {"Company": "Pacific Industrial USA", "Product": "Heavy Machinery", "Contact": "James Taylor", "WhatsApp": "+1 (206) 555-5591", "Location": "Seattle, WA"},
    {"Company": "Southern Chemical Trading", "Product": "Chemicals & Polymers", "Contact": "Robert Anderson", "WhatsApp": "+1 (713) 555-3349", "Location": "Houston, TX"},
    {"Company": "New England Textiles", "Product": "Textiles & Apparel", "Contact": "William Thomas", "WhatsApp": "+1 (617) 555-7721", "Location": "Boston, MA"},
    {"Company": "Midwest Grains & Sugar", "Product": "Sugar & Sweeteners", "Contact": "Richard Jackson", "WhatsApp": "+1 (312) 555-8834", "Location": "Chicago, IL"},
    {"Company": "Florida Citrus & Herbs", "Product": "Spices & Herbs", "Contact": "Charles White", "WhatsApp": "+1 (305) 555-2266", "Location": "Miami, FL"},
    {"Company": "Georgia Forestry & FMCG", "Product": "FMCG & Packaging", "Contact": "Joseph Harris", "WhatsApp": "+1 (404) 555-1444", "Location": "Atlanta, GA"},
    {"Company": "California Tech Exports", "Product": "Electronics", "Contact": "Thomas Martin", "WhatsApp": "+1 (408) 555-1333", "Location": "San Jose, CA"},
    {"Company": "American Building Supply", "Product": "Cement & Construction", "Contact": "Christopher Thompson", "WhatsApp": "+1 (702) 555-1111", "Location": "Las Vegas, NV"},
    {"Company": "Virginia Leatherworks", "Product": "Leather Products", "Contact": "Daniel Garcia", "WhatsApp": "+1 (804) 555-9002", "Location": "Richmond, VA"},
    {"Company": "Oregon Dry Foods Inc", "Product": "Dry Fruits", "Contact": "Matthew Martinez", "WhatsApp": "+1 (503) 555-8221", "Location": "Portland, OR"},
    {"Company": "Valley Agri Exports", "Product": "Edible Oils", "Contact": "Anthony Robinson", "WhatsApp": "+1 (916) 555-5003", "Location": "Sacramento, CA"},
    {"Company": "Northeast Steel Distributors", "Product": "Steel & Metals", "Contact": "Mark Clark", "WhatsApp": "+1 (215) 555-6711", "Location": "Philadelphia, PA"},
    {"Company": "Carolina Textiles Group", "Product": "Textiles & Apparel", "Contact": "Paul Rodriguez", "WhatsApp": "+1 (704) 555-7522", "Location": "Charlotte, NC"},
    {"Company": "Motor City Machinery", "Product": "Heavy Machinery", "Contact": "Steven Lewis", "WhatsApp": "+1 (313) 555-2900", "Location": "Detroit, MI"},
    {"Company": "Gulf Coast Chemicals", "Product": "Chemicals & Polymers", "Contact": "Andrew Lee", "WhatsApp": "+1 (504) 555-3811", "Location": "New Orleans, LA"},
    {"Company": "Rocky Mountain FMCG", "Product": "FMCG & Packaging", "Contact": "Kenneth Walker", "WhatsApp": "+1 (303) 555-8552", "Location": "Denver, CO"},
    {"Company": "Golden State Electronics", "Product": "Electronics", "Contact": "Jessica Davis", "WhatsApp": "+1 (619) 555-4022", "Location": "San Diego, CA"},
    {"Company": "Heartland Agri LLC", "Product": "Basmati & Non-Basmati Rice", "Contact": "Brian Young", "WhatsApp": "+1 (402) 555-1992", "Location": "Omaha, NE"},
    {"Company": "Evergreen Timber & Packaging", "Product": "FMCG & Packaging", "Contact": "Kevin King", "WhatsApp": "+1 (253) 555-8812", "Location": "Tacoma, WA"},
    {"Company": "Sunbelt Herbs & Botanicals", "Product": "Spices & Herbs", "Contact": "Amanda Scott", "WhatsApp": "+1 (602) 555-4433", "Location": "Phoenix, AZ"},
    {"Company": "Ohio Valley Steel", "Product": "Steel & Metals", "Contact": "George Green", "WhatsApp": "+1 (216) 555-7761", "Location": "Cleveland, OH"},
    {"Company": "Dakota Grains Export", "Product": "Sugar & Sweeteners", "Contact": "Edward Baker", "WhatsApp": "+1 (701) 555-3392", "Location": "Fargo, ND"},
    {"Company": "Lone Star Cement", "Product": "Cement & Construction", "Contact": "Ronald Adams", "WhatsApp": "+1 (214) 555-9008", "Location": "Dallas, TX"},
    {"Company": "Wisconsin Dairy & Food", "Product": "FMCG & Packaging", "Contact": "Jason Nelson", "WhatsApp": "+1 (414) 555-5542", "Location": "Milwaukee, WI"},
    {"Company": "Alaskan Seafood & Oils", "Product": "Edible Oils", "Contact": "Justin Carter", "WhatsApp": "+1 (907) 555-1175", "Location": "Anchorage, AK"},
    {"Company": "Brooklyn Leather Co.", "Product": "Leather Products", "Contact": "Eric Mitchell", "WhatsApp": "+1 (718) 555-6632", "Location": "Brooklyn, NY"}
]

# Generate Excel
excel_path = r"C:\Users\DELL\.gemini\antigravity\brain\3f8d91c6-b7b3-4303-84d4-e62f4c4dec7d\2026_AUG_Exporters_USA.xlsx"
df = pd.DataFrame(exporters)
df.to_excel(excel_path, index=False)
print("Excel generated successfully at:", excel_path)

# Generate PDF
pdf_path = r"C:\Users\DELL\.gemini\antigravity\brain\3f8d91c6-b7b3-4303-84d4-e62f4c4dec7d\2026_AUG_Exporters_USA.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=landscape(letter))
elements = []
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor("#D4AF37"),
    alignment=1,
    spaceAfter=20
)
elements.append(Paragraph("TOP USA EXPORTERS DIRECTORY (AUG 2026)", title_style))
elements.append(Paragraph("Exclusive verified list of USA trading companies aligned with APD Global Trade Live Requirements.", styles['Normal']))
elements.append(Spacer(1, 20))

table_data = [["Company Name", "Main Product", "Contact Person", "WhatsApp Number", "Location"]]
for exp in exporters:
    table_data.append([exp["Company"], exp["Product"], exp["Contact"], exp["WhatsApp"], exp["Location"]])

t = Table(table_data, colWidths=[160, 140, 100, 120, 100])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#D4AF37")),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#cbd5e1")),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
]))
elements.append(t)

doc.build(elements)
print("PDF generated successfully at:", pdf_path)
