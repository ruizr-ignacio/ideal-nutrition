import PyPDF2

def extract_pdf_info(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

        # Extract text from the first two pages
        page1_text = reader.getPage(0).extractText()
        page2_text = reader.getPage(1).extractText()

        # Process the text to extract relevant information
        general_info = extract_general_info(page1_text)
        physical_measurements = extract_physical_measurements(page2_text)

        return general_info, physical_measurements

# Path to your PDF file
file_path = '/input/2023-08-IgnacioRuiz.pdf'

# Extract information
general_info, physical_measurements = extract_pdf_info(file_path)

print("General Information:", general_info)
print("Physical Measurements:", physical_measurements)
