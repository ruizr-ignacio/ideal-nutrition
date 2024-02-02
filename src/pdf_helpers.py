import fitz
import json
import os

def extract_text_from_pdf_fitz(file_path, page_number):
    # Open the PDF file
    document = fitz.open(file_path)
    # Extract text from the specified page
    page_text = document[page_number].get_text()
    document.close()

    return page_text

def safeFile(file_name, json_data):
    directory = os.path.dirname(__file__) + '/output/'
    file_path = directory + file_name + '.json'

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)
