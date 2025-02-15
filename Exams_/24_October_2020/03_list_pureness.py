def best_list_pureness(numbers:list, k:int):
    rotation_count = 0
    best_count = 0
    best_pureness = 0

    for i, num in enumerate(numbers):
        best_pureness += (i * num)

    while rotation_count < k:

        pureness_value = 0

        rotation_count += 1
        numbers.insert(0, numbers[-1])
        numbers.pop()

        for i in range(len(numbers)):
            pureness_value += numbers[i] * i
            if pureness_value > best_pureness:
                best_pureness = pureness_value
                best_count = rotation_count

    return f"Best pureness {best_pureness} after {best_count} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
