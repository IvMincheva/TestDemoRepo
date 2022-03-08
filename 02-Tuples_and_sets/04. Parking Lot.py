import sys
from io import StringIO

test_input1 = '''11
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9999TT
IN, CA9876HH
IN, CA2822UU
'''
test_input2 = '''4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA
'''

# sys.stdin = StringIO(test_input1)

n = int(input())

parking_lot = set()

for _ in range(n):
    command, car = input().split(", ")
    if command == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print('Parking Lot is Empty')
