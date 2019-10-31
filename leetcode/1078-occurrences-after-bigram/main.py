"""
    1st: array iteration

    Time    O(n)
    Space   O(1)
    12 ms, faster than 89.96%
"""


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        strs = text.split()
        res = []
        for i in range(len(strs) - 2):
            if strs[i] == first and strs[i+1] == second:
                res.append(strs[i+2])
        return res
