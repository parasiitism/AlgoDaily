
from heapq import *

"""
    maxheap

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-x for x in nums]
        heapify(nums)
        while k > 0:
            popped = -heappop(nums)
            res += popped
            heappush(nums, -math.ceil(popped/3.0))
            k -= 1
        return res
