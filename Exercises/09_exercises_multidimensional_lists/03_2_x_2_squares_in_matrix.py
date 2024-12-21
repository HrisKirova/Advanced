rows, columns = [int(el) for el in input().split()]

matrix = []
counter = 0
for i in range(rows):
    row_data = input().split()
    matrix.append(row_data)

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        item = matrix[row_index][col_index]
        next_item = matrix[row_index][col_index + 1]
        item_below = matrix[row_index + 1][col_index]
        item_diagonal = matrix[row_index + 1][col_index + 1]
        if item == next_item == item_below == item_diagonal:
            counter += 1

print(counter)
