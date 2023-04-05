from heapq import *

"""
    heap + hashtable

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def findScore(self, nums: List[int]) -> int:
        minheap = []
        n = len(nums)
        for i in range(n):
            heappush(minheap, (nums[i], i))
        removed = set()
        score = 0
        while len(minheap) > 0:
            x, i = heappop(minheap)
            if i in removed:
                continue
            score += x
            removed.add(i)
            removed.add(i-1)
            removed.add(i+1)
        return score
