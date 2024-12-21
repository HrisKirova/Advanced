n = int(input())

matrix = []

for i in range(n):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

primary_diagonal = 0
for index in range(n):
    primary_diagonal += matrix[index][index]

secondary_diagonal = 0
for row_index in range(n):
    secondary_diagonal += matrix[row_index][n - row_index - 1]

result = abs(primary_diagonal - secondary_diagonal)

print(result)