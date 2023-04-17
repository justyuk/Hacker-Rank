import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        else:
            if grades[i] % 5 >=  3:
                grades[i] = 5 - (grades[i] % 5) + grades[i]
    return grades