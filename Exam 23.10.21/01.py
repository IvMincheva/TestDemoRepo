import sys
from io import StringIO
from collections import deque

test_input1 = '''105 20 30 25
120 60 11 400 10 1
'''
test_input2 = '''30 5 21 6 0 91
15 9 5 15 8
'''
test_input3 = '''200
5 15 32 20 10 5
'''

# sys.stdin = StringIO(test_input2)

materials = [int(x) for x in input().split()]
genie_magic = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and genie_magic:
    mat = materials.pop()
    magic = genie_magic.popleft()
    sum_for_present = mat + magic

    if sum_for_present < 100:
        if sum_for_present % 2 == 0:
            mat *= 2
            magic *= 3
            sum_for_present = mat + magic
        else:
            sum_for_present *= 2

    if sum_for_present >= 500:
        sum_for_present /= 2

    if 100 <= sum_for_present < 200:
        presents["Gemstone"] += 1
    elif 200 <= sum_for_present < 300:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= sum_for_present < 400:
        presents["Gold"] += 1
    elif 400 <= sum_for_present < 500:
        presents["Diamond Jewellery"] += 1

if (presents["Gemstone"] >= 1 and presents["Porcelain Sculpture"] >= 1) or \
        (presents["Gold"] >= 1 and presents["Diamond Jewellery"] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if genie_magic:
    print(f"Magic left: {', '.join([str(x) for x in genie_magic])}")

for key, value in sorted(presents.items()):
    if presents[key] >= 1:
        print(f"{key}: {value}")
