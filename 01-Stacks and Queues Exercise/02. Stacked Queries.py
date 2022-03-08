n = int(input())
stack = []

for _ in range(n):
    el = input().split()
    command = el[0]
    if command == "1":
        stack.append(int(el[1]))
    elif command == "2":
        #if len(stack) > 0:
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

# reversed_stack = []
# while stack:
#     reversed_stack.append(str(stack.pop()))
# print(', '.join(reversed_stack))

while stack:
    el = stack.pop()
    if stack:
        print(el, end=", ")
    else:
        print(el)
