import os


def traverse_directories(dir_path, result):
    for x in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, x)
        if os.path.isfile(file_with_path):
            ext = x.split(".")[-1]
            if ext not in result:
                result[ext] = []
            result[ext].append(file_with_path)
        elif os.path.isdir(file_with_path):
            traverse_directories(file_with_path, result)


result = {}
traverse_directories(os.getcwd(), result)

with open("report.txt", "w") as result_file:
    for ext, files in sorted(result.items()):
        result_file.write(f".{ext}")
        result_file.write("\n")
        for file in sorted(files):
            result_file.write(f"--- {file}")
            result_file.write("\n")
