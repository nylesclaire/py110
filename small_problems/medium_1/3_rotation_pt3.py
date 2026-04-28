### Problem
# input: integer
# output: "fully rotated" integer


### Data Structures
# ints, strings

### Algorithm
# 1) convert og number to string
# 2) start count at length of the string; initiate a result_str for us
#   to modify/ reassign as we go
# 3) loop through the chars of your string, and on each:
#   -perform the rotate_rightmost_digits w/ the current count as count
#   -reassign the result to "result_str"
#   -decrease the count
# 4) convert the result string to an int and return it




# From last exercise
def rotate_rightmost_digits(num, count):
    str_num = str(num)
    return int(str_num[:-count] + rotate_first_char(str_num[-count:]))

def rotate_first_char(given_str):
    return given_str[1:] + given_str[0]

# Modified it to use strings
def rotate_rightmost_chars(my_str, count):
    return my_str[:-count] + rotate_first_char(my_str[-count:])


# my first solution; why did I want to make everything a string?
def max_rotation1(given_num):
    og_str_num = str(given_num)
    current_count = len(og_str_num)
    result_str = og_str_num
    for char in og_str_num: 
        result_str = rotate_rightmost_chars(result_str, current_count)
        current_count -= 1
    return int(result_str)


# with some tweaking to fix that loop etc
def max_rotation(given_num):
    new_num = given_num
    for count in range(len(str(given_num)), 0, -1):
        new_num = rotate_rightmost_digits(new_num, count)
    return new_num
        

### Test cases
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True
print(max_rotation(105) == 15)                 # True