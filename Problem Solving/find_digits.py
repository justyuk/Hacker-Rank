import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    nums = [int(d) for d in str(n)]
    count = 0
    for i in nums:
        if i == 0:
            continue
        if n%i == 0:
            count += 1
    return count