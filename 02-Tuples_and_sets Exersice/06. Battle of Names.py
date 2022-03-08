n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

result = set()
if even_sum == odd_sum:
    result = odd.union(even)
elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)

print(", ".join([str(x) for x in result]))
