from collections import deque

working_bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while working_bees and nectar:
    matched_bee = working_bees.popleft()
    matched_nectar = nectar.pop()
    if matched_bee > matched_nectar:
        working_bees.appendleft(matched_bee)
    else:
        honey = 0
        if not (symbols[0] == "/" and matched_nectar == "0"):
            symbol = symbols.popleft()
            if symbol == "+":
                honey = abs(matched_bee + matched_nectar)
            elif symbol == "-":
                honey = abs(matched_bee - matched_nectar)
            elif symbol == "*":
                honey = abs(matched_bee * matched_nectar)
            elif symbol == "/":
                honey = abs(matched_bee / matched_nectar)
            total_honey += honey
        else:
            symbols.popleft()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f'Bees left: {", ".join(map(str, working_bees))}')
elif nectar:
    print(f'Nectar left: {", ".join(map(str, nectar))}')
