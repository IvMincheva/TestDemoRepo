from collections import deque

numbers = [int(x) for x in input().split(", ")]
searched_index = int(input())

result = 0
clock_cycles = deque(sorted([(numbers[index], index) for index in range(len(numbers))]))

while clock_cycles:
    number, index = clock_cycles.popleft()
    result += number
    if index == searched_index:
        print(result)
        break
