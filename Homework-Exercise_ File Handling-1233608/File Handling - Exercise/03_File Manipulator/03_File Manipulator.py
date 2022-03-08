import os
def file_manipulator():
    commands = input()
    while commands != "End":
        command = commands.split("-")
        action = command[0]
        file_name = command[1]

        if action == "Create":
            open(file_name, 'w').close()

        elif action == "Add":
            content = command[2]
            with open(file_name, 'a') as file_add:
                file_add.write(content)
                file_add.write('\n')
        elif action == "Replace":
            old_string = command[2]
            new_strings = command[3]
            if not os.path.exists(file_name):
                print("An error occurred")
            else:
                with open(file_name, 'r+') as file_read:
                    content = file_read.read()
                    content = content.replace(old_string, new_strings)
                    file_read.seek(0)
                    file_read.truncate()
                    file_read.write(content)
        elif action == "Delete":
            if not os.path.exists(file_name):
                print("An error occurred")
            else:
                os.remove(file_name)

        commands = input()
file_manipulator()