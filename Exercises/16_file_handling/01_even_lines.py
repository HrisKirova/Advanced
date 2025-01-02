# Define the characters to replace
replace_chars = {"-", ",", ".", "!", "?"}

# Open the file for reading
with open("text.txt", "r") as file:
    # Read all lines
    lines = file.readlines()

# Process each even line
for index, line in enumerate(lines):
    if index % 2 == 0:  # Check for even line
        # Replace specified characters with "@"
        for char in replace_chars:
            line = line.replace(char, "@")
        # Reverse the order of words
        reversed_line = " ".join(line.split()[::-1])
        # Print the result
        print(reversed_line)