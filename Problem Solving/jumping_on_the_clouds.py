import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    while True:
        energy = energy - c[i] * 2 -1
        i = (i+k) % n
        if i == 0:
            return energy