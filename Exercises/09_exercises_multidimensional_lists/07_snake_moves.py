rows, cols = [int(n) for n in input().split()]

text = input()

matrix = [[" " for _ in range(cols)] for row in range(rows)]

index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = text[index]
            index = (index + 1) % len(text)
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = text[index]
            index = (index + 1) % len(text)

for row in matrix:
    print("".join(row))