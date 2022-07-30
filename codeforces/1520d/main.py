from collections import *

"""
    Hashtable
    - transform the equation
        aj - ai = j - i
        i - ai = j - aj
    
    Time    O(N)
    Space   O(N)
"""


def f():
    n = int(input())
    for _ in range(n):
        _ = input()
        nums = [int(c) for c in input().split()]
        res = 0
        ctr = Counter()
        for i in range(len(nums)):
            diff = i - nums[i]
            if diff in ctr:
                res += ctr[diff]
            ctr[diff] += 1
        print(res)


f()
