from collections import deque

queue = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        while queue:
            print(queue.pop())
    else:
        queue.appendleft(command)


# from collections import deque
#
# name = input()
# queue = deque()
#
# while name != "End":
#
#     if name == "Paid":
#         while queue:
#             print(queue.popleft())
#     else:
#         queue.append(name)
#
#     name = input()
# print(f"{len(queue)} people remaining.")
