"""
    1st: sort

    Time    O(NlogN)
    Space   O(N)
    1068 ms, faster than 50.00%
"""


from heapq import *


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diffs = []
        for i in range(n):
            d = capacity[i] - rocks[i]
            diffs.append(d)
        diffs.sort()
        res = 0
        for i in range(n):
            d = diffs[i]
            if additionalRocks - d < 0:
                break
            additionalRocks -= d
            res += 1
        return res


"""
    2nd: min heap

    Time    O(NlogN)
    Space   O(N)
    1068 ms, faster than 50.00%
"""


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diffs = []
        for i in range(n):
            d = capacity[i] - rocks[i]
            diffs.append(d)
        heapify(diffs)
        res = 0
        while len(diffs) > 0:
            d = heappop(diffs)
            if additionalRocks - d < 0:
                break
            additionalRocks -= d
            res += 1
        return res
