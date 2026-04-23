
# using the original attempted loop
def reverse_string1(string):
    length = len(string)
    for char in string:
        string = char + string
    string = string[:length]

    return string

# using a cleaner syntax
def reverse_string(string):
    return string[::-1]

print(reverse_string("hello") == "olleh")