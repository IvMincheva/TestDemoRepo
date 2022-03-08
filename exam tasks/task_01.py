
a = [8, 5, 6, 16, 5]
l = 1
r = 3

b = []
el = ''
for index in range(0, len(a)):
    x = int(a[index]/(index + 1))
    if l <= x <= r and (a[index] == (index + 1) * x):
        el = 'true'
        b.append(el)
    else:
        el = 'false'
        b.append(el)

print(b)