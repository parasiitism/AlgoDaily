from collections import *


def f():
    n = int(input())
    nums = [int(c) for c in input().split()]
    res = 0
    total = sum(nums)
    ctr = Counter()
    pfs = 0
    for i in range(n):
        x = nums[i]
        pfs += x
        if 1 <= i < n - 1:
            if pfs * 3 == total * 2 and (pfs // 2) * 2 == pfs:
                res += ctr[pfs//2]
        ctr[pfs] += 1
    print(res)


f()
