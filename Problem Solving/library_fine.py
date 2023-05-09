import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    hackos = 0
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return (m1-m2)*500
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return (d1-d2)*15
    else:
        return 0