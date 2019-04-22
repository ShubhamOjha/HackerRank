#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribe_counter = 0
    flag = True

    b = [ j for j in range(1,len(q)+1)]
    for i in range(len(q)):
        if q[i] != b[i]:
            if (b[i+1] == q[i]):
                temp1 = b[i]
                b[i] = b[i+1]
                b[i+1] = temp1
                bribe_counter += 1
            elif (b[i+2] == q[i]):
                temp1 = b[i]
                temp2 = b[i+1]
                b[i] = b[i+2]
                b[i+1] = temp1
                b[i+2] = temp2
                bribe_counter += 2
            else:
                print("Too chaotic")
                flag = False
                break
    if(flag):
        print(bribe_counter)

                


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
