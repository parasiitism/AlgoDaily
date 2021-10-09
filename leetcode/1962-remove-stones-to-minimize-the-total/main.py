from heapq import *

"""
    1st: maxheap
    - since we remove x//2 for every number, the most aggresive way is to use a maxheap to halve the largest number K times

    Time    O(NlogN)
    Space   O(N)
    1888 ms, faster than 28.57% 
"""


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap = []
        for p in piles:
            heappush(maxheap, -p)
        while len(maxheap) > 0 and k > 0:
            x = -heappop(maxheap)
            x = (x+1)//2
            if x > 0:
                heappush(maxheap, -x)
            k -= 1
        return -sum(maxheap)
