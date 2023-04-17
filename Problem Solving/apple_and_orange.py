import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_Apples = 0
    count_Oranges = 0
    for i in range(len(apples)):
        if apples[i] + a >= s and apples[i] + a <= t:
            count_Apples += 1  
    for i in range(len(oranges)):
        if oranges[i] + b <= t and oranges[i] + b >= s:
            count_Oranges += 1
    print(count_Apples)
    print(count_Oranges)