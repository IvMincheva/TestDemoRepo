import sys
from io import StringIO

test_input1 = '''10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 B
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)
'''
test_input2 = '''B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)
'''

# sys.stdin = StringIO(test_input1)


def read_matrix():
    n = 6

    matrix = []

    for _ in range(n):
        matrix.append(input().split(' '))

    return matrix


matrix = read_matrix()
n = len(matrix)
buckets = []
position = 0

for r in range(n):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "B":
            buckets.append([r, c])
            position = (r, c)

score = 0
positions = {
    "pos1": 0,
    "pos2": 0,
    "pos3": 0,
}
for _ in range(3):
    coordinates = input()
    for el in positions:
        positions[el] = coordinates
        break
    # row, col = coordinates
    # print(row)
    # print(col)
    if coordinates in buckets:
        print("sdfsdf")
    # for idx in range(len(buckets)):
    #     (r, c) = (buckets[idx][1], buckets[idx][2])
    #     if (r, c) == coordinates:
    #         print("YES")
    #         # r, c = b_position
    #         score += sum(matrix[c])
    #     else:
    #         pass

print(matrix)
print(buckets)
print(position)