#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    b = s.split(' ')
    lst = []
    for i in range(len(b)):
        lst.append(b[i].capitalize())
        
    return ' '.join(lst) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
