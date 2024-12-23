from collections import deque

# Input data
mat_size = int(input())
commands = deque(input().split())
matrix = [input().split() for _ in range(mat_size)]

# Find the starting position of the miner ('s')
start_position = ()
for row in range(mat_size):
    for col in range(mat_size):
        if matrix[row][col] == "s":
            start_position = (row, col)

# Initialize variables
current_position = start_position
collected_coal = 0
total_coal = sum(row.count("c") for row in matrix)

# Direction mappings to avoid multiple if-statements
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Process commands
while commands:
    command = commands.popleft()
    # Calculate new position
    row_change, col_change = directions[command]
    new_row = current_position[0] + row_change
    new_col = current_position[1] + col_change

    # Check if the new position is within bounds
    if 0 <= new_row < mat_size and 0 <= new_col < mat_size:
        current_position = (new_row, new_col)
        cell = matrix[new_row][new_col]

        if cell == "c":
            collected_coal += 1
            matrix[new_row][new_col] = "*"  # Replace coal with empty space
            if collected_coal == total_coal:
                print(f"You collected all coal! ({new_row}, {new_col})")
                break
        elif cell == "e":
            print(f"Game over! ({new_row}, {new_col})")
            break
# If the game ends without collecting all coal
else:
    remaining_coal = total_coal - collected_coal
    print(f"{remaining_coal} pieces of coal left. ({current_position[0]}, {current_position[1]})")
