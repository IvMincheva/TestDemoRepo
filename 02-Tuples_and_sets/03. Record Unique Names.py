import sys
from io import StringIO

test_input1 = '''8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
'''

test_input2 = '''7
Lyle
Bruce
Alice
Easton
Shawn
Alice
Shawn
'''

test_input3 = '''6
Adam
Adam
Adam
Adam
Adam
Adam
'''

# sys.stdin = StringIO(test_input1)

n = int(input())
# names = {input() for _ in range(n)}
names = set()

for _ in range(n):
    names.add(input())
[print(name) for name in names]