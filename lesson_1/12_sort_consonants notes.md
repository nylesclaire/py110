## Understanding the Problem

- input: list containing strings 
- output: new sorted list of strings (I believe; see questions)

# rules
- explicit:
  - strings with the same number of adjacent consonants are to be included in their original order
  - consonants are considered adjacent if they are next to each other in the same word, or if there is a space between two consonants in adjacent words. 
- implicit: 
  - can't think of any.

# Questions: 
  - Is "y" considered a vowel or a consonant? **
  - Do I want to return the same list object or a new one? **
  - What should be the expected return value for an empty list? **
  - Does anything need to be case-sensitive?
  - Do we sort in order from highest # of adjacent consonants or lowest?

## Examples & Test cases

# more rules determined after test cases
- Sort in descending order of adjacent consonants
- You can never have a number of adjacent consonants equal to 1; if a string's consonants are not adjacent, the number is 0.

# from the discussion...
- Let's assume strings cannot be empty
- Let's assume we don't need to worry about case

# additional assumptions from me since I can't ask for clarification
- Let's call "y" a consonant. 
- Let's return a new list object. 
- Let's assume the original list will have at least one string.



## Data Structures
- We're given a list of strings. 
- We need to output another list of strings. 
- We may want to associate each string with the number of adjacent consonants within it, which could be done with additional lists, or tuples, or dictionaries, perhaps... TBD
- We need to maintain order, so we need to stick to sequences and iterables, not sets.

## Algorithm

# first draft - high level
- 1. Begin looping through input list. For the current string in our input list, calculate the number of adjacent consonants. (Will break this down later- helper function.)
- 2. For that number of adjacent consonants, create an associated sublist and add the first string as the first element of the list. 
- 3. Repeat until all strings in the list have been added to a list associated with the number of adjacent consonants in them. Ensure strings being added to an existing sublist are appended to the *end* of the list.
- 4. Concatenate or join the sublists in descending order. 
- 5. Return the resulting new list. 

# first draft - helper function
- Notes first
  - input: a non-empty string
  - output: the number of adjacent consonants 
  - rules (repeated from above):
    - You can never have a number of adjacent consonants equal to 1; if a string's consonants are not adjacent, the number is 0.
    - consonants are considered adjacent if they are next to each other in the same word, or if there is a space between two consonants in adjacent words. 
    - "y" is a consonant.
    - we don't need to worry about case

- 1. Set "adjacent consonents substring" to an empty string, and "list of substrings" as an empty list.
- 2. Begin iterating through each character in the string. With the current character:
  - If it is a consonant, append that consonant to the "new substring", then iterate to next character
  - If it is a whitespace character, ignore it and iterate to next character
  - If it is a vowel:
    - append "adjacent consonents substring" to "list of substrings"
    - then set "adjacent consonents substring" back to an empty string
    - iterate to the next character
- 3. When you're done iterating, you should have your complete "list of substrings" that includes all runs of adjacent consonants. Find the item in this list that has the maximum length; return that length, unless it is 1, in which case, return 0. 

- Another idea: use str.split() method w/ vowels as delimiters? Same concept really.