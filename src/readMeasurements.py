import re

def extract_physical_measurements(text):
    measurements = {}

    measurements['weight'] = re.search(r'Peso\s+\(kg\)\s+(\d+\.?\d*)', text).group(1).strip()
    measurements['body_fat_percentage'] = re.search(r'% Grasa\s+(\d+\.?\d*)', text).group(1).strip()
    measurements['lean_mass'] = re.search(r'Masa magra\s+\(kg\)\s+(\d+\.?\d*)', text).group(1).strip()
    measurements['bone_mass'] = re.search(r'Masa ósea\s+\(kg\)\s+(\d+\.?\d*)', text).group(1).strip()

    # Circumferences and Skinfold Measurements
    circumferences = {
        'flexed_arm': re.search(r'Brazo flexionado:\s+(\d+\.?\d*)cm', text).group(1).strip(),
        'relaxed_arm': re.search(r'Brazo relajado:\s+(\d+\.?\d*)cm', text).group(1).strip(),
        'waist': re.search(r'Cintura:\s+(\d+\.?\d*)cm', text).group(1).strip(),
        'hip': re.search(r'Cadera:\s+(\d+\.?\d*)cm', text).group(1).strip(),
        'mid_thigh': re.search(r'Muslo medio:\s+(\d+\.?\d*)cm', text).group(1).strip(),
        'leg': re.search(r'Pierna:\s+(\d+\.?\d*)cm', text).group(1).strip()
    }

    skinfold_measurements = {
        'biceps': re.search(r'Bíceps:\s+(\d+\.?\d*)mm', text).group(1).strip(),
        'iliac_crest': re.search(r'Cresta Ilíaca:\s+(\d+\.?\d*)mm', text).group(1).strip(),
        'subscapular': re.search(r'Subescapular:\s+(\d+\.?\d*)mm', text).group(1).strip(),
        'triceps': re.search(r'Tríceps:\s+(\d+\.?\d*)mm', text).group(1).strip(),
        'medial_leg': re.search(r'Pierna medial:\s+(\d+\.?\d*)mm', text).group(1).strip()
    }

    measurements['circumferences'] = circumferences
    measurements['skinfold_measurements'] = skinfold_measurements

    return measurements
