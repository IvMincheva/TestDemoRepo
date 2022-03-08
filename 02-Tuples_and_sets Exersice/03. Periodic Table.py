n = int(input())
chemical_el = set()

for _ in range(n):
    # elements = input().split()
    # for el in elements:
    #     chemical_el.add(el)
    [chemical_el.add(x) for x in input().split()]

# for each in chemical_el:
#     print(each)

[print(x) for x in chemical_el]