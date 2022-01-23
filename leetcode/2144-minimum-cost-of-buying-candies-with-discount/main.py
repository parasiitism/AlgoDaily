"""
    1st: sort
    - skip every 3rd element, accumulate the rest
        0 1 2 3 4 5 6 7
            ^     ^

    Time    O(NlogN)
    Space   O(1)
    76 ms, faster than 57.14%
"""


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(key=lambda x: -x)
        res = 0
        for i in range(len(cost)):
            if (i+1) % 3 == 0:
                continue
            res += cost[i]
        return res
