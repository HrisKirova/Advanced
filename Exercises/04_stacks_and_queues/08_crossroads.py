from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
total_cars_passed = 0
green_time = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break
    elif command != "green":
        cars.append(command)
    elif command == "green":
        green_time = green_light_duration

        while green_time and cars:
            current_car = cars.popleft()

            if len(current_car) <= green_time + free_window_duration:
                green_time -= len(current_car)
                if green_time < 0:
                    green_time = 0
                total_cars_passed += 1

            else:
                hit = (green_time + free_window_duration) - len(current_car)
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[hit]}.")
                exit()


