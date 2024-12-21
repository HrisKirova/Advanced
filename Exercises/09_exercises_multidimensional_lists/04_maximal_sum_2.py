rows, columns = map(int, input().split())

# Read the matrix
matrix = [list(map(int, input().split())) for _ in range(rows)]

# Initialize variables to track the maximum sum and its top-left position
max_sum = float('-inf')  # Use negative infinity for clarity
max_position = (0, 0)

# Iterate over all possible 3x3 submatrices
for row in range(rows - 2):
    for col in range(columns - 2):
        # Calculate the sum of the current 3x3 submatrix /
        # Replaced nested loops with a sum using a generator expression for the 3x3 submatrix
        current_sum = sum(matrix[i][j] for i in range(row, row + 3) for j in range(col, col + 3))

        # Update max_sum and max_position if a higher sum is found
        if current_sum > max_sum:
            max_sum = current_sum
            max_position = (row, col)

# Extract the top-left position of the 3x3 submatrix with the maximum sum
max_row, max_col = max_position

# Output the results
print(f"Sum = {max_sum}")
for i in range(max_row, max_row + 3):
    print(" ".join(map(str, matrix[i][max_col:max_col + 3])))
