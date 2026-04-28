# my first attempt - works but ugly
def rotate_rightmost_digits1(num, count):
    if count == 1:
        return num
    str_num = str(num)
    return int(str_num[:-(count)] + str_num[-(count - 1):] + str_num[-count])


# more elegant
def rotate_rightmost_digits(num, count):
    str_num = str(num)
    return int(str_num[:-count] + rotate_first_char(str_num[-count:]))

def rotate_first_char(given_str):
    return given_str[1:] + given_str[0]


# Test cases
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True