rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    action = command[0]

    if action != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    else:
        row0 = int(command[1])
        col0 = int(command[2])
        row1 = int(command[3])
        col1 = int(command[4])
        if 0 <= row0 < rows and 0 <= col0 < cols and 0 <= row1 < rows and 0 <= col1 < cols:
            # a, b = b, a -> to swap the elements
            matrix[row0][col0], matrix[row1][col1] = matrix[row1][col1], matrix[row0][col0]
            for row in matrix:
                print(" ".join(row))
        else:
            print("Invalid input!")

