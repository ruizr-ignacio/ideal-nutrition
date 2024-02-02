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

    return general_info
