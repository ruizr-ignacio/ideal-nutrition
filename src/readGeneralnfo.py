import re

def extract_general_info(text):
    general_info = {}
    
    # Extract Name
    name_match = re.search(r'Nombre:\s*(.*?)\s*Fecha:', text)
    if name_match:
        general_info['name'] = name_match.group(1).strip()

    # Extract Date
    date_match = re.search(r'Fecha:\s*(.*?)\s*Objetivo:', text)
    if date_match:
        general_info['date'] = date_match.group(1).strip()

    # Extract Objective
    objective_match = re.search(r'Objetivo:\s*(.*?)\s*Próxima cita:', text)
    if objective_match:
        general_info['objective'] = objective_match.group(1).strip()

    # Extract Caloric Intake
    # Regex just works for 0,000 values
    caloric_intake_match = re.search(r'(\d{1,1}(?:,\d{3})?)\s+Calorías', text)
    if caloric_intake_match:
        caloric_intake = caloric_intake_match.group(1).strip()
        # Removing comma for numerical representation
        general_info['caloric_intake'] = caloric_intake.replace(',', '')

    # Macronutrients
    # Debugging: Print a portion of the text to understand its format
    # start_index = text.find('Proteínas')  # Adjust 'Proteínas' if the actual text is different
    # end_index = start_index + 50  # Adjust the range as needed
    # print(text[start_index-50:end_index])  # Print a portion of the text for inspection

    # proteins_match = re.search(r'Proteínas\s*\(\s*g\s*\)\s*(\d+\.?\d*)', text)
    # print('proteins_match', proteins_match)
    # if proteins_match:
    #     general_info['proteins'] = proteins_match.group(1).strip()

    # lipids_match = re.search(r'Lípidos\s*\(\s*g\s*\)\s*(\d+\.?\d*)', text)
    # print('lipids_match', lipids_match)
    # if lipids_match:
    #     general_info['lipids'] = lipids_match.group(1).strip()

    # carbohydrates_match = re.search(r'Hidratos de C\s*\(\s*g\s*\)\s*(\d+\.?\d*)', text)
    # if carbohydrates_match:
    #     general_info['carbohydrates'] = carbohydrates_match.group(1).strip()

    # general_info['macronutrients'] = {
    #     'proteins': proteins,
    #     'lipids': lipids,
    #     'carbohydrates': carbohydrates
    # }

    return general_info
