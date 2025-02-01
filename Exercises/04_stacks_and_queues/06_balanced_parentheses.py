#
#
# def is_balanced(string):
#     stack = []
#     pairs = {')': '(', '}': '{', ']': '['}
#
#     for char in string:
#         if char in "({[":
#             stack.append(char)
#         elif char in ")}]":
#             if not stack or stack[-1] != pairs[char]:
#                 return False
#             stack.pop()
#
#     return not stack
#
#
# test_string = input()
# print(is_balanced(test_string))  # True

test_string = input()

stack = []
pairs = {")": "(", "}": "{", "]": "["}

is_balanced = True  # Flag to track whether the parentheses are balanced

for char in test_string:
    if char in "({[":  # Opening brackets
        stack.append(char)
    elif char in ")}]":  # Closing brackets
        if not stack or stack[-1] != pairs[char]:
            is_balanced = False  # Set flag to false if unbalanced
            break
        stack.pop()

# Final check: if stack is not empty, it's unbalanced
if is_balanced and not stack:
    print("YES")
else:
    print("NO")


