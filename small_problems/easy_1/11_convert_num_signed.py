
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

def signed_integer_to_string(given_integer):
    if given_integer < 0:
        return f"-{integer_to_string(abs(given_integer))}"
    elif given_integer > 0:
        return f"+{integer_to_string(given_integer)}"
    else:
        return "0"

# Test cases
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True