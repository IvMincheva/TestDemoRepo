import sys
from io import StringIO

test_input1 = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''
test_input2 = '''1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
'''

# sys.stdin = StringIO(test_input1)


def read_matrix():
    n, m = [int(x) for x in input().split()]

    matrix = []

    for _ in range(n):

        # row = [str(x) for x in input().split(' ')]
        row = input().split(' ')
        matrix.append(row)
    return matrix


def is_valid_position(r, c, n, m):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    return True


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

while True:
    line = input()
    if line == 'END':
        break

    args = line.split()
    if args[0] != "swap" or len(args) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in args[1:]]
    if not is_valid_position(row1, col1, n, m) or not is_valid_position(row2, col2, n, m):
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row_el in matrix:
        print(' '.join([str(x) for x in row_el]))
