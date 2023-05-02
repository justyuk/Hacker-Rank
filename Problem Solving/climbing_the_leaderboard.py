import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # removing recuring numbers in ranked list
    ranked = list(set(ranked))
    # sort scores in ascending order
    ranked = sorted(ranked)
    results = []
    i = 0
    l = len(ranked)
    
    for score in player:
        while i < l and ranked[i] <= score:
               i+=1
        results.append(l-i+1)
    return results