import re

def extract_general_info(text):
    general_info = {}
    general_info['name'] = re.search(r'Nombre:\s+(.*)', text).group(1).strip()
    general_info['date'] = re.search(r'Fecha:\s+(.*)', text).group(1).strip()
    general_info['objective'] = re.search(r'Objetivo:\s+(.*)Próxima cita', text).group(1).strip()
    general_info['caloric_intake'] = re.search(r'(\d+)\s+Calorías', text).group(1).strip()
    
    # Macronutrients
    proteins = re.search(r'Proteínas\s+\(g\)\s+(\d+\.?\d*)', text).group(1).strip()
    lipids = re.search(r'Lípidos\s+\(g\)\s+(\d+\.?\d*)', text).group(1).strip()
    carbohydrates = re.search(r'Hidratos de C\s+\(g\)\s+(\d+\.?\d*)', text).group(1).strip()

    general_info['macronutrients'] = {
        'proteins': proteins,
        'lipids': lipids,
        'carbohydrates': carbohydrates
    }

    return general_info
