def is_valid_move(row, col, n):
    """Check if the move is within the board boundaries."""
    return 0 <= row < n and 0 <= col < n

def count_attacks(board, row, col, n, moves):
    """Count how many knights the current knight can attack."""
    attacks_count = 0
    for dr, dc in moves: # delta row, delta col
        new_row, new_col = row + dr, col + dc
        if is_valid_move(new_row, new_col, n) and board[new_row][new_col] == "K":
            attacks_count += 1
    return attacks_count

# Input
n = int(input())
board = [list(input()) for _ in range(n)]

# Possible knight moves
knight_moves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

knights_removed = 0

# Simulate the game
while True:
    max_attacks = 0
    knight_to_remove = None

    # Find the knight with the most attacks
    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                attacks = count_attacks(board, row, col, n, knight_moves)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_to_remove = (row, col)

    # If no knight can attack another, stop
    if max_attacks == 0:
        break

    # Remove the knight
    if knight_to_remove:
        r, c = knight_to_remove
        board[r][c] = "0"
        knights_removed += 1

# Output the result
print(knights_removed)
