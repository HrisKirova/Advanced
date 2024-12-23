# Input data
rows, cols = map(int, input().split())
snake = input()

# Initialize the matrix
matrix = []

# Counter for the snake's current position
snake_index = 0

# Fill the matrix row by row
for row in range(rows):
    current_row = []
    for col in range(cols):
        # Add the current snake character
        current_row.append(snake[snake_index])
        # Move to the next character, wrapping around
        snake_index = (snake_index + 1) % len(snake)

    # Reverse the row for odd rows to create the zigzag pattern
    if row % 2 != 0:
        current_row.reverse()

    # Append the row to the matrix
    matrix.append(current_row)

# Print the matrix
for row in matrix:
    print("".join(row))
