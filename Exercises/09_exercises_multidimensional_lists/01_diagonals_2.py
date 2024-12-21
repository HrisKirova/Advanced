matrix = [[int(num) for num in input().split(", ")] for row in range(int(input()))]

left = []
right = []

for i, j in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    left.append(a)
    right.append(b)

print(f'Primary diagonal: {", ".join(map(str, left))}. Sum: {sum(left)}')
print(f'Secondary diagonal: {", ".join(map(str, right))}. Sum: {sum(right)}.')