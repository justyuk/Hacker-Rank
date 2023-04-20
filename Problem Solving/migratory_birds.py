import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    map = {}
    for i in arr:
        if i not in map:
            map[i] = 0
        if i in map:
            map[i] +=1
        print(map)
    map_max = max(map.values())
    key_min = [key for key, value in map.items() if value == map_max]
    return min(key_min)