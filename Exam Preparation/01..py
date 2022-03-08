import sys
from io import StringIO
from collections import deque

test_input1 = '''5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
'''
test_input2 = '''-15, -8, 0, -16, 0, -22
10, 5
'''

# sys.stdin = StringIO(test_input1)

fireworks = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

palm_firework = 0
willow_firework = 0
crossette_firework = 0
perfect_show = False

while fireworks:
    el = fireworks[0]
    if el <= 0:
        fireworks.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    total = el + explosive_power[-1]
    if total % 3 == 0 and total % 5 == 0:
        crossette_firework += 1
        fireworks.popleft()
        explosive_power.pop()

    elif total % 3 == 0:
        palm_firework += 1
        fireworks.popleft()
        explosive_power.pop()

    elif total % 5 == 0:
        willow_firework += 1
        fireworks.popleft()
        explosive_power.pop()
    else:
        new_el = el-1
        fireworks.append(new_el)
        fireworks.popleft()

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        print("Congrats! You made the perfect firework show!")
        perfect_show = True
        break

if not perfect_show:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")