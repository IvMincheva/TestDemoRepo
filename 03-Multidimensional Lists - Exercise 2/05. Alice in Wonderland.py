import sys
from io import StringIO

test_input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''
test_input2 = '''7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
'''

# sys.stdin = StringIO(test_input2)


def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == "up":
        return r-1, c
    if direction == "down":
        return r+1, c
    if direction == "left":
        return r, c-1
    return r, c+1


size = int(input())

matrix = []

alice_row, alice_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        el = elements[col]
        if el == "A":
            alice_row, alice_col = row, col

matrix[alice_row][alice_col] = "*"
tea_bags = 0

while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)
    if is_outside(alice_row, alice_col, size):
        break
    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"
    if cell_value == "R":
        break
    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(' '.join(row))