first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())
for _ in range(n):
    line_args = input().split()
    command = line_args[0]

    if command == "Add" and line_args[1] == "First":
        [first.add(int(x)) for x in line_args[2:]]
        # for idx in range(2, len(line_args)):
        #     first.add(int(line_args[idx]))
    elif command == "Add" and line_args[1] == "Second":
        [second.add(int(x)) for x in line_args[2:]]
        # for idx in range(2, len(line_args)):
        #     second.add(int(line_args[idx]))
    elif command == "Remove" and line_args[1] == "First":
        current_set = set([(int(x)) for x in line_args[2:]])
        first = first.difference(current_set)
    elif command == "Remove" and line_args[1] == "Second":
        current_set = set([(int(x)) for x in line_args[2:]])
        second = second.difference(current_set)
    elif command == "Check":
        print(first.issubset(second) or second.issubset(first))

print(', '.join([str(x) for x in sorted(first)]))
print(', '.join([str(x) for x in sorted(second)]))
