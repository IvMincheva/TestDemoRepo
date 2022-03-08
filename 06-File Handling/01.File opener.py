file_name = 'text.txt'
# x - create new file, throw if existing
# file = open("sample-x.txt", "x")

# w - create new file or overwrite existing
# file = open("sample-w.txt", "w")

# a - create new file or append to existing
# file = open("sample-a.txt", "a")

try:
    open(file_name, 'r')
    print("File found")
except:
    print("File not found")
