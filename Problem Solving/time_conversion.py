import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s.split(":")
    if s[-2:] == "PM":
        if hour[0] != "12":
            print(hour[0])
            hour[0] = str(int(hour[0])+12)
    else:
        if hour[0] == "12":
            hour[0] = "00"
    time = ':'.join(hour)
    return str(time[:-2])
