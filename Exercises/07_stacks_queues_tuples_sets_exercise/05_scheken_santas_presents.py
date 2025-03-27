from collections import deque


def check_toy_crafting(total_magic, price_dict):
    for item, price in price_dict.items():
        if total_magic == price:
            return item
    return None


materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

crafting_magic_need = {
    'Bicycle': 400,
    'Teddy bear': 300,
    'Wooden train': 250,
    'Doll': 150,
}

created_toys = {
    'Bicycle': 0,
    'Teddy bear': 0,
    'Wooden train': 0,
    'Doll': 0,
}

while materials and magic_level:
    material = materials[-1]
    magic = magic_level[0]
    total = material * magic

    if material == 0 or magic == 0:
        if material == 0:
            materials.pop()
        if magic == 0:
            magic_level.popleft()
        continue

    if total < 0:
        material = materials.pop()
        magic = magic_level.popleft()
        calculate = material + magic
        materials.append(calculate)
        continue

    if total in crafting_magic_need.values():
        crafted_toy = check_toy_crafting(total, crafting_magic_need)
        if crafted_toy:
            created_toys[crafted_toy] += 1
        materials.pop()
        magic_level.popleft()
        continue

    if total > 0:
        magic_level.popleft()
        materials[-1] += 15
        continue

if (created_toys['Bicycle'] > 0 and created_toys['Teddy bear'] > 0) or \
   (created_toys['Doll'] > 0 and created_toys['Wooden train'] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for item, value in sorted(created_toys.items()):
    if value:
        print(f"{item}: {value}")