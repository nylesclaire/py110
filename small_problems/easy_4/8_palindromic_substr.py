### Problem
# I actually think I can just combine multiple prev functions
# in the body of a new function and call it a day
# Or! Edit my "is_palindrome" one slightly to account for single letters

def is_palindrome(str_input):
    if len(str_input) < 2:
        return False
    else: 
        return str_input == str_input[::-1]

def leading_substrings(str_word):
    return [str_word[:idx] for idx in range(1, len(str_word) + 1)]

def substrings(given_str):
    return [substring 
            for idx in range(len(given_str) + 1)
            for substring in leading_substrings(given_str[idx:])
    ]

def palindromes(str1):
    substrings_list = substrings(str1)
    return [item for item in substrings_list if (is_palindrome(item))]


# Test cases
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True