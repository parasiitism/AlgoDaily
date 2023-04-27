from collections import Counter
from heapq import *

"""
    1st: hashtable + minheap
    - calculate the occurance of every number
    - use minheap to remove the least appeared number until k = 0

    Time    O(NlogN)
    Space   O(N)
    1004 ms, faster than 33.33%
"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ctr = Counter(arr)
        pq = []
        for key in ctr:
            heappush(pq, (ctr[key], key))
        while len(pq) > 0:
            cnt, key = heappop(pq)
            if k >= cnt:
                ctr[key] = 0
                k -= cnt
            elif k > 0:
                ctr[key] -= k
                k = 0
            else:
                break
        res = 0
        for key in ctr:
            if ctr[key] > 0:
                res += 1
        return res
