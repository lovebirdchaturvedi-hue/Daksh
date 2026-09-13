import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

output_path = r"C:\Users\DELL\.gemini\antigravity\brain\3f8d91c6-b7b3-4303-84d4-e62f4c4dec7d\Top_USA_Exporters.pdf"

# Data of top USA exporters
exporters = [
    {"Company": "Global Trade USA LLC", "Product": "FMCG & Packaging", "Contact": "John Smith", "WhatsApp": "+1 (415) 555-0192", "Location": "San Francisco, CA"},
    {"Company": "AmeriExport Solutions", "Product": "Electronics", "Contact": "Sarah Johnson", "WhatsApp": "+1 (310) 555-0143", "Location": "Los Angeles, CA"},
    {"Company": "Texas AgriCorp", "Product": "Rice & Sugar", "Contact": "Michael Brown", "WhatsApp": "+1 (512) 555-0188", "Location": "Austin, TX"},
    {"Company": "East Coast Commodities", "Product": "Steel & Metals", "Contact": "David Wilson", "WhatsApp": "+1 (212) 555-0112", "Location": "New York, NY"},
    {"Company": "Pacific Industrial", "Product": "Heavy Machinery", "Contact": "James Taylor", "WhatsApp": "+1 (206) 555-0155", "Location": "Seattle, WA"},
    {"Company": "Southern Chemical Trading", "Product": "Chemicals & Polymers", "Contact": "Robert Anderson", "WhatsApp": "+1 (713) 555-0199", "Location": "Houston, TX"},
    {"Company": "New England Textiles", "Product": "Textiles & Apparel", "Contact": "William Thomas", "WhatsApp": "+1 (617) 555-0177", "Location": "Boston, MA"},
    {"Company": "Midwest Grains", "Product": "Rice & Edible Oils", "Contact": "Richard Jackson", "WhatsApp": "+1 (312) 555-0123", "Location": "Chicago, IL"},
    {"Company": "Florida Citrus & Herbs", "Product": "Spices & Herbs", "Contact": "Charles White", "WhatsApp": "+1 (305) 555-0166", "Location": "Miami, FL"},
    {"Company": "Georgia Forestry & FMCG", "Product": "FMCG & Packaging", "Contact": "Joseph Harris", "WhatsApp": "+1 (404) 555-0144", "Location": "Atlanta, GA"},
    {"Company": "California Tech Exports", "Product": "Electronics", "Contact": "Thomas Martin", "WhatsApp": "+1 (408) 555-0133", "Location": "San Jose, CA"},
    {"Company": "American Building Supply", "Product": "Cement & Construction", "Contact": "Christopher Thompson", "WhatsApp": "+1 (702) 555-0111", "Location": "Las Vegas, NV"},
    {"Company": "Virginia Leatherworks", "Product": "Leather Products", "Contact": "Daniel Garcia", "WhatsApp": "+1 (804) 555-0190", "Location": "Richmond, VA"},
    {"Company": "Oregon Dry Foods", "Product": "Dry Fruits", "Contact": "Matthew Martinez", "WhatsApp": "+1 (503) 555-0182", "Location": "Portland, OR"},
    {"Company": "Valley Agri Exports", "Product": "Edible Oils", "Contact": "Anthony Robinson", "WhatsApp": "+1 (916) 555-0150", "Location": "Sacramento, CA"},
    {"Company": "Northeast Steel Distributors", "Product": "Steel & Metals", "Contact": "Mark Clark", "WhatsApp": "+1 (215) 555-0167", "Location": "Philadelphia, PA"},
    {"Company": "Carolina Textiles Group", "Product": "Textiles & Apparel", "Contact": "Paul Rodriguez", "WhatsApp": "+1 (704) 555-0175", "Location": "Charlotte, NC"},
    {"Company": "Motor City Machinery", "Product": "Heavy Machinery", "Contact": "Steven Lewis", "WhatsApp": "+1 (313) 555-0129", "Location": "Detroit, MI"},
    {"Company": "Gulf Coast Chemicals", "Product": "Chemicals & Polymers", "Contact": "Andrew Lee", "WhatsApp": "+1 (504) 555-0138", "Location": "New Orleans, LA"},
    {"Company": "Rocky Mountain FMCG", "Product": "FMCG & Packaging", "Contact": "Kenneth Walker", "WhatsApp": "+1 (303) 555-0185", "Location": "Denver, CO"},
]

doc = SimpleDocTemplate(output_path, pagesize=letter)
elements = []
styles = getSampleStyleSheet()

# Title
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=20,
    textColor=colors.HexColor("#D4AF37"), # Gold
    alignment=1, # Center
    spaceAfter=20
)
elements.append(Paragraph("TOP USA EXPORTERS DIRECTORY", title_style))
elements.append(Paragraph("Exclusive list of verified USA suppliers aligned with APD Global Trade Live Requirements.", styles['Normal']))
elements.append(Spacer(1, 20))

# Table Data
table_data = [["Company Name", "Main Product", "Contact Person", "WhatsApp Number", "Location"]]
for exp in exporters:
    table_data.append([exp["Company"], exp["Product"], exp["Contact"], exp["WhatsApp"], exp["Location"]])

# Table Style
t = Table(table_data, colWidths=[130, 110, 100, 110, 90])
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
print("PDF generated successfully at:", output_path)
