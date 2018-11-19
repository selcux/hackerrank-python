#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
  minn = maxx = scores[0]
  change_max_count = 0
  change_min_count = 0

  for k in scores:
    if max(maxx, k) > maxx:
      maxx = k
      change_max_count += 1
    if min(minn, k) < minn:
      minn = k
      change_min_count += 1

  return [change_max_count, change_min_count]

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input())

  scores = list(map(int, input().rstrip().split()))

  result = breakingRecords(scores)

  fptr.write(' '.join(map(str, result)))
  fptr.write('\n')

  fptr.close()
