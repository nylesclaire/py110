

def staggered_case1(given_str):
    result_str = ""
    alpha_idx = -1
    for char in given_str:
        if char.isalpha():
            alpha_idx += 1
            if alpha_idx % 2 == 0:
                result_str += char.upper()
            else:
                result_str += char.lower()
        else: 
            result_str += char
    return result_str


def staggered_case(given_str):
    result_str = ""
    upper_tog = False
    for char in given_str:
        if char.isalpha():
            upper_tog = not upper_tog
            if upper_tog:
                result_str += char.upper()
            else:
                result_str += char.lower()
        else: 
            result_str += char
    return result_str


# Test cases
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True