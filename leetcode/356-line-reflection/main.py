"""
    1st approach: hastable + math
    - calculate the parallel line by averging min and max
    - for every point, find if there is a counter part on another side

    e.g.

    *   *   |   *   *   <- 2
        *   |           <- 1
    ------------------
    5   6   7   8   9

    the averge is 7
    for point [5, 2], counterpart = [2*7-5, 2] = [9, 2], which is on the plane
    for point [6, 2], counterpart = [2*7-6, 2] = [8, 2], which is on the plane
    for point [8, 2], counterpart = [2*7-8, 2] = [6, 2], which is on the plane
    for point [9, 2], counterpart = [2*7-9, 2] = [5, 2], which is on the plane
    for point [6, 1], counterpart = [2*7-6, 1] = [8, 1], which is NOT on the plane

    Time    O(n)
    Space   O(n)
    96 ms, faster than 71.43%
"""


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        ht = set()
        xMin = sys.maxsize
        xMax = -sys.maxsize
        for x, y in points:
            xMin = min(xMin, x)
            xMax = max(xMax, x)
            ht.add(x, y)
        avg2 = xMin + xMax
        for x, y in points:
            key = (avg2-x, y)
            if key not in ht:
                return False
        return True
