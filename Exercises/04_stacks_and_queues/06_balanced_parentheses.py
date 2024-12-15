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
for char in test_string:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if not stack or stack[-1] != pairs[char]:
            print("NO")
            break
        stack.pop()
if not stack:
    print("Yes".upper())
