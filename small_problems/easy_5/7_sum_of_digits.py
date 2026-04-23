
def sum_digits(num):
    return sum([int(item) for item in str(num)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True