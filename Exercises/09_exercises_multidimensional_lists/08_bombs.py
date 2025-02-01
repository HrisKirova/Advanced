mat_size = int(input())
matrix = [[int(num) for num in input().split()] for row in range(mat_size)]


bomb_coordinates = input().split()
'''
123
1x5
678
'''


def get_bomb(x, y, size):
    cells = []
    if x - 1 in range(size) and y - 1 in range(size):
        cells.append((x - 1, y - 1))
    if x in range(size) and y - 1 in range(size):
        cells.append((x, y - 1))
    if x + 1 in range(size) and y - 1 in range(size):
        cells.append((x + 1, y - 1))
    if x - 1 in range(size) and y in range(size):
        cells.append((x - 1, y))
    if x + 1 in range(size) and y in range(size):
        cells.append((x + 1, y))
    if x - 1 in range(size) and y + 1 in range(size):
        cells.append((x - 1, y + 1))
    if x in range(size) and y + 1 in range(size):
        cells.append((x, y + 1))
    if x + 1 in range(size) and y + 1 in range(size):
        cells.append((x + 1, y + 1))
    return cells


for bomb in bomb_coordinates:
    row, col = [int(n) for n in bomb.split(",")]
    current_bomb = matrix[row][col]
    if current_bomb > 0:
        neighbour_cells = get_bomb(row, col, mat_size)
        for r, c in neighbour_cells:
            if matrix[r][c] > 0:
                matrix[r][c] -= current_bomb
        matrix[row][col] = 0

cells_count = 0
cells_sum = 0

for row in range(mat_size):
    for col in range(mat_size):
        if matrix[row][col] > 0:
            cells_count += 1
            cells_sum += matrix[row][col]

print(f"Alive cells: {cells_count}")
print(f"Sum: {cells_sum}")

for row in range(mat_size):
    print(*matrix[row])