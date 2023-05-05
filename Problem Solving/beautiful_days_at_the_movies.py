import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    
    count = 0
    for day in range(i,j+1):
        reversed_num = int(str(day)[::-1])
        if abs(day - reversed_num)%k == 0:
            count += 1
    return count
