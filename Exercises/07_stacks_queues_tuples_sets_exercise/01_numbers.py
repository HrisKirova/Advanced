# Read initial sequences
first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

# Process commands
for _ in range(int(input())):
    command_line = input().split()
    first, second, *details = command_line

    # Parse the command and numbers
    command = f"{first} {second}"
    numbers = list(map(int, details)) if details else []

    if command == "Add First":
        first_sequence.update(numbers)  # Add multiple numbers to the first sequence
    elif command == "Add Second":
        second_sequence.update(numbers)  # Add multiple numbers to the second sequence
    elif command == "Remove First":
        first_sequence -= set(numbers)  # Remove numbers from the first sequence
        # first_sequence.difference_update(numbers) -> does the same as -=
    elif command == "Remove Second":
        second_sequence -= set(numbers)  # Remove numbers from the second sequence
    elif command == "Check Subset":
        # Check if one set is a subset of the other
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        # print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence)) => returns True or False
        else:
            print("False")

# Print the final sequences in sorted order
print(", ".join(map(str, sorted(first_sequence))))
# print(*sorted(first_sequence, sep= ", ")) -> works too
print(", ".join(map(str, sorted(second_sequence))))
