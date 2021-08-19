
from heapq import *

"""
    1st: heap
    - we can fullfill the requirement by rearranging the array in a ZigZag way
        so that for every number, its neighbours must be larger or smaller than itself
    - it works becos all the numbers are distinct
    - e.g. [1, 2, 3, 4, 5, 6]

    [1, 6, 2, 5, 3, 4]
     _  ^ _ ^ _  ^  _

    Time    O(NlogN)
    Space   O(N)
    1744 ms, faster than 25.00%
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        halfIdx = len(nums) // 2
        minheap = nums[:halfIdx]
        maxheap = [-x for x in nums[halfIdx:]]
        heapify(minheap)
        heapify(maxheap)
        res = []
        while len(minheap) > 0 or len(maxheap) > 0:
            if len(minheap) > 0:
                res.append(heappop(minheap))
            if len(maxheap) > 0:
                res.append(-heappop(maxheap))
        return res
