n = int(input())
matrix = [list(input()) for _ in range(n)]

health = 100
possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
starting_position = ()

total_stars = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            starting_position = (row, col)
        elif matrix[row][col] == "*":
            total_stars += 1
freezer = False
while True:

    direction = input().strip()
    if direction == "end":
        if health > 0 and total_stars > 0:
            print("Pacman failed to collect all the stars.")
        matrix[starting_position[0]][starting_position[1]] = "P"
        break
    move = possible_moves[direction]
    new_row = (starting_position[0] + move[0]) % n
    new_col = (starting_position[1] + move[1]) % n

    matrix[starting_position[0]][starting_position[1]] = "-"
    starting_position = (new_row, new_col)
    if matrix[new_row][new_col] == "-":
        continue
    elif matrix[new_row][new_col] == "*":
        matrix[new_row][new_col] = "-"
        total_stars -= 1
        if total_stars == 0:
            print("Pacman wins! All the stars are collected.")
            matrix[starting_position[0]][starting_position[1]] = "P"
            break
    elif matrix[new_row][new_col] == "F":
        freezer = True
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "G":
        if freezer:
            freezer = False
            continue
        else:
            health -= 50
            matrix[new_row][new_col] = "-"
            if health <= 0:
                matrix[starting_position[0]][starting_position[1]] = "P"
                print(f"Game over! Pacman last coordinates [{new_row},{new_col}]")
                break


print(f"Health: {health}")
if total_stars > 0:
    print(f"Uncollected stars: {total_stars}")
for row in matrix:
    print("".join(row))