
### Problem
# input: list, optional delimiter, optional final word
# output: string w/ list elements joined w/ a default delimiter and 'or' 
#       before the last one, OR w/ a specified delimiter, OR w/ a specified 
#       delimiter and a specified final word.
# rules: -empty list returns an empty string
#       -single-item list returns the item as a string w/ nothing added
#       -two-item list returns the two elemeents with no delimiter but w/ just 
#       the end word

### Data Structures
# the list.
# strings - final string, delim chars, end_word, spaces
# join. method still? 
# len function for sure

### Algorithm
# 1) Initiate the result string as empty
# 2) Loop through items in the list.
#   -if item is the last item in the list, append it and return the
#   result string
#   -if item is the second last item, append it plus the delimiter
#   and the "end word" string (except if len(lst) == 2, in which case
#   skip the delimiter
#   -if item is not the second last or last item, append it plus the
#   delimiter string

# My solution
def join_or1(lst, delim=', ', end_word='or'):
    if len(lst) == 0:
        return ""
    if len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        return f"{str(lst[-2])} {end_word} {str(lst[-1])}"
    
    working_lst = []
    rev_lst = lst[::-1]
    for item in rev_lst:
        working_lst.append(str(item))
        working_lst.append(delim)
    working_lst.pop()
    working_lst.insert(1, (end_word + " "))
    working_lst.reverse()
    return "".join(working_lst)

# after reading LS documentation & writing my own version 
def join_or(lst, delim=', ', end_word='or'):
    match len(lst):
        case 0:
            return ""
        case 1:
            return str(lst[0])
        case 2:
            return f"{str(lst[0])} {end_word} {str(lst[1])}"
    
    leading_lst = [str(item) + delim for item in lst[0:-1]]
    return f"{"".join(leading_lst)}{end_word} {str(lst[-1])}"




## Examples / Test cases
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"