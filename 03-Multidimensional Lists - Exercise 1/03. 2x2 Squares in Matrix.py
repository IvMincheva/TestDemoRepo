import sys
from io import StringIO

test_input1 = '''3 4
A B B D
E B B B
I J B B
'''
test_input2 = '''2 2
a b
c d
'''
test_input3 = '''5 4
A A B D
A A B B
I J B B
C C C G
C C K P
'''

sys.stdin = StringIO(test_input3)


def read_matrix():
    n, m = [int(x) for x in input().split()]

    matrix = []

    for _ in range(n):
        row = [str(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])

count = 0
for r in range(n-1):
    for c in range(m-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            count += 1
print(count)
