def even_lines():
    symbols = {"-", ",", ".", "!", "?"}
    try:
        with open('text.txt', 'r') as file_text:
            for index_line, line in enumerate(file_text):
                if index_line % 2 == 0:
                    for symbol in symbols:
                        line = line.replace(symbol, "@")
                    l_line = line.split()
                    reverse_line = l_line[::-1]
                    print(' '.join(reverse_line))
    except FileNotFoundError:
        print("FileNotFoundError")
even_lines()