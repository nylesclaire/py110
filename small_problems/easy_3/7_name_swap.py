def swap_name1(first_last):
    return  ", ".join(first_last.split()[::-1])

# further exploration
def swap_name(first_mid_last):
    name_list = first_mid_last.split()
    return f"{name_list[-1]}, {" ".join(name_list[0:-1])}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True]
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True