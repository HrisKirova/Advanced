from collections import deque

initial_colors = deque(input().split())
primary_colors = ["blue", "yellow", "red"]
secondary_colors = ["orange", "purple", "green"]
new_colors = []

while initial_colors:
    if len(initial_colors) == 1:
        new_color = initial_colors.pop()

    else:
        first_part = initial_colors.popleft()
        second_part = initial_colors.pop()
        new_color = first_part + second_part
        another_color = second_part + first_part
        if new_color in primary_colors or new_color in secondary_colors:
            new_colors.append(new_color)
        elif another_color in primary_colors or another_color in secondary_colors:
            new_colors.append(another_color)
        else:
            midpoint = len(initial_colors) // 2
            if first_part:
                initial_colors.insert(midpoint, first_part[:-1])
            if second_part:
                initial_colors.insert(midpoint, second_part[:-1])

for color in new_colors:
    if color == "orange" and ("yellow" not in new_colors or "red" not in new_colors):
        new_colors.remove(color)
    elif color == "green" and ("yellow" not in new_colors or "blue" not in new_colors):
        new_colors.remove(color)
    elif color == "purple" and ("blue" not in new_colors or "red" not in new_colors):
        new_colors.remove(color)

print(new_colors)