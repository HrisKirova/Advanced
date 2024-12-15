stack = []
n_commands = int(input())
for _ in range(n_commands):
    command = input().split()
    number = command[0]
    if command[0] == "1":
        second_num = command[1]
        stack.append(int(second_num))
    elif stack:
        if command[0] == "2":
            stack.pop()
        elif command[0] == "3":
            print(max(stack))
        elif command[0] == "4":
            print(min(stack))
for _ in range(len(stack)):
    print(stack.pop(), end=" ")