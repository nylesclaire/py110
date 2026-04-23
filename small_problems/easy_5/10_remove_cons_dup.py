### Problem
# input: sequence of integers
# output: sequence of integers w/ order maintained, and consecutive 
# duplicates removed


### Algorithm
# 1) loop through the numbers, and retain the ones whose value is not
# equal to the number preceeding.

def unique_sequence1(seq):
    return [seq[idx] for idx in range(len(seq)) 
                     if seq[idx] != seq[idx - 1]]

def unique_sequence(seq):
    return [value for idx, value in enumerate(seq) 
                  if idx == 0 or value != seq[idx - 1]]

### Test cases
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True