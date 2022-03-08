def get_file_content(path_to_file):
    with open(path_to_file, 'r') as file:
        input_str = file.readlines()
    return input_str


special_symbols = ['-', ',', '.', '!', '?']
path_to_file = "text.txt"
data = get_file_content(path_to_file)


for row in range(0, len(data),  2):
    line = data[row]
    for symbol in special_symbols:
        line = line.strip().replace(symbol, '@')

    reversed_sentence = ' '.join(reversed(line.split()))

    print(reversed_sentence)
