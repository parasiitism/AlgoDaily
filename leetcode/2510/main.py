"""
    recursion: backtracking

    Time    O(2^N) -> O(N!)3399 ms
    Space   O(RC)
"""


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        if R % 2 == 1 and C % 2 == 1:
            return False
        if R % 2 == 0 and C % 2 == 0:
            return False

        def dfs(i, j, zeros, ones):
            if i < 0 or i > R-1 or j < 0 or j > C-1:
                return False
            if grid[i][j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros > (R+C)//2 or ones > (R+C)//2:
                return False
            if i == R-1 and j == C-1:
                return zeros == ones
            if dfs(i+1, j, zeros, ones) == True:
                return True
            if dfs(i, j+1, zeros, ones) == True:
                return True
            return False

        return dfs(0, 0, 0, 0)
