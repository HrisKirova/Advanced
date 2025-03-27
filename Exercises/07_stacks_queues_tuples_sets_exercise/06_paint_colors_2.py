# Improved by chatGPT -> 100 / 100 (with my fixes)
data = input().split()
colors = []

# Define main and secondary colors
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
paired_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

while data:
    if len(data) > 1:
        # Concatenate first and last substrings
        substr_left = data[0]
        substr_right = data[-1]
        combined = [substr_left + substr_right, substr_right + substr_left]

        # Check for colors
        found_color = next((color for color in combined if color in main_colors or color in secondary_colors), None)
        if found_color:
            colors.append(found_color)
            data.pop(0)  # Remove the first substring
            data.pop(-1)  # Remove the last substring
        else:
            # Modify substrings and reinsert
            substr_left = substr_left[:-1] if len(substr_left) > 1 else ""
            substr_right = substr_right[:-1] if len(substr_right) > 1 else ""
            data.pop(0)
            data.pop(-1)
            middle = len(data) // 2
            if substr_left:
                data.insert(middle, substr_left)
            if substr_right:
                data.insert(middle, substr_right)
    else:
        # Handle the last single substring
        remaining = data.pop()
        if remaining in main_colors or remaining in secondary_colors:
            colors.append(remaining)

# Validate secondary colors at the end
final_colors = []
for color in colors:
    if color in secondary_colors:
        required_colors = paired_colors[color]
        # Check if all required main colors are in the collected colors
        if required_colors.issubset(colors):
            final_colors.append(color)
    else:
        final_colors.append(color)

# Print the result
print(final_colors)
