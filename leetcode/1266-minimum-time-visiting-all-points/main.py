"""
    1st: math

    Time    O(N)
    Space   O(1)
    76 ms, faster than 11.34%
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            lastX, lastY = points[i-1]
            curX, curY = points[i]
            xDiff = abs(curX - lastX)
            yDiff = abs(curY - lastY)
            maxDiff = max(xDiff, yDiff)
            res += maxDiff
        return res
