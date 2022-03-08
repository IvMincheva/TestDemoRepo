import os

if "my_first_file.txt" in os.listdir("."):
    os.remove("my_first_file.txt")
else:
    print("File already deleted!")


# if os.path.exists("my_first_file.txt"):
#     os.remove("my_first_file.txt")
# else:
#     print("File already deleted!")
