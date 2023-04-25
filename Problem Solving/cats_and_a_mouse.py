import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(z-x) == abs(z-y):
        return  "Mouse C"
    if abs(z-x) > abs(z-y):
        return "Cat B"
    else:
        return "Cat A"