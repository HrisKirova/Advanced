def accommodate_new_pets(capacity:int, max_weight: float, *pet_data):
    break_condition = False
    accommodated_pets = dict()
    break_condition = False
    for i in range(len(pet_data)):
        current_pet_type = pet_data[i][0]
        current_pet_weight = pet_data[i][1]

        if capacity == 0:
            break_condition = True
            break
        elif float(current_pet_weight) > float(max_weight):
            continue
        elif len(accommodated_pets) < capacity:
            if current_pet_type not in accommodated_pets:
                accommodated_pets[current_pet_type] = 0
            accommodated_pets[current_pet_type] += 1
            capacity -= 1

            # Final message
    if capacity == 0 and break_condition:
        result = "You did not manage to accommodate all pets!"
    else:
        result = f"All pets are accommodated! Available capacity: {capacity}."

    # Append details about accommodated pets
    if accommodated_pets:
        pet_details = "\n".join(f"{pet} -> {num}" for pet, num in sorted(accommodated_pets.items()))
        return f"{result}\nAccommodated pets:\n{pet_details}"

    return result

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))







