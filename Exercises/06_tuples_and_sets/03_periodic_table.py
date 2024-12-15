count = int(input())
unique_elements = set()
for _ in range(count):
    elements = input().split()
    for x in elements:
        unique_elements.add(x)

print(*unique_elements, sep="\n")
