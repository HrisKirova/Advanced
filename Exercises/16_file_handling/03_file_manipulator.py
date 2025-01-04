import os

while True:
    commands = input()
    if commands == "End":
        break

    command_parts = commands.split("-")
    action = command_parts[0]
    file_name = command_parts[1]

    if action == "Create":
        # Create or overwrite the file with empty content
        with open(file_name, "w") as file:
            pass

    elif action == "Add":
        # Append content to the file, creating it if necessary
        content = command_parts[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif action == "Replace":
        # Replace old_string with new_string in the file
        old_string = command_parts[2]
        new_string = command_parts[3]
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            # Replace occurrences of old_string with new_string
            with open(file_name, "w") as file:
                for line in lines:
                    file.write(line.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        # Delete the file if it exists
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
