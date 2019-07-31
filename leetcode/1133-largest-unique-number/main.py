"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    36 ms, faster than 63.71%
"""


class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = {}
        for x in A:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        res = -1
        for key in m:
            if m[key] == 1:
                res = max(res, key)
        return res
