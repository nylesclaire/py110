## Problem
# input: whole number / non-negative integer
# output: string representation of that number
# rules: -Do not use conversion functions
#       -"construct the string by analyzing and manipulating the number"


## Algorithm
# 1. Determine number of digits:
#   - loop, dividing by increasing powers of 10 until the dividend
#   is less than 1. That power is the "number of digits"
# 2. Take original number again and floor divide by 10 ^
#   "number of digits" minus 1, that dividend can be saved to "current
#   digit".
# 3. Convert "current digit" via dict to a str char
#   and save to "result string" (prev initialized to "")
# 4. Subtract ("current digit" * 10) from the orig. number, and
#   1 from the "number of digits".
# 5. Repeat steps 2-4 until "number of digits" is 0.

DIGIT_CHARS = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

def determine_num_of_digits(given_int):
    if given_int == 0:
        return 1
    else:
        dividend = 1
        power = -1
        while dividend >= 1:
            power += 1
            dividend = given_int / (10 ** power)
        return power

def integer_to_string(our_int):
    result_str = ""
    current_num_of_digits = determine_num_of_digits(our_int)
    while current_num_of_digits > 0:
        current_digit = our_int // (10 ** (current_num_of_digits - 1))
        result_str += DIGIT_CHARS[current_digit]
        our_int -= current_digit * (10 ** (current_num_of_digits - 1))
        current_num_of_digits -= 1
    return result_str

# Test cases
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
