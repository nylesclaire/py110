from datetime import date


def friday_the_13ths(given_year):
    running_total_13ths = 0
    for month in range(1,12):
        if date(given_year, month, 13).weekday() == 4:
            running_total_13ths +=1
    return running_total_13ths


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True