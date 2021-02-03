from heapq import *

"""
    1st: heap
    - similar to lc630, 857
    - sort the engineers by efficiency
    - when it iterate thru
        - maintain the top K fastest engineers
        - calculate the total performance(speed * efficiency = product)
    
    ref:
    - https://leetcode.com/problems/maximum-performance-of-a-team/discuss/539687/JavaC%2B%2BPython-Priority-Queue

    Time    O(NlogN + NlogK)
    Space   O(N)
    596 ms, faster than 10.47%
"""


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minheap = []
        res = 0
        speedSum = 0
        A = []
        for i in range(n):
            A.append((efficiency[i], speed[i]))
        A.sort(reverse=1)
        for e, s in A:
            heappush(minheap, s)
            speedSum += s
            if len(minheap) > k:
                speedSum -= heappop(minheap)
            res = max(res, speedSum * e)
        return res % (10**9 + 7)
