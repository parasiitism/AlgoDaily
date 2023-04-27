from heapq import *

"""
    2nd: learned from others
    1. loop over 10^5 days
    2. on each day
        - pop the events that end before today
        - push the events that start from today
        - then greedily attend the event that ends soonest, res += 1

    ref:
    - https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510263/JavaC%2B%2BPython-Priority-Queue
    - https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510262/Detailed-analysisLet-me-lead-you-to-the-solution-step-by-step

    Time    O(10^5 x logN)
    Space   O(N)
    1900 ms, faster than 45.54%
"""


class Solution(object):
    def maxEvents(self, events):
        events.sort(key=lambda x: x[0])
        n = len(events)
        pq = []
        i = 0
        res = 0
        for d in range(1, 100001):
            while len(pq) > 0 and pq[0] < d:
                heappop(pq)
            while i < n and events[i][0] == d:
                heappush(pq, events[i][1])
                i += 1
            if len(pq) > 0:
                heappop(pq)
                res += 1
        return res
