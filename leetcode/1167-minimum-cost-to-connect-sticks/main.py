import heapq

"""
    1st: heap

    Time    O(NlogN)
    Space   O(1)
    800 ms, faster than 82.10%
"""


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        pq = sticks
        heapq.heapify(pq)
        res = 0
        while len(pq) > 1:
            a = heapq.heappop(pq)
            b = heapq.heappop(pq)
            res += a + b
            heapq.heappush(pq, a + b)
        return res
