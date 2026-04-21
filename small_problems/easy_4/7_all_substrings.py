### Problem
# input: string
# output: list of all substrings
# rules: 
#   - the list must be ordered by where in the string the substring begins
#   - at each starting index, order them from shortest to longest
#   - use the function we just wrote in previous small problem. 

def leading_substrings(str_word):
    return [str_word[:idx] for idx in range(1, len(str_word) + 1)]

def substrings1(given_str):
    result_list = []
    for item in [given_str[idx:] for idx in range(len(given_str) + 1)]:
        result_list.extend(leading_substrings(item))
    return result_list

def substrings2(given_str):
    result_list = []
    for idx in range(len(given_str) + 1):
        result_list.extend(leading_substrings(given_str[idx:]))
    return result_list

def substrings3(given_str):
    result_list = []
    for idx in range(len(given_str) + 1):
        result_list += leading_substrings(given_str[idx:])
    return result_list

def substrings(given_str):
    return [substring 
            for idx in range(len(given_str) + 1)
            for substring in leading_substrings(given_str[idx:])
    ]

# Test case
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
print(substrings('abcde') == expected_result)  # True