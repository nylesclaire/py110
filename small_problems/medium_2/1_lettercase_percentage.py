## Problem
# input: string
# output: dictionary w/ 3 items
# rules:
#   -the three percentages should be between 0.00 and 100.00 and be 
#   rounded to 2 decimal points
#   -the string will always contain at least 1 character

## Data Structures
# the o.g. string
# the dictionary, containing keys that are strings and values that are floats

## Algorithm
# 1. loop through the string. For each character, update one of 3 "small totals"
#   as appropriate: lowercase, uppercase, neither (by performing predicate
#   methods to determine)
# 2. Determine and save the total number of characters in the string. ("total")
# 3. For each of the three small totals, divide them by "total", then multiply
#   by 100. Assign that number to a dictionary value, paired with an appropriate
#   descriptive key.
# 4. Return the dictionary. 


def letter_percentages1(given_string):
    lower_tot = 0
    upper_tot = 0
    neither_tot = 0
    total = len(given_string)

    for char in given_string:
        if char.islower():
            lower_tot += 1
        elif char.isupper():
            upper_tot += 1
        else:
            neither_tot += 1
    
    result_dict = {}
    result_dict['lowercase'] = f"{((lower_tot / total) * 100):.2f}"
    result_dict['uppercase'] = f"{((upper_tot / total) * 100):.2f}"
    result_dict['neither'] = f"{((neither_tot / total) * 100):.2f}"

    return result_dict

# ----------------------------------------------------

def percentage(small_number, total):
    return f"{((small_number / total) * 100):.2f}"


def letter_percentages(given_string):
    lower_tot = upper_tot = neither_tot = 0
    total = len(given_string)

    for char in given_string:
        if char.islower():
            lower_tot += 1
        elif char.isupper():
            upper_tot += 1
        else:
            neither_tot += 1

    result_dict = {
        "lowercase": percentage(lower_tot, total),
        "uppercase": percentage(upper_tot, total),
        "neither": percentage(neither_tot, total),
    }

    return result_dict




## Examples/ Test cases
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)