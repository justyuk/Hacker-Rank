import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    map = {}
    min = a[-1]
    max = b[0]
    for i in range(min,max+1):
        if max % i == 0:
            map[i] = 0
    join = a+b
    count = 0
    print(join,"this is join")
    for i in map:
        for j in join:
            print(j)
            if j%i == 0 or i%j==0:
                map[i] +=1
        if map[i] == len(join):
            count +=1
    return count