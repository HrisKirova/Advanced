def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [n for n in args[:-1] if n % 2 == 0]
    elif command == "odd":
        return [num for num in args[:-1] if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))