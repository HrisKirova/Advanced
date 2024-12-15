# Read the text from the console
text = input()

# Use a set to get all unique characters in the text
unique_chars = set(text)

# Create a dictionary to store the counts of each character
char_count = {char: text.count(char) for char in unique_chars}

# Sort the dictionary keys alphabetically and print the results
for char in sorted(char_count.keys()):
    print(f"{char}: {char_count[char]}")
