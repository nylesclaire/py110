def is_consonant(char):
    if char.lower() in "bcdfghjklmnpqrstvwxyz":
        return True

def double_consonants(given_str):
    result_str = ""
    for char in given_str:
        if is_consonant(char):
            result_str += (char * 2)
        else:
            result_str += char
    return result_str

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")