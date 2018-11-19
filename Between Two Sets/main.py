#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    n = max(a)
    m = min(b)

    between = [x for x in range(n, m + 1)]

    filter_first = list()
    for elem in a:
        item = [x for x in between if x % elem == 0]
        filter_first.append(item)
    common_first = set(filter_first[0]).intersection(*filter_first)
    common_first = list(common_first)

    filter_second = []
    for elem in b:
        item = [x for x in common_first if elem % x == 0]
        filter_second.append(item)
    common_second = set(filter_second[0]).intersection(*filter_second)
    common_second = list(common_second)
    
    return len(common_second)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
