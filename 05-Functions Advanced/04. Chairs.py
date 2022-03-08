def generate_combinations(values, index, count, comb):
    if len(comb) == count:
        print(", ".join(comb))
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combinations(values, i+1, count, comb)
        comb.pop()


names = input().split(", ")
count = int(input())
generate_combinations(names, 0, count, [])

test1 = '''Peter, George, Amy
2
'''
test2 = '''Mariya, Emilly, Tom, Bob
1
'''