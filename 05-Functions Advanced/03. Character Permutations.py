def char_permutations(index, values):
    if index == len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        char_permutations(index+1, values)
        values[i], values[index] = values[index], values[i]


char_permutations(0, list(input()))
# input() = "abc"
# input() = "12"