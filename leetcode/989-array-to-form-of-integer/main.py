"""
    1st approach: basic addition with carry

    Time    O(m+n)
    Space   O(m+n)
    288 ms, faster than 62.65%
"""


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        B = []
        for c in str(K):
            B.append(int(c))
        res = []
        carry = 0
        while len(A) > 0 or len(B) > 0:
            a = 0
            if len(A) > 0:
                a = A.pop()
            b = 0
            if len(B) > 0:
                b = B.pop()
            temp = a + b + carry
            num = temp % 10
            carry = temp/10
            res.append(num)
        if carry > 0:
            res.append(carry)
        return res[::-1]
