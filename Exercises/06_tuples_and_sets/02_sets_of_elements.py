n, m = [int(el) for el in input().split()]
set1 = set()
set2 = set()
for _ in range(n):
    num = int(input())
    set1.add(num)
for _ in range(m):
    num = int(input())
    set2.add(num)

result = set1.intersection(set2)


print(*result, sep="\n")