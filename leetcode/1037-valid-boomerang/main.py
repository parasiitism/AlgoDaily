"""
    1st: math, hashset

    Time    O(1)
    Space   O(1)
    16 ms, faster than 81.87%
"""


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        hs = set()
        hs.add((x1, y1))
        hs.add((x2, y2))
        hs.add((x3, y3))
        if len(hs) < 3:
            return False

        slope1 = (y1 - y2) / ((x1 - x2) * 1.0) if x1 - x2 != 0 else 'inf'
        slope2 = (y1 - y3) / ((x1 - x3) * 1.0) if x1 - x3 != 0 else 'inf'
        return slope1 != slope2
