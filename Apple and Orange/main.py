#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
  apples_absolute_pos = [a + x for x in apples]
  oranges_absolute_pos = [b + x for x in oranges]
  apples_in_the_house = [x for x in apples_absolute_pos if x >= s and x <= t]
  oranges_in_the_house = [x for x in oranges_absolute_pos if x >= s and x <= t]
  print(len(apples_in_the_house))
  print(len(oranges_in_the_house))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
