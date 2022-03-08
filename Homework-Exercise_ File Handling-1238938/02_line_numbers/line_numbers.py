import string

path_to_text= 'text.txt'
path_to_write = 'output.txt'
letters = string.ascii_letters
punctuation_marks = string.punctuation
counter = 0
with open(path_to_text, 'r') as file_to_read, open(path_to_write, 'w') as file_to_write:
    for row in file_to_read:
        counter +=1
        count_letters = len(list(filter(lambda x: x in letters, row)))
        count_punctuation_marks = len(list(filter(lambda x: x in punctuation_marks,row)))
        file_to_write.write(f"{counter}: {row.strip()} ({count_letters})({count_punctuation_marks})\n")

