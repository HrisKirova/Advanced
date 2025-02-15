n, m = [int(el) for el in input().split(' ')]
# matrix = [list(input()) for _ in range(n)]
matrix = []
starting_pos = ()
pos_to_change = ()
for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "B":
            pos_to_change = (row, col)
            starting_pos = (row, col)

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
pizza_taken = False
while True:

    direction = input().strip()

    if not direction or direction not in possible_moves:
        print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
        continue

    move = possible_moves[direction]
    new_row = starting_pos[0] + move[0]
    new_col = starting_pos[1] + move[1]

    if 0 <= new_row < n and 0 <= new_col < m:
        if matrix[new_row][new_col] == "P":
            pizza_taken = True
            matrix[new_row][new_col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
            # starting_pos = (new_row, new_col)

        elif matrix[new_row][new_col] == '*':
            continue

        elif matrix[new_row][new_col] == "A":
            if pizza_taken:
                matrix[new_row][new_col] = "P"
                print(f"Pizza is delivered on time! Next order...")
                break

        elif matrix[new_row][new_col] == "-":
            matrix[new_row][new_col] = "."
        starting_pos = (new_row, new_col)


    else:
        matrix[pos_to_change[0]][pos_to_change[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

for row in matrix:
    print("".join(row))