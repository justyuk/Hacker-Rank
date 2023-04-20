import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min = scores[0]
    max = scores[0]
    min_count = 0
    max_count = 0
    for i in range(1,len(scores)):
        if scores[i] == min or scores[i] == max:
            pass
        if scores[i] < min:
            min_count += 1
            min = scores[i]
        if scores[i] > max:
            max_count += 1
            max = scores[i]
    return max_count,min_count