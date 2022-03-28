from heapq import *

"""
    1st: maxheap

    Time    O(NlogN)
    Space   O(N)
    1124 ms, faster than 60.00%
"""


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        maxheap = []
        for x in nums:
            heappush(maxheap, -x)
        count = 0
        total = sum(nums)
        cur_total = total
        while len(maxheap) > 0:
            pop = -heappop(maxheap)
            half = pop / 2.0
            cur_total -= half
            count += 1
            if cur_total <= total / 2.0:
                break
            heappush(maxheap, -half)
        return count
