num_rows = int(input())

matrix = [[int(el) for el in input().split()] for row in range(num_rows)]

while True:
    command = input()
    if command == "END":
        break
    else:
        command_parts = command.split()
        action = command_parts[0]
        r = int(command_parts[1])
        c = int(command_parts[2])
        value = int(command_parts[3])
        if action == "Add":
            if 0 <= r < num_rows and 0 <= c < len(matrix[0]):
                matrix[r][c] += value
            else:
                print("Invalid coordinates")
                continue
        elif action == "Subtract":
            if 0 <= r < num_rows and 0 <= c < len(matrix[0]):
                matrix[r][c] -= value
            else:
                print("Invalid coordinates")
                continue

for row in matrix:
    print(*row)
