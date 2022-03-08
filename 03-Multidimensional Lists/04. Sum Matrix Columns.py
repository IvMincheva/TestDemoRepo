import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''
test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''

# sys.stdin = StringIO(test_input2)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

n = len(matrix)
m = len(matrix[0])
column_sums = [0] * m

for row_index in range(n):
    for column_index in range(m):
        value = matrix[row_index][column_index]
        column_sums[column_index] += value

# for el in column_sums:
#     print(el)
[print(x) for x in column_sums]