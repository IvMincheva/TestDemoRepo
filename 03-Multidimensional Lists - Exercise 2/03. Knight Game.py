import sys
from io import StringIO

test_input1 = '''5 
0K0K0
K000K
00K00
K000K
0K0K0
'''
test_input2 = '''2
KK
KK
'''
test_input3 = '''8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
'''

# sys.stdin = StringIO(test_input3)


def is_knight_placed(board, row, col):
    board_size = len(board)
    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == "K"


def count_affected_knights(board, row, col):
    result = 0

    if is_knight_placed(board, row - 2, col - 1):
        result += 1
    if is_knight_placed(board, row - 2, col + 1):
        result += 1
    if is_knight_placed(board, row + 2, col - 1):
        result += 1
    if is_knight_placed(board, row + 2, col + 1):
        result += 1
    if is_knight_placed(board, row - 1, col - 2):
        result += 1
    if is_knight_placed(board, row - 1, col + 2):
        result += 1
    if is_knight_placed(board, row + 1, col - 2):
        result += 1
    if is_knight_placed(board, row + 1, col + 2):
        result += 1
    return result


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0
while True:
    max_count = 0
    knight_row = 0
    knight_col = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "0":
                continue
            count = count_affected_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)