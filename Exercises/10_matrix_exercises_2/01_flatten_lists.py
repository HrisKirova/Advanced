text = list(input().split("|"))
matrix = []

for el in text:
    current_el = el.split()
    matrix.append(current_el)

for row in range(len(matrix) - 1, -1, -1):
    print(*matrix[row], end=" ")

# Solution 2
# Input processing
# text = input().split("|")
#
# # Flatten the matrix in reverse order
# flattened = " ".join(el.strip() for el in reversed(text))
#
# # Print the result
# print(flattened)