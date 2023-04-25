#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if n % 2 == 0:
        n += 1
    front = math.ceil((p-1)/2)
    back = math.floor((n-p)/2)
    print(front, back)
    if front < back:
        return front
    else:
        return back