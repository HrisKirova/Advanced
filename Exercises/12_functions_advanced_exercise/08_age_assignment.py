def age_assignment(*names, **kwargs):
    # Create a dictionary to store the assigned ages
    assignment = {}

    # Assign ages to names based on their first letter
    for name in names:
        first_letter = name[0]  # Get the first letter of the name
        if first_letter in kwargs:
            assignment[name] = kwargs[first_letter]

    # Sort names alphabetically and format the result
    return "\n".join(f"{name} is {age} years old." for name, age in sorted(assignment.items()))


# def age_assignment(*names, **kwargs):
#     # Use a dictionary comprehension to directly map names to ages
#     assignment = {name: kwargs[name[0]] for name in names}
#     # Sort by name and format the output
#     return "\n".join(f"{name} is {age} years old" for name, age in sorted(assignment.items()))
#


print(age_assignment("Peter", "George", G=26, P=19))