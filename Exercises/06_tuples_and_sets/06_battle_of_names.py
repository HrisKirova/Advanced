num_of_names = int(input())
odd_set = set()
even_set = set()

for i in range(1, num_of_names +1):
    name = input()
    sum_names = sum(ord(char) for char in name) # !!! this way avoiding the for loop
    total = sum_names // i
    if total % 2 == 0:
        even_set.add(total)
    else:
        odd_set.add(total)


summarized_odd = sum(odd_set)
summarized_even = sum(even_set)

if summarized_even == summarized_odd:
    print(", ".join(map(str, odd_set.union(even_set))))
elif summarized_odd > summarized_even:
    print(", ".join(map(str, odd_set.difference(even_set))))
else:
    print(", ".join(map(str, odd_set.symmetric_difference(even_set))))