# Input the matrix
num_rows = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(num_rows)]

# Validate coordinates
def is_valid_coordinate(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

# Process commands
while True:
    command = input()
    if command == "END":
        break

    command_parts = command.split()
    action, r, c, value = command_parts[0], int(command_parts[1]), int(command_parts[2]), int(command_parts[3])

    if is_valid_coordinate(r, c, matrix):
        if action == "Add":
            matrix[r][c] += value
        elif action == "Subtract":
            matrix[r][c] -= value
    else:
        print("Invalid coordinates")

# Print the final matrix
for row in matrix:
    print(*row)
