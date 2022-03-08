class ValueCannotBeNegativeError(Exception):
    # def __init__(self, min_value):
    #     super().__init__(f"The value must be positive or greater than {min_value}!")
    pass


numbers = [int(input()) for _ in range(5)]
#
# try:
for number in numbers:
    if number < 0:
        raise ValueCannotBeNegativeError
#     print("No exception")
#
# except:
#     print("Exception handled")