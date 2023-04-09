from heapq import *

"""
    minheap
    - my 1st attempt was just iterate linearly and remove the nums[i] if prefix_sum < 0, however this is not correct when we consider
    and example [6,-6,-3,3,1,5], actually what we want to remove is the -6 at index1
    - so the best approach is to use a minheap:
        - just add every number to prefix_sum
        - while the prefix_sum < 0, remove the most negatove number(s) until prefix_sum >= 0

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        n = len(nums)
        minheap = []
        pfs = 0
        res = 0
        for i in range(n):
            x = nums[i]
            pfs += x
            heappush(minheap, x)
            while pfs < 0 and len(minheap) > 0:
                most_negative = heappop(minheap)
                pfs -= most_negative
                res += 1
        return res
