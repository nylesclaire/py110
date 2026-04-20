def repeater1(given_str):
    result = ""
    for char in given_str:
        result = result + (char * 2)
    return result

def repeater(given_str):
    return "".join([(char * 2) for char in given_str])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True