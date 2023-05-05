import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared = 5
    const = 2
    liked = 0
    count = 0
    for i in range(n):
        liked = shared//const
        count += liked
        shared = liked*3
    return count
        