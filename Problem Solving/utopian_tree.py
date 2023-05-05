import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    h = 0
    for i in range(n+1):
        if i % 2 != 0:
            h *= 2
        else:
            h += 1
    return h