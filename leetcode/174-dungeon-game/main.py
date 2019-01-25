import sys


class Solution(object):
    """
        1st approach
        - brute force dfs all the paths and find the least negative path sum
        Time    O(2^(m+n))
        Space   O(1)
    """

   def __init__(self):
        self.leastNegative = -sys.maxint-1

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        self.dfs(dungeon, 0, 0, 0)
        if self.leastNegative > 0:
            return 1
        return -self.leastNegative+1

    def dfs(self, dungeon, i, j, acc):
        if i < 0 or i >= len(dungeon) or j < 0 or j >= len(dungeon[0]):
            return
        temp = acc + dungeon[i][j]
        if i == len(dungeon) - 1 and j == len(dungeon[0])-1:
            print(temp)
            if temp < 0 and temp > self.leastNegative:
                self.leastNegative = temp

        self.dfs(dungeon, i+1, j, temp)
        self.dfs(dungeon, i, j+1, temp)


print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
