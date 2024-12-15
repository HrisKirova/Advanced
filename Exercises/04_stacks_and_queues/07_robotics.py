from collections import deque
from datetime import datetime, timedelta

# Parse robot data and starting time
robots_list = input().split(";")
robots = []
# Parse the starting time
start_time = datetime.strptime(input(), "%H:%M:%S") # Not clear to me !!!
for robot in robots_list:
    robot_name, process_time = robot.split("-")
    robots.append({"name": robot_name, "time": int(process_time), "busy_until": start_time})


# Read products until "End"
products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

# Process products
current_time = start_time
while products:
    current_time += timedelta(seconds=1) # this too not clear!!!
    product = products.popleft()
    assigned = False

    # Check each robot
    for robot in robots:
        # If the robot is free, assign the product
        if current_time >= robot["busy_until"]:
            robot["busy_until"] = current_time + timedelta(seconds=robot["time"])
            print(f"{robot['name']} - {product} [{current_time.strftime('%H:%M:%S')}]")
            assigned = True
            break

    # If no robot could take the product, requeue it
    if not assigned:
        products.append(product)
