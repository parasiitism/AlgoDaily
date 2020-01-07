"""
    1st: dynamic programming
    - create auxillary horizontal and vertical arrays to record the consecutive ones
    - iterate the array from bottom right, try to find 4 sides which can form a square

    ref:
    - https://leetcode.com/problems/largest-1-bordered-square/discuss/345265/c%2B%2B-beats-100-(both-time-and-memory)-concise-with-algorithm-and-image

    Time    O(RC * min(R, C))
    Space   O(2RC)
    120 ms, faster than 100.00%
"""


class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        h = [c * [0] for _ in range(r)]
        v = [c * [0] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    h[i][j] = 1 if j == 0 else h[i][j-1] + 1
                    v[i][j] = 1 if i == 0 else v[i-1][j] + 1

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    # find s, the bottom line & the right line, h[i][j] and v[i][j]
                    s = min(h[i][j], v[i][j])
                    # see if the left line & the top line, v[i][j-s+1] and h[i-s+1][j]
                    while s > res:
                        if v[i][j-s+1] >= s and h[i-s+1][j] >= s:
                            res = max(res, s)
                            break
                        s -= 1
        return res*res
