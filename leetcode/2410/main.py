"""
    sort + 2 pointers

    Time    O(NlogN + MlogM + max(N, M))
    Space   O(1)
    2144 ms, faster than 14.29%
"""


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        res = 0
        for i in range(len(players)):
            p = players[i]
            while j < len(trainers) and p > trainers[j]:
                j += 1
            if j < len(trainers) and p <= trainers[j]:
                res += 1
                j += 1
        return res
