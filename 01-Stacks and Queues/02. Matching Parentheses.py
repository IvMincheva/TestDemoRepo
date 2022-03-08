expression = input()
parentheses_index = []

for index, ch in enumerate(expression):
    if ch == "(":
        parentheses_index.append(index)
    elif ch == ")":
        closing_index = index
        opening_index = parentheses_index.pop()
        print(expression[opening_index:closing_index + 1])


# expression = input()
# stack = []
#
# for index in range(len(expression)):
#     if expression[index] == "(":
#         stack.append(index)
#     elif expression[index] == ")":
#         start_index = stack.pop()
#         print(expression[start_index:index+1])
