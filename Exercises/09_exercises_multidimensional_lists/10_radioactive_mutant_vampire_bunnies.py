def bunny_spread(bunny_positions, board):
    n = len(board)
    m = len(board[0])
    new_bunny_positions = set()  # To store the new positions of bunnies

    for r, c in bunny_positions:
        # Try spreading in all directions
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_r, new_c = r + dr, c + dc
            # Check if the new position is within the matrix bounds
            if 0 <= new_r < n and 0 <= new_c < m:
                if board[new_r][new_c] != "B":  # Spread only to non-bunny cells
                    new_bunny_positions.add((new_r, new_c))

    # Update the matrix with new bunny positions
    for new_r, new_c in new_bunny_positions:
        board[new_r][new_c] = "B"

    # Return all current bunny positions (old + new)
    return bunny_positions | new_bunny_positions


def player_move(current_position, command, n, m):
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    r, c = current_position
    dr, dc = directions[command]
    new_r, new_c = r + dr, c + dc

    # Check if the player moves outside the matrix (escape)
    if 0 <= new_r < n and 0 <= new_c < m:
        return new_r, new_c, False  # False indicates the player is still inside
    return new_r, new_c, True  # True indicates the player has escaped


# Input parsing
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
commands = input()

# Locate the player and bunnies
player = None
bunny_positions = set()

for r in range(n):
    for c in range(m):
        if matrix[r][c] == "P":
            player = (r, c)
        elif matrix[r][c] == "B":
            bunny_positions.add((r, c))

# Game loop
for command in commands:
    # Move the player first
    player_row, player_col = player
    new_row, new_col, escaped = player_move(player, command, n, m)

    if escaped:  # Player escapes
        # Clear the player's previous position
        matrix[player_row][player_col] = "."
        # Spread the bunnies
        bunny_positions = bunny_spread(bunny_positions, matrix)
        # Print the final matrix and result
        print("\n".join("".join(row) for row in matrix))
        print(f"won: {player_row} {player_col}")
        break

    # Check if the player dies after moving
    if matrix[new_row][new_col] == "B":
        # Clear the player's previous position
        matrix[player_row][player_col] = "."
        # Spread the bunnies
        bunny_positions = bunny_spread(bunny_positions, matrix)
        # Print the final matrix and result
        print("\n".join("".join(row) for row in matrix))
        print(f"dead: {new_row} {new_col}")
        break

    # Update player position
    matrix[player_row][player_col] = "."
    matrix[new_row][new_col] = "P"
    player = (new_row, new_col)

    # Spread the bunnies after the player moves
    bunny_positions = bunny_spread(bunny_positions, matrix)

    # Check if the player dies due to bunny spread
    if matrix[player[0]][player[1]] == "B":
        print("\n".join("".join(row) for row in matrix))
        print(f"dead: {player[0]} {player[1]}")
        break
