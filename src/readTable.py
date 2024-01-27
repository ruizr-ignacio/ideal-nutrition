def parse_meal_plan(text):
    # Define the categories and meal times
    meal_times = ["Desayuno", "Colación 12:00 p.m.", "Comida", "Colación 6:00 p.m.", "Cena"]
    base_categories = [
        "Verduras", "Frutas", "Cereales", "Lácteos",
        "Alimentos de Origen Animal", "Aceites y grasas"
    ]
    subcategories = ["Descremados", "Muy bajo aporte de grasa", "Moderado aporte de grasa", "Con proteína"]
    meal_plan = {meal_time: {} for meal_time in meal_times}

    lines = text.split('\n')
    current_category = ""
    portions_index = 0

    for line in lines:
        line = line.strip()

        # Check if the line is a base category or a continuation of it
        if any(base_category in line for base_category in base_categories):
            current_category = line
            portions_index = 0
        elif line in subcategories and current_category:
            current_category += " " + line
        elif line.isdigit() and current_category:
            if portions_index < len(meal_times):
                meal_plan[meal_times[portions_index]].setdefault(current_category, int(line))
                portions_index += 1
            else:
                current_category = ""
                portions_index = 0
        elif line == "" and current_category:
            if portions_index < len(meal_times):
                meal_plan[meal_times[portions_index]].setdefault(current_category, 0)
                portions_index += 1
            else:
                current_category = ""
                portions_index = 0

    return meal_plan
