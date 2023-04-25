
import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here

    s = sum(bill)
    if (s-bill[k])/2 == b:
        print("Bon Appetit")
    else:
        print(int(b - ((s-bill[k])/2)))