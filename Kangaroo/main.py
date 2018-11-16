#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
        return "NO"

    max_iteration = 100000000000000
    d1 = x1
    d2 = x2
    sign = unit_value(x1, x2)
    i = 0
    
    while d1 != d2:
        i += 1
        d1 = x1 + v1 * i
        d2 = x2 + v2 * i
        
        if (d1 != d2 and (i >= max_iteration or sign != unit_value(d1, d2))):
            return "NO"

    return "YES"

def unit_value(n1, n2):
    return (n1 - n2) / abs(n1 - n2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
