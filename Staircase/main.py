#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
  for i in range(n):
    k = i + 1
    t = n - k
    print((' ' * t) + ('#' * k))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
