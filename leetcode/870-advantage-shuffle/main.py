"""
    1st: sorting

    Time    O(nlogn)
    Space   O(n)
    428 ms, faster than 25.82%
"""


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b = []
        for i in range(len(B)):
            b.append((B[i], i))
        a = sorted(A, reverse=True)
        b = sorted(b, reverse=True)
        res = len(A) * [-1]
        unused = []
        for i in range(len(b)):
            val, pos = b[i]
            if len(a) > 0 and a[0] > val:
                res[pos] = a.pop(0)
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = a.pop(0)
        return res
