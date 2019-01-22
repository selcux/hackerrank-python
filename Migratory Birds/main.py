#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq = Counter(arr)
    reverse = [(y, x) for (x, y) in freq.items()]
    sorted_common = sorted(reverse, key=lambda tup: (-tup[0], tup[1]))
    (_, item) = sorted_common[0]
    return item

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
