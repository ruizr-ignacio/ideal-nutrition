import fitz
import json
import os
# import unicodedata

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

# def remove_accents(input_str):
#     # Normalize the Unicode string and decompose the accents
#     nfkd_form = unicodedata.normalize('NFKD', input_str)
#     # Return the string with base characters only
#     return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

# def process_json(data):
#     if isinstance(data, dict):
#         return {key: process_json(value) for key, value in data.items()}
#     elif isinstance(data, list):
#         return [process_json(element) for element in data]
#     elif isinstance(data, str):
#         return remove_accents(data)
#     else:
#         return data
