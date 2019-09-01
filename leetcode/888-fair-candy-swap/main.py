"""
    1st: hashtable

    Time    O(n)
    Space   O(n)
    324 ms, faster than 96.56%
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a = sum(A)
        b = sum(B)
        avg = (a + b)//2
        diff = avg - a

        setA = set(A)
        for x in B:
            if x-diff in setA:
                return [x-diff, x]
        return []
