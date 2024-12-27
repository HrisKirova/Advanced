def fill_the_box(*args):
    for i in range(len(args)): # to get the index: args.index("Finish")
        if args[i] == "Finish":
            args = args[:i]
            size_of_box = args[0] * args[1] * args[2]
            sum_cubes = sum(args[3:])
            if size_of_box >= sum_cubes:
                return f"There is free space in the box. You could put {size_of_box - sum_cubes} more cubes."
            else:
                return f"No more free space! You have {sum_cubes - size_of_box} more cubes."

# def fill_the_box(*args):
#     # Extract dimensions of the box and the cubes
#     length, width, height, *cubes = args
#     # Calculate the box volume
#     size_of_box = length * width * height
#
#     # Sum the cubes until "Finish" is encountered
#     total_cubes = 0
#     for cube in cubes:
#         if cube == "Finish":
#             break
#         total_cubes += cube
#
#     # Compare box capacity with total cubes
#     if size_of_box >= total_cubes:
#         return f"There is free space in the box. You could put {size_of_box - total_cubes} more cubes."
#     else:
#         return f"No more free space! You have {total_cubes - size_of_box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))