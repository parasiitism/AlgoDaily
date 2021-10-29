"""
    minheap to get the k-th largeest number

    Time    O(NlogK)    92 ms
    Space   O(K)        4400 KB
"""
from heapq import *


def f():
    _, k = map(int, input().split())
    nums = [int(s) for s in input().split(" ")]
    minheap = []
    for x in nums:
        if x <= 0:
            continue
        heappush(minheap, x)
        if len(minheap) > k:
            heappop(minheap)
    if len(minheap) == 0:
        return 0
    threshold = minheap[0]
    res = 0
    for x in nums:
        if x >= threshold:
            res += 1
    return res


print(f())
