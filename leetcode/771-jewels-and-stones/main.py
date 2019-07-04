"""
    1st approach: hashset

	Time		O(len(J)+len(S))
	Space		O(len(J))
	12 ms, faster than 96.71%
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        m = set()
        for c in J:
            m.add(c)
        res = 0
        for c in S:
            if c in m:
                res += 1
        return res
