n = int(input())

matrix = []
for i in range(n):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

primary_diagonal = []
secondary_diagonal = []
# for row_index in range(n):
#     for col_index in range(n):
#         if row_index == col_index:
#             primary_diagonal.append(matrix[row_index][col_index])
for index in range(n):
    primary_diagonal.append(matrix[index][index])

secondary_diagonal = [matrix[i][n - 1 - i] for i in range(n)]

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}.')
