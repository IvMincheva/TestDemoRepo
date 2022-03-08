import sys
from io import StringIO

test_input1 = '''5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
'''
test_input2 = '''3
4
- - - -
V - X -
- V C V
- - - S
left
up
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


def get_houses_in_range(size, r, c):
    houses = []
    if not is_outside(r-1, c, size):
        houses.append([r-1, c])
    if not is_outside(r+1, c, size):
        houses.append([r+1, c])
    if not is_outside(r-1, c-1, size):
        houses.append([r, c-1])
    if not is_outside(r, c+1, size):
        houses.append([r, c+1])
    return houses


presents = int(input())
size = int(input())

matrix = []

santa_row, santa_col = 0, 0
initial_good_kids_count = 0
good_kids_count = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        el = elements[col]
        if el == "S":
            santa_row, santa_col = row, col
        elif el == "V":
            initial_good_kids_count += 1

good_kids_count = initial_good_kids_count

while True:
    line = input()
    if line == "Christmas morning":
        break
    next_santa_row, next_santa_col = get_next_position(line, santa_row, santa_col)
    if matrix[next_santa_row][next_santa_col] == "V":
        good_kids_count -= 1
        presents -= 1

    elif matrix[next_santa_row][next_santa_col] == "C":
        houses_in_range = get_houses_in_range(size, next_santa_row, next_santa_col)
        for row, col in houses_in_range:
            if matrix[row][col] == "X":
                presents -= 1
            if matrix[row][col] == "V":
                presents -= 1
                good_kids_count -= 1
            matrix[row][col] = "-"
            if presents == 0:
                break
    matrix[santa_row][santa_col] = "-"
    matrix[next_santa_row][next_santa_col] = "S"
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents == 0:
        break
if presents == 0 and good_kids_count > 0:
    print("Santa ran out of presents!")

for row_el in matrix:
    print(' '.join(row_el))

if good_kids_count == 0:
    print(f"Good job, Santa! {initial_good_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")