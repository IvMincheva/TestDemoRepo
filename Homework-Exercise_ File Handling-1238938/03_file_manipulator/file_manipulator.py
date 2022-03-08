import os
ERROR_MESSAGE = "An error occurred"
command_list = input()
while command_list != "End":
    tokens = command_list.split('-')
    command = tokens[0]
    file_name = tokens[1]
    # print(tokens)
    if command == "Create":
        open(f"{file_name}", 'w').close()
    elif command == "Add":
        content = tokens[2]
        with open(f"{file_name}", 'a') as file:
            file.write(content+'\n')
    elif command == "Replace":
        old_string = tokens[2]
        new_string = tokens[3]
        try:
            with open(f"{file_name}", 'r+') as file:
                line = file.read()
                line = line.replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(line)
        except FileNotFoundError:
            print(ERROR_MESSAGE)

    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(ERROR_MESSAGE)

    command_list = input()

