file = open("numbers.txt")

total = 0

for line in file:
    num = int(line)
    total += num

print(total)