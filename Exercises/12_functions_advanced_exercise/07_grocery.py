def grocery_store(**kwargs):

    # Sort by quantity (descending), name length (descending), and name (ascending)

    sorted_groceries = sorted(kwargs.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

    # Format the output string
    result = "\n".join(f"{name}: {quantity}" for name, quantity in sorted_groceries)
    return result

# Example usage
print(grocery_store(bread=5, pasta=12, eggs=12))
print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
