from collections import deque

# Mapping magic levels to presents
required_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

def process_zeros(materials, magic_level):
    """Removes zeros from materials and magic levels."""
    while materials and materials[-1] == 0:
        materials.pop()
    while magic_level and magic_level[0] == 0:
        magic_level.popleft()

def calculate_magic(material, magic, materials, presents):
    """Handles the crafting logic based on total magic."""
    total_magic = material * magic
    if total_magic in required_magic:
        present = required_magic[total_magic]
        presents[present] = presents.get(present, 0) + 1
    elif total_magic < 0:
        materials.append(material + magic)  # Add when the product is negative
    elif total_magic > 0:
        materials.append(material + 15)    # Increase material when unmatched magic

def check_success(presents):
    """Checks if the crafting task is successful."""
    return ("Doll" in presents and "Wooden train" in presents) or \
           ("Teddy bear" in presents and "Bicycle" in presents)

def print_results(materials, magic_level, presents):
    """Prints the final results."""
    if check_success(presents):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    # Print remaining materials and magic levels
    if materials:
        print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
    if magic_level:
        print(f"Magic left: {', '.join(map(str, magic_level))}")

    # Print crafted presents in alphabetical order
    for present, count in sorted(presents.items()):
        print(f"{present}: {count}")

# Main program logic
def main():
    # Input data
    materials = deque(map(int, input().split()))
    magic_level = deque(map(int, input().split()))
    presents = {}

    # Process crafting loop
    while materials and magic_level:
        process_zeros(materials, magic_level)
        if not materials or not magic_level:  # Ensure no empty collections
            break

        # Get the current material and magic value
        material = materials.pop()
        magic = magic_level.popleft()

        # Calculate crafting logic
        calculate_magic(material, magic, materials, presents)

    # Print final results
    print_results(materials, magic_level, presents)

# Run the program
if __name__ == "__main__":
    main()
