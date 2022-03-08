import sys
from io import StringIO

test_input1 = '''4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
'''
test_input2 = '''3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2
'''

sys.stdin = StringIO(test_input1)


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split(' ')])
    return matrix


matrix = read_matrix()
n = len(matrix)

