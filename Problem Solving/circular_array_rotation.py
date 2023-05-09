import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    map = {}
    for i in range(n):
        map[(i + k) % n] = a[i]
    sort_map = sorted(map.keys())
    a = [map[key] for key in sort_map]
    result = []
    for q in queries:
        result.append(a[q])
    return result
