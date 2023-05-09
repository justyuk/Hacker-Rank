import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    l = len(arr)
    result = [n]
    while l != 0:
        m = min(arr)
        arr = [x - m for x in arr]
        arr = [x for x in arr if x != 0]
        if len(arr) == 0:
            break
        else:
            result.append(len(arr))
    return result