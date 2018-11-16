#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
  arr.sort()
  length = len(arr)
  min = arr[:(length - 1)]
  max = arr[-(length - 1):]
  min_sum = sum(min)
  max_sum = sum(max)
  print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
