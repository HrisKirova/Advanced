def age_assignment(*names, **kwargs):
    assignment = {}
    for name in names:
        for key, value in kwargs.items():
            if name[0] == key:
                assignment[name] = value

    assignment = sorted(assignment.items())
    return "\n".join(f"{name} is {age} years old" for name, age in assignment)

# def age_assignment(*names, **kwargs):
#     # Use a dictionary comprehension to directly map names to ages
#     assignment = {name: kwargs[name[0]] for name in names}
#     # Sort by name and format the output
#     return "\n".join(f"{name} is {age} years old" for name, age in sorted(assignment.items()))
#


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))