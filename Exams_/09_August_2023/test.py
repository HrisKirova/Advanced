def accommodate_new_pets(capacity: int, max_weight: float, *pet_data):
    accommodated_pets = dict()
    total_valid_pets = 0  # Count total pets that could be accommodated

    for pet_type, pet_weight in pet_data:
        if float(pet_weight) > float(max_weight):  # Skip overweight pets
            continue

        total_valid_pets += 1  # Count only pets that are within the weight limit

        if capacity > 0:  # Ensure we only accommodate within capacity
            if pet_type not in accommodated_pets:
                accommodated_pets[pet_type] = 0
            accommodated_pets[pet_type] += 1
            capacity -= 1  # Reduce available space


    if len(accommodated_pets) == total_valid_pets:
        result = f"All pets are accommodated! Available capacity: {capacity}."
    else:
        result = "You did not manage to accommodate all pets!"


    if accommodated_pets:
        pet_details = "\n".join(f"{pet}: {num}" for pet, num in sorted(accommodated_pets.items()))
        return f"{result}\nAccommodated pets:\n{pet_details}"

    return result

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
