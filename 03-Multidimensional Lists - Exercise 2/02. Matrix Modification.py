import sys
from io import StringIO

test_input1 = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''
test_input2 = '''4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
'''

# sys.stdin = StringIO(test_input2)


def is_invalid_position(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break

    args = line.split()
    command = args[0]
    row, col, value = [int(x) for x in args[1:]]
    if is_invalid_position(size, row, col):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row_el in matrix:
    print(' '.join([str(x) for x in row_el]))