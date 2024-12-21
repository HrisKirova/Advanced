# Input rows and columns
rows, cols = map(int, input().split())

# Generate the matrix
matrix = [
    [f"{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}" for c in range(cols)]
    for r in range(rows)
]

# Print the matrix
for row in matrix:
    print(" ".join(row))
