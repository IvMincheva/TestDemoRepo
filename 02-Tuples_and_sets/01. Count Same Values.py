import sys
from io import StringIO

test_input1 = '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'
test_input2 = '2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'

# sys.stdin = StringIO(test_input2)

number_counts = {}

numbers = [float(x) for x in input().split(" ")]

for number in numbers:
    if number not in number_counts:
        number_counts[number] = 0
    number_counts[number] += 1

for number, count in number_counts.items():
    print(f"{number} - {count} times")