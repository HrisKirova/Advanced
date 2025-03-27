row_num, col_num = [int(n) for n in input().split()]

board = []
for i in range(row_num):
    row_data = input().split()
    board.append(row_data)

square_count = 0


for i in range(row_num - 1):
    for j in range(col_num - 1):
        item = board[i][j]
        next_item = board[i][j + 1]
        item_below = board[i + 1][j]
        item_diagonal = board[i + 1][j + 1]
        if item == next_item == item_below == item_diagonal:
            square_count += 1

print(square_count)