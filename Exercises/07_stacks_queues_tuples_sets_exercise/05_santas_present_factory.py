from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))
presents = {}
if materials[-1] == 0:
    materials.pop()
if magic_level[0] == 0:
    magic_level.popleft()
while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    total_magic = material * magic
    if total_magic == 150:
        presents["Doll"] = 0
        presents["Doll"] += 1
    elif total_magic == 250:
        presents["Wooden train"] = 0
        presents["Wooden train"] += 1
    elif total_magic == 300:
        presents["Teddy bear"] = 0
        presents["Teddy bear"] += 1
    elif total_magic == 400:
        presents["Bicycle"] = 0
        presents["Bicycle"] += 1
    elif total_magic < 0:
        sum_ = material + magic
        materials.append(sum_)
    elif total_magic > 0:
        materials.append(material + 15)

if "Doll" and "Wooden train" in presents or "Teddy bear" and "Bicycle" in presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")
for present, count in presents.items():
    print(f'{present}: {count}')