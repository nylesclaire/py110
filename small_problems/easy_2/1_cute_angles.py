## Problem
# inputs: a float (between 0 and 360)
# outputs: a string representing the angle in degrees, minutes, & seconds
# rules: 
#    explicit: 
#       -use degree symbol, single quote for minutes, double quote for
#       seconds
#       -There are 60 min in a degree, 60 seconds in a minute


## data structures 
# a float, maybe ints at some point, and strings

## algorithm
#   1. Take original float and take all whole number digits and save as 
#   "degrees as int"
#   2. Take the decimal part of the o.g. float and multiply it by 60, save 
#   the result as a "minutes as float"
#   3. Take the whole number digits of "minutes as float" and save it as
#   "minutes as int" 
#   4. Take the decimal part of "minutes as float" and multiply it by .6,
#   then save the result as "seconds as float"
#   5. Take the whole number digits of "seconds as float" and save them as
#   "seconds as int"
#   6. Convert all the ints to strings, making sure the min and seconds ones
#   have two digits (so "2" should be "02")
#   6. Concatenate, format and return the full string with correct symbols.

DEGREE = "\u00B0"
NUM_OF_MIN_IN_DEGREE = 60
NUM_OF_SEC_IN_MINUTE = 60

def dms(given_float):
    degrees_as_int = int(given_float)
    minutes_as_float = (given_float - degrees_as_int) * NUM_OF_MIN_IN_DEGREE
    minutes_as_int = int(minutes_as_float)
    seconds_as_float = (minutes_as_float - minutes_as_int) * NUM_OF_SEC_IN_MINUTE
    seconds_as_int = int(seconds_as_float)

    degrees = str(degrees_as_int)
    minutes = str(minutes_as_int)
    if len(minutes) < 2: 
        minutes = "0" + minutes
    seconds = str(seconds_as_int)
    if len(seconds) < 2:
        seconds = "0" + seconds
    return degrees + DEGREE + minutes + "'" + seconds + '"'

# Test cases
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")