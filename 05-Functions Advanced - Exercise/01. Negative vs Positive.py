numbers = [int(x) for x in input().split()]
positive_sum = sum(filter(lambda x: x > 0, numbers))
negative_sum = sum(filter(lambda x: x < 0, numbers))

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > abs(positive_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

# test1 = '''1 2 -3 -4 65 -98 12 57 -84'''
# test2 = '''1 2 3'''