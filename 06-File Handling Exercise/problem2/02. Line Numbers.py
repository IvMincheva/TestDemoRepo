punct = {',', '.', '?', '!', "'", '-', ';', ':', '_', '"'}

with open("text.txt", "r") as file, open("output.txt", "w") as result:
    idx = 1
    for line in file:
        # print(line.strip())
        letters_count = 0
        punct_count = 0
        for ch in line:
            if ch in punct:
                punct_count += 1
            elif ch.isalpha():
                letters_count += 1
        result.write(f"Line {idx}: {line.strip()} ({letters_count})({punct_count})")
        result.write("\n")
        idx += 1
