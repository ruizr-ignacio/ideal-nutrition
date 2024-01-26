import fitz  # PyMuPDF

def extract_text_from_pdf_fitz(pdf_path, page_number):
    # Open the PDF file
    document = fitz.open(pdf_path)
    # Extract text from the specified page
    page_text = document[page_number].get_text()
    document.close()
    
    return page_text
