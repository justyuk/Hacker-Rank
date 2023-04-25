import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    max = 0
    for i in keyboards:
        for j in drives:
            if i+j <= b and i+j > max:
                max  = i+j
    if max == 0:
        return -1
    else:
        return max