def plant_garden(available_space: float, *allowed_plants, **planting_requests):
    allowed_plants_data = {plant_type: required_space for plant_type, required_space in allowed_plants}
    planted_plants = {}

    for plant_type, desired_quantity in sorted(planting_requests.items()):
        if plant_type not in allowed_plants_data:
            continue
        max_possible_plants = int(available_space / allowed_plants_data[plant_type])
        plants_to_plant = min(max_possible_plants, desired_quantity)
        if plants_to_plant > 0:
            planted_plants[plant_type] = plants_to_plant
            available_space -= plants_to_plant * allowed_plants_data[plant_type]
        if available_space <= 0 and not planting_requests:
            break

    result = ["Planted plants:"]
    [result.append(f"{plant_type}: {planted_plants[plant_type]}") for plant_type in sorted(planted_plants)]
    formated_planted_pcs = "\n".join(result)

    if all(planted_plants.get(pt, 0) == qty for pt, qty in planting_requests.items() if pt in allowed_plants_data):
        return f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n{formated_planted_pcs}"
    return f"Not enough space to plant all requested plants!\n{formated_planted_pcs}"



print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
