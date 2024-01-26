import os
from pdf_helpers import safeFile
from analyzer import extract_pdf_info

def main():    
    # Path to your PDF file
    file_path = os.path.dirname(__file__) + '/input/2023-08-IgnacioRuiz.pdf'

    # Extract information
    general_info, physical_measurements, meals = extract_pdf_info(file_path)

    data = {
        "general_info": general_info,
        "physical_measurements": physical_measurements,
        "meals": meals
    }
    safeFile('output', data)


main()
