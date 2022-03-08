def counter_letters(text):
    counter_letters = 0
    counter_punctuation = 0
    symbols = {"-", ",", ".", "!", "?", ";", ":", "_", "'"}
    for letter in text:
        if letter.isalpha():
            counter_letters += 1
        elif letter in symbols:
            counter_punctuation += 1

    return counter_letters, counter_punctuation

def line_numbers():
    new_lines = ""
    try:
        with open('text.txt', 'r') as file_text, open("output.txt", 'w') as file_output:
            for index_line, line in enumerate(file_text, 1):
                number_of_letters, number_of_punctuation = counter_letters(line)
                line = f"Line {index_line}: {line.strip()} ({number_of_letters}) ({number_of_punctuation})"
                file_output.write(line)
                file_output.write('\n')

    except FileNotFoundError:
        print("FileNotFoundError")

    #try:
        #with open("output.txt", 'w') as file_output:

line_numbers()