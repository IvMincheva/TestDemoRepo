# file = open("my_first_file.txt", "w")
#
# file.write("'I just created my first file!'")


# def write_to_file(file_path, mode, text):
#     file = open(file_path, mode)
#     file.write(text)
#     file.close()
#
#
# write_to_file("my_first_file.txt", "w", '''I just created my first file!''')


file_path = "my_first_file.txt"
content = 'I just created my first file!'

with open(file_path, "w") as file:
    file.write(content)
