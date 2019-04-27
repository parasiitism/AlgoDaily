"""
    2nd approach: calculate 'B's on each row and each col
    1. for row, if there are 'B', calculate the number of 'B' for those columns
    2. if that row only has 1 'B', check if there is only one 'B' on that column
    3. be careful of 'one column checking'

    Time		O(m*n)
    Space		O(n)
    456 ms, faster than 22.22%
"""


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if len(picture) == 0 or len(picture[0]) == 0:
            return 0

        rowsOfBs = len(picture) * [0]
        colsOfBs = len(picture[0]) * [0]

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rowsOfBs[i] += 1
                    colsOfBs[j] += 1

        res = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and rowsOfBs[i] == 1 and colsOfBs[j] == 1:
                    res += 1

        return res
