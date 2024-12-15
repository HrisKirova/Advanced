num = int(input())
longest_intersection = set()
for _ in range(num):
    first_range, second_range = (list(map(int, r.split(","))) for r in input().split("-")) # can omit list here because I won't use the ranges further
    first_start, first_end = first_range
    second_start, second_end = second_range
    # Create sets directly from ranges
    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    # Find the intersection
    inters = first_set & second_set
    if len(longest_intersection) < len(inters):
        longest_intersection = inters

print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")