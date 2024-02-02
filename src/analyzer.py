import PyPDF2

from readGeneralnfo import extract_general_info
from readMeasurements import extract_physical_measurements
# from extractPage import extract_text_from_pdf_fitz
from readTable import parse_meal_plan
from pdf_helpers import extract_text_from_pdf_fitz

def extract_pdf_info(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        page1_text = reader.pages[0].extract_text()
        page2_text = reader.pages[1].extract_text()
        page3_text = reader.pages[2].extract_text()

        # Process the text to extract relevant information
        general_info = extract_general_info(page1_text)
        physical_measurements = extract_physical_measurements(page2_text)

    page3_text = extract_text_from_pdf_fitz(file_path, 2)
    meals = parse_meal_plan(page3_text)

    return general_info, physical_measurements, meals
