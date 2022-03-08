import sys
from io import StringIO

test_input1 = '''. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
'''
test_input2 = '''. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .
'''

# sys.stdin = StringIO(test_input1)


def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


board = []
n = 8
for _ in range(n):
    board.append([str(x) for x in input().split()])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1),
}

queens = []
for r in range(len(board)):
    for c in range(len(board)):
        if board[r][c] == "Q":
            for direction in directions:
                next_row = r + directions[direction][0]
                next_col = c + directions[direction][1]
                while is_in_range(next_row, next_col, n):
                    if board[next_row][next_col] == "Q":
                        break
                    if board[next_row][next_col] == "K":
                        queens.append([r, c])
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if queens:
    [print(position) for position in queens]
else:
    print("The king is safe!")