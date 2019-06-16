"""
    1st approach: dfs + hashtable
    - dfs to search the increasing path and increment path length recursive from bottom
    - since we increment the path length from bottom, we can cache the path length for (i, j, direction) to avoid redundant calculation in the future

    e.g.
    [200, 100, 50, 5, 6]
    [1,     2,  3, 4, 7]
    [50, 50, 50, 100, 8]
    [50, 50, 50, 100, 9]

    Lets say we already have [5,6,7,8,9] after we reverse the first row,
    on the 2nd row, we want to include [1,2,3,4] to the [5,6,7,8,9].
    
    If we already have (i=0, j=3, dir=right) = 5, we use it to increment the path length when we are at (1, 3) = 4 going upward

    Time    O(RC) every cell will be visited once
    Space   O(4RC) 4 directions on each cell
    1072 ms, faster than 5.00%
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        seen = {}
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                steps = self.search(matrix, i, j, seen)
                res = max(res, steps)
        return res

    def search(self, matrix, i, j, seen):
        up = self.dfs(matrix, i-1, j, 0, matrix[i][j], seen)
        down = self.dfs(matrix, i+1, j, 1, matrix[i][j], seen)
        left = self.dfs(matrix, i, j-1, 2, matrix[i][j], seen)
        right = self.dfs(matrix, i, j+1, 3, matrix[i][j], seen)
        steps = max(up, down, left, right) + 1
        return steps

    def dfs(self, matrix, i, j, d, last, seen):
        if i < 0 or i+1 > len(matrix) or j < 0 or j+1 > len(matrix[0]):
            return 0
        if matrix[i][j] <= last:
            return 0
        key = (i, j, d)
        if key in seen:
            return seen[key]
        up = self.dfs(matrix, i-1, j, 0, matrix[i][j], seen)
        down = self.dfs(matrix, i+1, j, 1, matrix[i][j], seen)
        left = self.dfs(matrix, i, j-1, 2, matrix[i][j], seen)
        right = self.dfs(matrix, i, j+1, 3, matrix[i][j], seen)
        steps = max(up, down, left, right) + 1
        seen[key] = steps
        return steps
