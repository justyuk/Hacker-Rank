import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0
    valleys = 0
    for i in path:
        if i == "D" and count == 0:
            valleys += 1
            count -= 1
        elif i == "D":
            count -=1
        elif i == "U":
            count += 1
    return valleys
            