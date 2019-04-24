#!/bin/python3
# Referal Question : https://www.hackerrank.com/challenges/minimum-swaps-2/problem

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    counter = 0
    length = len(arr)

    arr_dict = {}

    for i,item in enumerate(arr,1):
        arr_dict[item] = i
    checked = [False]*(length+1)

    for key,value in sorted(arr_dict.items(), key=lambda x: x[0]):
        if checked[key] or key == value:
            continue
        c_count = 0
        value = key
        while not checked[value]:

            checked[value] = True
            value = arr_dict[value]
            c_count +=1
        counter +=c_count - 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
