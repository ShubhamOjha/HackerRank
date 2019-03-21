#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	c = 0
	lvl = 0
	for step in s:
		if step == 'U':
			lvl +=1
		elif step == 'D':
			lvl -=1

		if lvl ==0 & step == 'U':
			c += 1

	return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
