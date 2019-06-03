"""
    1st approach: finding rows pattern

    e.g.1
    000     110
    001 ->  111 <- all ones
    110     000 <- all zeros
            ^^
            flip columns

    e.g.2
    00111       11111 <- all ones
    11000       00000 <- all zeros
    10101  ->   01101
    10100       01100
    00111       11111 <- all ones
                ^^
                flip

    when we look closer, actually row0, row1 and row4 have the same pattern originally
    row0 = 00111
    row1 = 11000
    row4 = 00111

    so we can just flip the rows count the pattern occurrence instead of brainlessly flipping the columns

    ref:
    - https://www.youtube.com/watch?v=kvmnQKaZHXA
    - https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/discuss/304007/C%2B%2BChinesefind-the-same-pattern-between-the-rows

    Time    O(RC)
    Space   O(R) <- hashtable for rows patterns
    1540 ms, faster than 100.00%
"""


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = {}
        maxOccur = 0
        for arr in matrix:
            if arr[0] == 1:
                self.flipRows(arr)
            key = ','.join([str(x) for x in arr])
            if key not in m:
                m[key] = 1
            else:
                m[key] += 1
            maxOccur = max(maxOccur, m[key])
        return maxOccur

    def flipRows(self, arr):
        for i in range(len(arr)):
            arr[i] = 1-arr[i]
