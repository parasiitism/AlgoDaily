from heapq import *

"""
    1st: sort + heap
    - we only need 2 non- overlaping intervals
    - sort the array to make sure that the time of the events move forward
    - use a minheap to keep the events
    - pop the minheap to find max left non-overlapping interval
    - the result must be one of the popped event + current event

    Time    O(NlogN)
    Space   O(N)
    1716 ms, faster than 7.69%
"""


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        res = 0
        max_left = 0
        minheap = []
        for s, e, v in events:
            heappush(minheap, (e, v))
            while len(minheap) and minheap[0][0] < s:
                _e, _v = heappop(minheap)
                max_left = max(max_left, _v)
            res = max(res, max_left + v)
        return res
