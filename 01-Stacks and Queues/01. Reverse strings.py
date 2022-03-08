# text = input()
# ss = []
#
# for ch in text:
#     ss.append(ch)
#
# result = ''
#
# while len(ss) > 0:
#     result += ss.pop()
#
# print(result)

word = list(input())
stack = []

while word:
    stack.append(word.pop())

print(f"".join(stack))