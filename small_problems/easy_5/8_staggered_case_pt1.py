
def staggered_case(given_str):
    result_str = ""
    for idx in range(len(given_str)):
        if idx % 2 == 0:
            result_str += given_str[idx].upper()
        else:
            result_str += given_str[idx].lower()
    return result_str


# Test cases
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True