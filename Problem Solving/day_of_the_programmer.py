#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here

    leap = f"12.09.{year}"
    non_leap = f"13.09.{year}"
    if year == 1918:
        return f"26.09.{year}"
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return leap
    else:
        return non_leap