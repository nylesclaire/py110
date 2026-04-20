## Problem
# input: a time of day in 24 hr format (military time)
# output: -an integer between 0 and 1439 (inclusive) representing the minutes 
#           based on time after midnight
#          -an integer between 0 and 1439 (inclusive) representing the minutes
#           based on time before midnight 
# rules: -can't use datetime module
#       -all inputs will be in a string format of "hh:mm"

## Data Structures
# strings, integers, some constants based on minutes per hour and hours per day

## Algorithm
# For function 1 (minutes after midnight):
# 1) take the first two chars of the given string and convert to int. Assign
# to "hours"
# 2) take the last two chars of the given string and convert to int. Assign
# to "minutes"
# 3) multiply "hours" by "min_per_hour" and add that to "minutes"
# 4) return "minutes"

# For function 2 (minutes before midnight):
# 1) # 1) take the first two chars of the given string and convert to int. Assign
# to "hours"
# 2) take the last two chars of the given string and convert to int. Assign
# to "minutes"
# 3) subtract "hours" from "hours per day"
# 4) multiply "hours" by "min per hour" and subtract "minutes" from it, 
# reassign to "minutes". 
# 5) return "minutes"


MIN_PER_HOUR = 60
HOURS_PER_DAY = 24
MIN_PER_DAY = MIN_PER_HOUR * HOURS_PER_DAY

def after_midnight(time_24_str):
    hours, minutes = (int(time_24_str[0:2]), int(time_24_str[3:5]))
    result = (hours * MIN_PER_HOUR) + minutes
    if result > 1439:
        return 0
    return result

def before_midnight(time_24_str):
    hours, minutes = (int(time_24_str[0:2]), int(time_24_str[3:5]))
    result = ((HOURS_PER_DAY - hours) * MIN_PER_HOUR) - minutes
    if result > 1439:
        return 0
    return result

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
