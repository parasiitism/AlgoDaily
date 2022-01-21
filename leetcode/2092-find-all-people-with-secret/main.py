from collections import *
from heapq import *

"""
    1st: BFS + heap + binary search
    - the minheap is important, it makes sure that the order of "telling secret" is ascending

    Time    O(E * (logE + logV))
    Space   O(E)
    4511 ms, faster than 8.20%
"""


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # create a graph
        g = {}
        for i in range(n):
            g[i] = []
        for u, v, t in meetings:
            g[u].append([v, t])
            g[v].append([u, t])
        # sort the connected people by meeting's time
        for i in range(n):
            g[i].sort(key=lambda x: (x[1], x[0]))
        # put all the people who have meeting(s) with person0 into a minheap (ordered by meeting's time)
        res = set([0])
        minheap = []
        heappush(minheap, (0, firstPerson))
        for v, t in g[0]:
            heappush(minheap, (t, v))
        # important: BFS + minheap ordered by time
        while len(minheap) > 0:
            t, v = heappop(minheap)
            if v in res:
                continue
            res.add(v)
            # important: just put the meetings into the minheap if and only if its meeting's time >= current time
            bIdx = self.lowerBsearch(g[v], t)
            for i in range(bIdx, len(g[v])):
                _v, _t = g[v][i]
                heappush(minheap, (_t, _v))
        return res

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][1]:
                right = mid
            else:
                left = mid + 1
        return left
