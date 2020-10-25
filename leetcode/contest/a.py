#!/bin/python3

import re
import sys
import math
import random
import os


#
# implement method/function with name 'solve' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. p is of type INTEGER.
#  2. n is of type INTEGER.
#  3. k is of type INTEGER.
#  4. m is of type INTEGER.


def solve(p,n,k,m):
    # Write your code here
    if (n%m == 0 or m%n == 0) and p == k:
        return -1
    a = n
    b = m
    while a != b:
        if a < b:
            a += p
        else:
            b += k

    return a

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
#     fptr.write("\n")
#     p = int(input().strip())
#     n = int(input().strip())
#     k = int(input().strip())
#     m = int(input().strip())
#     outcome = solve(p, n, k, m)

#     fptr.write(str(outcome)  + '\n');

#     fptr.close()

