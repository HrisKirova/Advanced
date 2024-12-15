from collections import deque

current_string = (input().split())
queue  = deque()

for char in current_string:
    if char not in "*+-/":
        queue.append(int(char))
    else:
        while len(queue) > 1:
            num1 = queue.popleft()
            num2 = queue.popleft()
            if char == "+":
                queue.appendleft(num1 + num2)
            elif char == "-":
                queue.appendleft(num1 - num2)
            elif char == "*":
                queue.appendleft(num1 * num2)
            elif char == "/":
                queue.appendleft(num1 // num2)

print(queue.popleft())

