command = input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == "Even" else 1
filter_sum = sum(filter(lambda x: x % 2 == parity, numbers))

# if command == "Even":
#     filter(lambda x: x % 2 == 0, numbers)
# elif command == "Odd":
#     filter(lambda x: x % 2 == 1, numbers)

print(filter_sum * len(numbers))

# test1 = '''Odd
# 1 3 5 34 7 9 12 11 13 10
# '''
# test2 = '''Even
# 1 3 5 7 9 13
# '''
