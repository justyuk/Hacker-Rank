
import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    ar = math.ceil(math.sqrt(a))
    br = math.ceil(math.sqrt(b))
    count = 0
    for i in range(ar,br+1):
        print(i)
        if i**2 <= b and i**2 >=a:
            count += 1
    return count