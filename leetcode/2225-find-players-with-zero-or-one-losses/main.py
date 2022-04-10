from collections import *

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    2577 ms, faster than 63.42%
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        pids = set()
        for winner, loser in matches:
            pids.add(winner)
            pids.add(loser)
        for p in pids:
            d[p] = [0, 0]  # win, lost
        for winner, loser in matches:
            d[winner][0] += 1
            d[loser][1] += 1
        zeroLost = []
        oneLost = []
        for p in pids:
            if d[p][1] == 0:
                zeroLost.append(p)
            elif d[p][1] == 1:
                oneLost.append(p)
        return [sorted(zeroLost), sorted(oneLost)]
