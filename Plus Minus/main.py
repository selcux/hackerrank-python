#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  positives = len([x for x in arr if x > 0])
  negatives = len([x for x in arr if x < 0])
  zeros = len([x for x in arr if x == 0])
  total = len(arr)

  positive_rate = round(positives / total, 6)
  negative_rate = round(negatives / total, 6)
  zero_rate = round(zeros / total, 6)
  
  print(str.format('{0:.6f}', positive_rate))
  print(str.format('{0:.6f}', negative_rate))
  print(str.format('{0:.6f}', zero_rate))

if __name__ == '__main__':
  n = int(input())

  arr = list(map(int, input().rstrip().split()))

  plusMinus(arr)
