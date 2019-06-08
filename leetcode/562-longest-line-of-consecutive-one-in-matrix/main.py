"""
    1st approach: dfs
    - similar to lc490, 505
    - on each 1, explore 4 directions to see if we can form the longest consecutive ones
    - during exploration, cache each point with corresponding direction to avoid redundant calculation in the future

    Time    O(RC * max(R, C))
    Space   O(4RC)
    556 ms, faster than 38.99%
"""


class Solution(object):

    def __init__(self):
        self.res = 0
        self.seen = set()

    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    self.dfs(M, i, j)
        return self.res

    def dfs(self, M, x, y):
        dirs = [(1, -1), (0, 1), (1, 1), (1, 0)]
        count = 0
        # explore the directions
        for di, dj in dirs:
            # if we have explored this point with this direction, skip
            if (x, y, di, dj) in self.seen:
                continue
            # explore the matrix from this point in one direction
            i = x
            j = y
            count = 1
            while 0 <= i + di < len(M) and 0 <= j + dj < len(M[0]) and M[i+di][j+dj] == 1:
                i += di
                j += dj
                count += 1
                # ready to avoid redudant calculation
                self.seen.add((i, j, di, dj))
            # update the result if necessary
            self.res = max(self.res, count)


a = [
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
]
print(Solution().longestLine(a))

a = [
    [0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
]
print(Solution().longestLine(a))
