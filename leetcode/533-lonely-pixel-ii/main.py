"""
    1st approach: hashtable
    - the trickiest part is to understand Rule 2

    Rule 2 means
    - the rows(which has N 'B's in row and col) should have exactly the same appearence
    
    e.g.
    WBWBBW
    WBWBBW
    WBWBBW
    WWBWBW
    first 3 rows have the same appearence which is WBWBBW

    Time    O(2N)
    Space   O(N)
    448 ms, faster than 40.58%
"""


class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if len(picture) == 0 or len(picture[0]) == 0:
            return 0

        colsOfBs = len(picture[0]) * [0]
        # key: occurence
        # WBWBBW: 3
        m = {}
        for i in range(len(picture)):
            s = ""
            bCount = 0
            for j in range(len(picture[0])):
                s += picture[i][j]
                if picture[i][j] == 'B':
                    colsOfBs[j] += 1
                    bCount += 1
            # only if the count of 'B's == N we put the key(e.g.WBWBBW) into the hashtable
            if bCount == N:
                if s not in m:
                    m[s] = 1
                else:
                    m[s] += 1

        res = 0
        # for key each appears exactly N times
        for key in m:
            if m[key] == N:
                for i in range(len(key)):
                    # check if the col of current B has N of 'B's
                    if key[i] == 'B' and colsOfBs[i] == N:
                        res += N
        return res
