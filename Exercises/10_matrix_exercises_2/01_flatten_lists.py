# Read input and split into sub-lists
text = input().split("|")

# Flatten sub-lists in reverse order
result = []
for sublist in reversed(text):
    # Split by spaces, ignore extra spaces, and extend the result list
    result.extend(sublist.split())

# Print the final flattened list
print(" ".join(result))

# Solution 2
# Input processing
# text = input().split("|")
#
# # Flatten the matrix in reverse order
# flattened = " ".join(el.strip() for el in reversed(text))
#
# # Print the result
# print(flattened)