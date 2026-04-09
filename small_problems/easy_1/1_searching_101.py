list_1st_5 = []

for indx in range(0,5):
    list_1st_5.append(input(f"Enter number {indx + 1}: "))

last_num = input("Enter the last number: ")
str_list_1st_5 = ','.join(list_1st_5)

if last_num in list_1st_5:
    print(f"{last_num} is in {str_list_1st_5}")
else:
    print(f"{last_num} isn't in {str_list_1st_5}")