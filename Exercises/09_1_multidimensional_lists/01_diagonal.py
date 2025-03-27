n = int(input())

board = [[int(num) for num in input().split(", ")] for row in range(n)]

primary_d = []
secondary_d = []

for index in range(len(board)):
    primary_d.append(board[index][index])
    secondary_d.append(board[index][n - 1 - index])

print(f"Primary diagonal: {', '.join(str(el) for el in primary_d)}. Sum: {sum(primary_d)}")
print(f"Primary diagonal: {', '.join(str(el) for el in secondary_d)}. Sum: {sum(secondary_d)}")