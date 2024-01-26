import re

def extract_physical_measurements(text):
    measurements = {}

    weight_match = re.search(r'Peso\s*\(\s*kg\s*\)\s*(\d+\.\d+)', text)
    if weight_match:
        measurements['weight'] = weight_match.group(1).strip()

    body_fat_match = re.search(r'%\s*Grasa\s*(\d+\.\d+)', text)
    if body_fat_match:
        measurements['body_fat_percentage'] = body_fat_match.group(1).strip()

    lean_mass_match = re.search(r'Masa\s*magra\s*\(\s*kg\s*\)\s*(\d+\.\d+)', text)
    if lean_mass_match:
        measurements['lean_mass'] = lean_mass_match.group(1).strip()

    bone_mass_match = re.search(r'Masa\s*ósea\s*\(\s*kg\s*\)\s*(\d+\.\d+)', text)
    if bone_mass_match:
        measurements['bone_mass'] = bone_mass_match.group(1).strip()

    # Circumferences
    circumferences = {}

    flexed_arm_match = re.search(r'Brazo flexionado\s*:\s*(\d+\.?\d*)\s*cm', text)
    if flexed_arm_match:
        circumferences['flexed_arm'] = flexed_arm_match.group(1).strip()

    relaxed_arm_match = re.search(r'Brazo relajado\s*:\s*(\d+\.?\d*)\s*cm', text)
    if relaxed_arm_match:
        circumferences['relaxed_arm'] = relaxed_arm_match.group(1).strip()

    waist_match = re.search(r'Cintura\s*:\s*(\d+\.?\d*)\s*cm', text)
    if waist_match:
        circumferences['waist'] = waist_match.group(1).strip()

    hip_match = re.search(r'Cadera\s*:\s*(\d+\.?\d*)\s*cm', text)
    if hip_match:
        circumferences['hip'] = hip_match.group(1).strip()

    mid_thigh_match = re.search(r'Muslo medio\s*:\s*(\d+\.?\d*)\s*cm', text)
    if mid_thigh_match:
        circumferences['mid_thigh'] = mid_thigh_match.group(1).strip()

    leg_match = re.search(r'Pierna\s*:\s*(\d+\.?\d*)\s*cm', text)
    if leg_match:
        circumferences['leg'] = leg_match.group(1).strip()

    measurements['circumferences'] = circumferences

    # Skin measurements
    skinfold_measurements = {}    
    supraespinal_match = re.search(r'Supraespinal\s*:\s*(\d+\.?\d*)\s*mm', text)
    if supraespinal_match:
        skinfold_measurements['supraspinal'] = supraespinal_match.group(1).strip()

    abdominal_match = re.search(r'Abdominal\s*:\s*(\d+\.?\d*)\s*mm', text)
    if abdominal_match:
        skinfold_measurements['abdominal'] = abdominal_match.group(1).strip()

    muslo_anterior_match = re.search(r'Muslo anterior\s*:\s*(\d+\.?\d*)\s*mm', text)
    if muslo_anterior_match:
        skinfold_measurements['anterior_thigh'] = muslo_anterior_match.group(1).strip()

    skinfold_measurements['biceps'] = re.search(r'Bíceps:\s+(\d+\.?\d*)mm', text).group(1).strip()
    skinfold_measurements['iliac_crest'] = re.search(r'Cresta Ilíaca:\s+(\d+\.?\d*)mm', text).group(1).strip()
    skinfold_measurements['subscapular'] = re.search(r'Subescapular:\s+(\d+\.?\d*)mm', text).group(1).strip()
    skinfold_measurements['triceps'] = re.search(r'Tríceps:\s+(\d+\.?\d*)mm', text).group(1).strip()
    skinfold_measurements['medial_leg'] = re.search(r'Pierna medial:\s+(\d+\.?\d*)mm', text).group(1).strip()

    measurements['skinfold_measurements'] = skinfold_measurements

    return measurements
