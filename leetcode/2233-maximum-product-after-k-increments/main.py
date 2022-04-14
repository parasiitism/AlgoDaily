from heapq import *

"""
    1st: min heap
    - incrementing a smaller number can maximize their product
        e.g. 2, 7
        3*7 = 21
        2*8 = 16
        ========
        e.g. 10, 144
        11, 144 = 1584
        10, 145 = 1450
    - so just keep incrementing the smallest number k times and take the product

    Time    O(NlogN)
    Space   O(N)
    1720 ms, faster than 20.00%
"""


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        minheap = nums[:]
        heapify(minheap)
        while k > 0:
            k -= 1
            smallest = heappop(minheap)
            smallest += 1
            heappush(minheap, smallest)
        res = 1
        for x in minheap:
            res *= x
            res %= 10**9 + 7
        return res
