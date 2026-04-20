## Problem
# input: any integer (representing minutes)
# output: time of day in hh:mm format. (military time not am/ pm)
# rules:
#   - can't use datetime module
#   - negative number is minutes before midnight; positive is after
#   - ignore Daylight savings & other complications

## Data structures
# integers
# ???

## Algorithm
# 1) determine if "given minutes" is positive or negative or zero, branch here.
# 2) for zero minutes, return the right string
# 3) for positive numbers:
#       -floor divide by 60. If the dividend is < 24, assign this number to "hours"
#           -if the dividend is >= 24, modulo it by 24, and then assign that
#           number to "hours"
#       -modulo given minutes by 60 to get the remainder, assign this number 
#       to "minutes"
#       -return a string of hours : minutes
# 4) for negative numbers:
#       -floor divide by 60. If the dividend is < 24, subtract it from 23 and
#       assign this number to "hours"
#           -if the dividend is >= 24, modulo it by 24, and then subtract it 
#           from 23 and assign this number to "hours"
#       -modulo given minutes by 60 to get the remainder, subtract this from 60 
#       and assign this number to minutes
#       -return a string of hours : minutes


MIN_IN_HOUR = 60
HOURS_IN_DAY = 24

def pos_time_of_day(given_minutes):
    our_hours = given_minutes // MIN_IN_HOUR
    if our_hours >= HOURS_IN_DAY:
        our_hours = our_hours % HOURS_IN_DAY
    our_min = given_minutes % MIN_IN_HOUR
    return display_time(our_hours, our_min)

def neg_time_of_day(given_minutes):
    our_hours = given_minutes // MIN_IN_HOUR
    if our_hours >= HOURS_IN_DAY:
        our_hours = our_hours % HOURS_IN_DAY
    our_before_hours = (HOURS_IN_DAY - 1) - our_hours
    our_min = given_minutes % MIN_IN_HOUR
    our_before_min = MIN_IN_HOUR - our_min
    return display_time(our_before_hours, our_before_min)

def time_of_day(given_minutes):
    if given_minutes == 0:
        return "00:00"
    elif given_minutes > 0:
        return pos_time_of_day(given_minutes)
    return neg_time_of_day(abs(given_minutes))

def display_time(hours, min):
    return f"{hours:02}:{min:02}"



print(time_of_day(0) == "00:00")        # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(-1437) == "00:03")    # True