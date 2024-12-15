num_commands = int(input())

parking_lot = set()
for _ in range(num_commands):
    action, car_plate = input().split(", ")

    if action == "IN":
        parking_lot.add(car_plate)
    elif action == "OUT":
        if car_plate in parking_lot:
            parking_lot.remove(car_plate)

if parking_lot:
    print(*parking_lot, sep="\n") # unpack the set and separator = new line

