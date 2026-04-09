# Problem
# input: string of digits OR string of digits preceded by + or
# - sign
# output: appropriate positive or negative integer
# rules:
#   -all inputs will be valid
#   -can have +, -, or no sign in front

# data structures:
#   - strings, ints. Range. 

# Algorithm:
# 1. Initiate "sign" as None. 
# 2. If the first character of the string is a plus or minus sign,
#   remove that character and reassign it to variable "sign". 
# 3. Use the conversion function from previous exercise to convert
#   the string to an integer. 
# 4. If "sign" equals None or "+", return the integer. If sign 
#   equals "-", subtract your integer from 0 and return the result.


DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def digit_char_to_digit(character):
    return DIGITS[character]    

def string_to_integer(given_string):
    working_str = given_string[::-1]
    result_val = 0
    for idx in range(len(working_str)):
        result_val += digit_char_to_digit(working_str[idx]) * (10 ** idx)
    return result_val

def string_to_signed_integer(signed_str):
    sign = None
    if signed_str[0] in ["+", "-"]:
        sign = signed_str[0]
        signed_str = signed_str.lstrip("+-")
    new_int = string_to_integer(signed_str)
    if sign in ["+", None]:
        return new_int
    return (0 - new_int)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True