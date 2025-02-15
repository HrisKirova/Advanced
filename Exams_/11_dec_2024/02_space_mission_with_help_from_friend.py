# 100/ 100
matrix_size = int(input())
matrix = []
resources = 100
spaceship = ()
planet = ()
mission_accomplished = False

for rows in range(matrix_size):
    row_data = input().split()
    matrix.append(row_data)

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "S":
            spaceship = (row, col)
        if matrix[row][col] == "P":
            planet = (row, col)

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()

    move = possible_moves[direction]
    new_row = spaceship[0] + move[0]
    new_col = spaceship[1] + move[1]


    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:

        if matrix[spaceship[0]][spaceship[1]] != "R":
            matrix[spaceship[0]][spaceship[1]] = "."


        spaceship = (new_row, new_col)
        resources -= 5  # Deduct resources for the move


        if matrix[new_row][new_col] == "P":
            mission_accomplished = True
            print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
            break
        elif matrix[new_row][new_col] == "R":
            resources += 10  # Refuel at the space station
            if resources > 100:
                resources = 100  # Cap resources at 100
        elif matrix[new_row][new_col] == "M":
            resources -= 5  # Deduct additional resources for meteorite collision
            matrix[new_row][new_col] = "."  # Destroy the meteorite


        if resources < 5:
            print("Mission failed! The spaceship was stranded in space.")
            break
    else:

        print("Mission failed! The spaceship was lost in space.")
        break


if mission_accomplished:
    matrix[planet[0]][planet[1]] = "P"  # Mark Planet B as reached
else:
    matrix[spaceship[0]][spaceship[1]] = "S"  # Mark the last known position of the spaceship


for row in matrix:
    print(" ".join(row))