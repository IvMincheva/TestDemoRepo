ll = [1, 2, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
target = 9

c = 1
n = len(ll)
for i in range(n):
    for j in range(n):
        c += 1
        if i == j:
            continue
        if ll[i] + ll[j] == target:
            print(ll[i], ll[j])

print(f"Total iterations: {c}")
print(f"Total el: {n}")

remainders = set()
c = 0
for x in ll:
    c += 1
    if x in remainders:
        print(x)
    remainders.add(target - x)
print(f"Total iterations: {c}")