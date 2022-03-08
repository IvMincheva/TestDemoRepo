import os
def directory_traversal():
    cwd = os.getcwd()
    d_results = {}
    suffixes = ('.html', '.js', '.pptx', '.py', '.txt')
    for root, dirs, files in os.walk(os.path.join(cwd,'Examples')):
        for file in files:
            if file.endswith(suffixes):
                extention = file.split(".")[1]
                if extention not in d_results:
                    d_results[extention] = []
                d_results[extention].append(file)

    d_results_sorted = dict(sorted(d_results.items(), key=lambda x: x[0]))

    with open('report.txt', 'w') as file_report:

        for key, l_values in d_results_sorted.items():
            file_report.write(f".{key}")
            file_report.write('\n')
            for value in sorted(l_values):
                file_report.write(f'- - - {value}')
                file_report.write('\n')


directory_traversal()