import os


def traverse_directories(dir_path, files_dict):

    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            extension = file.split('.')[-1]
            if extension not in files_dict.keys():
                files_dict[extension] = []
            files_dict[extension].append(file)
        elif os.path.isdir(os.path.join(dir_path, file)):

            traverse_directories(os.path.join(dir_path, file), files_dict)


result_dict = {}
traverse_directories(os.getcwd(), result_dict)

with open("report.txt", "w") as file_write:
    for key, value in sorted(result_dict.items(), key=lambda kvp:kvp[0]):
        file_write.write(f".{key}"+"\n")
        for file_name in sorted(value):
            file_write.write(f"- - - {file_name}"+"\n")
