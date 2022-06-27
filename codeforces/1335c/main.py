from collections import *

"""
    hashtable

    Time    O(N)
    Space   O(N)
"""


def f():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = [int(x) for x in input().split()]
        print(solve(nums))


def solve(nums):
    ctr = Counter()
    max_count = 0
    for x in nums:
        ctr[x] += 1
        if ctr[x] > max_count:
            max_count = ctr[x]
    key_count = len(ctr.keys())
    if key_count > max_count:
        return max_count
    elif key_count == max_count:
        return max_count - 1
    return min(max_count-1, key_count)


f()
