#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    diff = [5 - (x % 5) if x >= 38 else 0 for x in grades]
    delta = [x if x < 3 else 0 for x in diff]
    rounded = [sum(x) for x in zip(grades, delta)]
    return rounded

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
