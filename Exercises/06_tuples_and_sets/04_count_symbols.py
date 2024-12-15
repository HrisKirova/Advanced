text = input()
# Create an empty dictionary to store character counts
char_count = {}

# Count occurrences of each character
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Sort the dictionary keys alphabetically and print the results
for char in sorted(char_count.keys()):
    print(f"{char}: {char_count[char]}")