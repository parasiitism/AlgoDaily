from bisect import *


def f():
    N = int(input())
    nums = [int(s) for s in input().split()]
    nums.sort()
    q = int(input())
    res = []
    for _ in range(q):
        x = int(input())
        j = bisect_right(nums, x)
        res.append(j)
    for r in res:
        print(r)


f()
