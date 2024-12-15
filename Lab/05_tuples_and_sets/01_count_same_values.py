numbers = tuple([float(x) for x in input().split()])

occ = {}

for n in numbers:
    occ[n] = numbers.count(n)
for key, value in occ.items():
    print(f"{key:.1f} - {value} times")