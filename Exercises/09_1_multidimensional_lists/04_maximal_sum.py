rows, cols = [int(el) for el in input().split()]

board = [[int(num) for num in input().split()] for row in range(rows)]

max_sum = -181 # -float("inf")
max_row = 0
max_col = 0
for row in range(rows - 2):
    for col in range(cols -2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += board[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = col
print(f"Sum = {max_sum}")

for i in range(max_row, max_row + 3):
    for j in range(max_col, max_col +3):
        print(board[i][j], end=" ")
    print()
