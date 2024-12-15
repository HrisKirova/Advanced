
n, m = map(int, input().split())
set1 = set()
set2 = set()
for x in range(n + m):
    num = int(input())
    if len(set1) < n:
        set1.add(num)
    else:
        set2.add(num)

result = set1.intersection(set2)


print(" ".join(str(x) for x in result))