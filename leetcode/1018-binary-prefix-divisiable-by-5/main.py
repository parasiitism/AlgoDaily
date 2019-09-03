"""
    1st: brute force

    problem: if len(A) is too big, the integer will be out of bound

    Time    O(n)
    Space   O(n)
    308 ms, faster than 42.13%
"""


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        num = 0
        for x in A:
            num = num*2 + x
            res.append(num % 5 == 0)
        return res
