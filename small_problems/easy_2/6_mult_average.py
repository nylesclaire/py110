## Problem
# input: list of positive integers
# output: string with numeric value inside rounded to 3 decimal places
# rules: 
#   -assuming valid input list w/ only integers

## Data structures 
# The list. The integers inside it. Floats, once we divide. A rounded 
# float, need to remember or look up how to do that. And then convert
# to a string. 

## Algorithm
# 1) Initiate a "product_so_far" variable that is 1. 
# 2) Use a for loop, and multiply each item in the list by the product,
# re-save as the "product_so_far".
# 3) Divide "product_so_far" by the length of the list, and save as 
# "float_result"
# 4) Use f-string formatting to return a string version of "float result"
# displaying 3 decimal places.

def multiplicative_average(given_list):
    product_so_far = 1
    for item in given_list:
        product_so_far *= item
    float_result = product_so_far / len(given_list)
    return f"{float_result:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")