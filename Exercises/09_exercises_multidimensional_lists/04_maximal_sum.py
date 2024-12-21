rows, columns = [int(el) for el in input().split()]
# matrix = [int(num) for num in input().split() for row in range(rows)]
matrix = []

for i in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)
max_number = -181 # because the lowest sum we may have in square of 3 x 3 is to be full of -20
                            # (according the condition in the task) , otherwise we may solve it with None
max_row_position = 0
max_col_position = 0
for row in range(rows - 2):
    for col in range(columns - 2):
        sum_numbers = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                sum_numbers += matrix[i][j]
        # if max_number = None:
        #     max_number = sum_number
        # else:
        if sum_numbers > max_number:
            max_number = sum_numbers
            max_row_position = row
            max_col_position = col

print(f"Sum = {max_number}")
for i in range(max_row_position, max_row_position +3):
    for j in range(max_col_position, max_col_position + 3):
        print(matrix[i][j], end=" ")
    print()

