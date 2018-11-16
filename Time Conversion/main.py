#!/bin/python3

import os
import sys
import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    tm = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return tm.strftime("%H:%M:%S")

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
