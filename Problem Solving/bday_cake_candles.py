import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max = candles[0]
    count = 0
    for i in range(len(candles)):
        if candles[i] > max:
            max = candles[i]
        elif candles[i] == max:
            count += 1
    return count