parenth_line = input()

stack = []

for parenth in parenth_line:
    if parenth == "{" or parenth == "[" or parenth == "(":
        stack.append(parenth)
    elif parenth == "}" and stack[-1] == "{":
        stack.pop()
    elif parenth == "]" and stack[-1] == "[":
        stack.pop()
    elif parenth == ")" and stack[-1] == "(":
        stack.pop()

if stack:
    print("NO")
else:
    print("YES")