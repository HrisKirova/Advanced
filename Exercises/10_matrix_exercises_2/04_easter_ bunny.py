n = int(input())

matrix = [[n for n in input().split()] for row in range(n)]
bunny = None
max_sum = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = (row, col)
# for row in range(n):
#     line = input().split()
#     matrix.append(line)
#     if "B" in line:
#         bunny = (row, line.index("B"))  # Locate the bunny
# Define possible directions
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def is_valid(r, c, size):
    """Check if a cell is within the matrix boundaries."""
    return 0 <= r < size and 0 <= c < size

# Initialize variables to track the best path
best_direction = None
best_path = []
max_eggs = 0

# Explore each direction
for direction, (dr, dc) in directions.items():
    current_row, current_col = bunny
    path = []
    eggs = 0

    while True:
        current_row += dr
        current_col += dc

        if not is_valid(current_row, current_col, n) or matrix[current_row][current_col] == "X":
            break

        # Collect eggs
        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])

    # Update the best path if the current direction is better
    if eggs > max_eggs:
        max_eggs = eggs
        best_path = path
        best_direction = direction

# Print the results
print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)