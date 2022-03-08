numbers_stack = input().split()
result = []

while len(numbers_stack) > 0:
    el = numbers_stack.pop()
    result.append(el)
print(" ".join(result))
