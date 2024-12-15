number_of_names = int(input())
unique_names = set()
for _ in range(number_of_names):
    new_entry = input()
    unique_names.add(new_entry)

print("\n".join(unique_names))