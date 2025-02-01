from collections import deque

# Input processing
chocolate = deque(int(x) for x in input().split(", "))
milk_cups = deque(int(y) for y in input().split(", "))
milk_chocolates = 0

# Process ingredients until conditions are met
while chocolate and milk_cups and milk_chocolates < 5:
    # Remove chocolates <= 0
    while chocolate and chocolate[-1] <= 0:
        chocolate.pop()

    # Remove milk cups <= 0
    while milk_cups and milk_cups[0] <= 0:
        milk_cups.popleft()

    # Check if both are non-empty after cleaning
    if not chocolate or not milk_cups:
        break

    # Get last chocolate and first milk
    last_chocolate = chocolate.pop()
    first_milk = milk_cups.popleft()

    # Check for a match
    if last_chocolate == first_milk:
        milk_chocolates += 1
    else:
        # Decrease chocolate and move milk to the end
        chocolate.append(last_chocolate - 5)
        milk_cups.append(first_milk)

# Output results
if milk_chocolates == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f'Chocolate: {", ".join(str(x) for x in chocolate)}')
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(str(y) for y in milk_cups)}")
else:
    print("Milk: empty")
