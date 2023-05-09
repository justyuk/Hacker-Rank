import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    result = []
    for i in range(1, len(p)+1):
        result.append(p.index(p.index(i)+1 )+1)
    return result