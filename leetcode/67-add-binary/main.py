"""
    1st approach: stack + carry
	- each digit = byteA + byteB + carry
	- add the digits until no more carry, a, b

    Time    O(A+B + max(A, B))
    Space   O(A+B)
    32 ms, faster than 39.01%
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        stackA = [int(x) for x in a]
        stackB = [int(x) for x in b]
        carry = 0
        res = ""
        while len(stackA) or len(stackB):
            x = 0
            if len(stackA) > 0:
                x = stackA.pop()
            y = 0
            if len(stackB) > 0:
                y = stackB.pop()
            temp = x + y + carry
            num = temp % 2
            carry = temp/2
            res = str(num) + res
        if carry == 1:
            res = '1' + res
        return res
