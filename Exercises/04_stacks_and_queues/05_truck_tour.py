from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    current_fuel, distance = map(int, input().split())
    pumps.append((current_fuel, distance))

# Find the starting pump
for start_index in range(petrol_pumps):
    tank = 0
    completed = True  # Assume we can complete the circle from this pump

    for fuel, distance in pumps:
        tank += fuel  # Fill the tank with the petrol from the current pump
        if tank < distance:  # Check if we can reach the next pump
            completed = False
            break
        tank -= distance  # Subtract the fuel needed to reach the next pump

    if completed:
        print(start_index)
        break

    # Rotate the queue to simulate starting from the next pump
    pumps.append(pumps.popleft())