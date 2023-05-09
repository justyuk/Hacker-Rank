import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    count = 0
    for i,j in zip(s,t):
        if i == j:
            count += 1
        else: break
    total_length = len(s+t)
    if total_length - 2*count <= k and (total_length-count*2)%2 == k%2 or total_length <= k:
        return "Yes"
    else:
        return "No"