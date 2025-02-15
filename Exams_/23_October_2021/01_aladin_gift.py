from collections import deque
def check_range(result):
    if 100 <= result < 500:
        return True
    return False
def check_gift(result):
    if 100 <= result <= 199:
        return "Gemstone"
    elif 200 <= result <= 299:
        return "Porcelain Sculpture"
    elif 300 <= result <= 399:
        return "Gold"
    elif 400 <= result <= 499:
        return "Diamond Jewellery"
materials = deque(int(el) for el in input().split())
magic_level = deque(int(el) for el in input().split())
presents = {}
while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    result = current_material + current_magic
    if check_range(result):
        present = check_gift(result)
        if present not in presents:
            presents[present] = 0
        presents[present] += 1
    elif result < 100:
        if result % 2 == 0:
            result_new = current_material * 2 + current_magic * 3
        else:
            result_new = (current_material + current_magic) * 2
        if check_range(result_new):
            present = check_gift(result_new)
            if present not in presents:
                presents[present] = 0
            presents[present] += 1
    elif result >= 500:
        result_new = result / 2
        if check_range(result_new):
            present = check_gift(result_new)
            if present not in presents:
                presents[present] = 0
            presents[present] += 1


if ({"Gemstone", "Porcelain Sculpture"} <= presents.keys() or
    {"Gold", "Diamond Jewellery"} <= presents.keys()):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")


if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

if presents:
    for present, amount in sorted(presents.items()):  # No need for filtering
        print(f"{present}: {amount}")