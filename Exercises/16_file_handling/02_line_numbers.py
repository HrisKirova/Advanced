import string

# Read the input file
with open("02_text.txt", "r") as file:
    lines = file.readlines()

# Process each line and write to the output file
with open("output.txt", "w") as output_file:
    for index, line in enumerate(lines, start=1):  # Start numbering from 1
        line = line.strip()  # Remove leading/trailing whitespace

        # Count letters using a list comprehension
        letters_count = len([char for char in line if char.isalpha()])

        # Count punctuation using a list comprehension
        punctuation_count = len([char for char in line if char in string.punctuation])

        # Write the formatted line to the output file
        output_file.write(
            f"Line {index}: {line} ({letters_count})({punctuation_count})\n"
        )
