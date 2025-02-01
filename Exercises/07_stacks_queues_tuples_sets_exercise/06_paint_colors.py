# My solution -> 60 /100
data = input().split()
colors = []

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

paired_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

while data and len(data) > 1:
    substr_left = data[0]
    substr_right = data[-1]
    result1 = substr_left + substr_right
    result2 = substr_right + substr_left
    if result1 in main_colors:
        data.pop()
        data.pop(0)
        colors.append(result1)
    elif result1 in secondary_colors:
        data.pop()
        data.pop(0)
        colors.append(result1)
    elif result2 in main_colors:
        data.pop()
        data.pop(0)
        colors.append(result2)
    elif result2 in secondary_colors:
        data.pop()
        data.pop(0)
        colors.append(result2)
    else:
        add_left = substr_left[:-1]
        add_right = substr_right[:-1]
        data.pop()
        data.pop(0)
        middle = len(data) // 2
        if add_left:
            data.insert(middle, add_left)
        if add_right:
            data.insert(middle, add_right)

if len(data) == 1:
    last = data[0]
    if last in main_colors or last in secondary_colors:
        colors.append(last)
        data.pop()

for i in range(len(colors)):
    if colors[i] in secondary_colors:
        main_col_1, main_col_2 = paired_colors[colors[i]]
        if main_col_1 not in colors or main_col_2 not in colors:
            colors.pop(i)

print(colors)

            