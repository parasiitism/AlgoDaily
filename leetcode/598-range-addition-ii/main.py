"""
    1st approach: row * col
    - since the addition must start from 0 in rither rows or cols, we can just use 2 arrays to record head of the rows and the first row
    - then we can multiply maxRowCount and the maxColCount

    e.g.

    3 3 1 0
    3 3 1 0
    3 3 1 0
    2 2 1 0

    maxRowCount = 3
    maxColCount = 2
    maxRowCount * maxColCount = 6

    Time    O(O * (R+C) + R + C)
    Space   O(R + C)
    740 ms, faster than 11.23%
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        rows = m * [0]
        cols = n * [0]
        for a, b in ops:
            for i in range(len(rows)):
                if i < a:
                    rows[i] += 1
            for i in range(len(cols)):
                if i < b:
                    cols[i] += 1
        maxRow = 0
        maxRowCount = 0
        for i in range(len(rows)):
            if rows[i] > maxRow:
                maxRow = rows[i]
                maxRowCount = 1
            elif rows[i] == maxRow:
                maxRowCount += 1
        maxCol = 0
        maxColCount = 0
        for i in range(len(cols)):
            if cols[i] > maxCol:
                maxCol = cols[i]
                maxColCount = 1
            elif cols[i] == maxCol:
                maxColCount += 1
        return maxRowCount * maxColCount


"""
    2nd approach: use min

    learned from others
    - https://leetcode.com/problems/range-addition-ii/solution/

    Time    O(O)
    Space   O(R + C)
    44 ms, faster than 64.93%
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for a, b in ops:
            m = min(m, a)
            n = min(n, b)
        return m * n
