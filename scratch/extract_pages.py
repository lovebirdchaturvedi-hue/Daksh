from PyPDF2 import PdfReader, PdfWriter

# Open the 8-page PDF
input_pdf_path = r"C:\Users\DELL\Downloads\Offer_Letter_Ashish_Final_100000_Fixed.pdf"
output_pdf_path = r"C:\Users\DELL\Downloads\Offer_Letter_Ashish_1Lac_Perfect.pdf"

reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# The user wants to KEEP pages 1, 3, 5, 7 (which are indices 0, 2, 4, 6)
# And delete 2, 4, 6, 8 (indices 1, 3, 5, 7)
pages_to_keep = [0, 2, 4, 6]

for page_num in pages_to_keep:
    if page_num < len(reader.pages):
        writer.add_page(reader.pages[page_num])

# Save the final 4-page PDF
with open(output_pdf_path, "wb") as f:
    writer.write(f)

print(f"Saved perfectly extracted 4-page PDF to {output_pdf_path}")
