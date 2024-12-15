clothes = [int(x) for x in input().split()]
# clothes = list(map(int, input().split()))
capacity_of_rack = int(input())
current_rack = 0
rack_count = 1

while clothes:
    item = clothes.pop()
    if current_rack + item <= capacity_of_rack:
        current_rack += item
    else:
        rack_count += 1
        current_rack = item

print(rack_count)