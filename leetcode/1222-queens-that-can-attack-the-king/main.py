"""
    1st: hashtable
    - put all the queens in a hashset
    - search for the nearest queen in 8 directions

    Time    O(Q + 8*8)
    Space   O(Q + 8)
    24 ms, faster than 78.95%
"""


class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queensMap = set()
        for i, j in queens:
            queensMap.add((i, j))
        res = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for di, dj in directions:
            i = king[0] + di
            j = king[1] + dj
            while i >= 0 and i < 8 and j >= 0 and j < 8:
                if (i, j) in queensMap:
                    res.append((i, j))
                    break
                i += di
                j += dj
        return res
