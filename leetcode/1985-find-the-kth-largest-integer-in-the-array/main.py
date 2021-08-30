from heapq import *

"""
    1st: min heap
    - i love bigint in python

    Time    O(NlogK)
    Space   O(K)
    272 ms, faster than 100.00%
"""


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minheap = []
        for x in nums:
            num = int(x)
            heappush(minheap, num)
            if len(minheap) > k:
                heappop(minheap)
        return str(minheap[0])
