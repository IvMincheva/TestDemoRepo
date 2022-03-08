clothes = [int(x) for x in input().split()]

rack_capacity = int(input())

used_racks = 1
current_rack = rack_capacity

while clothes:
    clothing = clothes[-1]
    if clothing > current_rack:
        used_racks += 1
        current_rack = rack_capacity
    else:
        current_rack -= clothing
        clothes.pop()

print(used_racks)