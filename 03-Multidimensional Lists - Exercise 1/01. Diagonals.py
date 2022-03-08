import sys
from io import StringIO

test_input1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''

# sys.stdin = StringIO(test_input1)


def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

sum_of_primary = []
sum_of_secondary = []
n = len(matrix)

# for r in range(n):
#     for c in range(n):
#         if r == c:
#             primary_element = matrix[r][c]
#             sum_of_primary.append(primary_element)
#         if r == n - c - 1:
#             secondary_el = matrix[r][c]
#             sum_of_secondary.append(secondary_el)

for row in range(n):
    sum_of_primary.append(matrix[row][row])
    sum_of_secondary.append(matrix[row][n - row - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in sum_of_primary])}. Sum: {sum(sum_of_primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sum_of_secondary])}. Sum: {sum(sum_of_secondary)}")
