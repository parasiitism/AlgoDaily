"""
    1st: greedy with prefix sum, a bit like dynamic programming
    - basically, any robot can only move down once
    - so robot1 just has to find the point to 'block' robot robot2 to get score    
    - idea.png

    Time    O(N)
    Space   O(1)
    1096 ms, faster than 100.00%
"""


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = 2**32
        topRightSum = sum(grid[0])
        bottomLeftSum = 0
        for i in range(n):
            topRightSum -= grid[0][i]
            res = min(res, max(topRightSum, bottomLeftSum))
            bottomLeftSum += grid[1][i]
        return res
