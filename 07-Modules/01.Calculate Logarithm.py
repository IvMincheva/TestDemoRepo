import math


def calculated_log(x, base_as_str):
    if base_as_str == "natural":
        return math.log(x)

    base = int(base_as_str)
    return math.log(x, base)


print(f'{calculated_log(10, 10):.2f}')
print(f'{calculated_log(1024, 2):.2f}')
print(f'{calculated_log(1024*1024, 2):.2f}')
print(f'{calculated_log(10, "natural"):.2f}')
