from heapq import *

"""
    1st: 2 heaps

    Time    O(NlogN)
    Space   O(N)
    696 ms, faster than 81.10%
"""


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        res = None

        mapping = []
        for i in range(len(times)):
            s, e = times[i]
            mapping.append([s, e, i])
        mapping.sort()

        occupieds = []  # (t, cIdx)
        unoccupieds = []  # (cIdx)

        chairIdx = 0
        for i in range(len(mapping)):
            s, e, userIdx = mapping[i]

            while len(occupieds) > 0 and occupieds[0][0] <= s:
                popTime, popChairIdx = heappop(occupieds)
                heappush(unoccupieds, popChairIdx)

            currentChair = None
            if len(unoccupieds) > 0:
                popChairIdx = heappop(unoccupieds)
                currentChair = popChairIdx
            else:
                currentChair = chairIdx
                chairIdx += 1

            heappush(occupieds, (e, currentChair))
            if userIdx == targetFriend:
                res = currentChair
                break
        return res
