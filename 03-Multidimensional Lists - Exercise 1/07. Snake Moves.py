import sys
from io import StringIO

test_input1 = '''5 6
SoftUni
'''
test_input2 = '''1 4
Python
'''

# sys.stdin = StringIO(test_input1)


def read_matrix():
    n, m = [int(x) for x in input().split()]

    matrix = []

    for row in range(n):
        matrix.append([None] * m)
    return matrix


matrix = read_matrix()

word = input()
word_idx = 0
n = len(matrix)
m = len(matrix[0])
for row in range(n):
    for col in range(m):
        if row % 2 == 0:
            matrix[row][col] = word[word_idx]
        else:
            matrix[row][m - 1 - col] = word[word_idx]
        word_idx = (word_idx + 1) % len(word)

[print(''.join(x)) for x in matrix]
