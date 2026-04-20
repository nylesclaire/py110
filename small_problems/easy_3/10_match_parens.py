### Problem
# input: string
# output: boolean
# rules:
#   - if there are no parentheses, it returns True
#   - pairs must occur in order: "(" and then ")"

### Data Structures
# strings
# maybe I convert to lists?

### Algorithm
# 1) iterate through the string and build a list of the parentheses chars
# 2) iterate through the list.
#   - for each ")":
#       -if there is a "(" in the slice of the list preceding:
#           - pop the first start and the first end Parens char in the list 
#           (use the index and pop methods)
#       -if not, return False
# 3) if the list is not empty, return False
# 4) else, return True

# WAit this sucks because it would mutate a list we're looping through. Dumb. 
# Let me think how to do this in a way that makes sense
# Okay this is going to be ugly af...

def is_balanced(given_str):
    working_list = [char for char in given_str if char in "()"]
    # print(f'Initial list- {working_list}')
    while working_list:
        for idx, item in enumerate(working_list):
            if item == "(" and ")" in working_list[(idx + 1):]:
                working_list.pop(working_list.index("("))
                working_list.pop(working_list.index(")"))
                # print(f"Popping- {working_list}")
                continue
            else: 
                # print(f"Other- {working_list}")
                return False
        return True
    return True

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True