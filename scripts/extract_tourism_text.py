import pdfplumber

# Path to the PDF file you moved
pdf_path = "data/tourism.pdf"

# Extract text from the PDF
with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()

# Save the extracted text to a file for later processing
with open("data/extracted_tourism_text.txt", "w") as file:
    file.write(full_text)

print("Text extraction completed! Saved to 'data/extracted_tourism_text.txt'")
