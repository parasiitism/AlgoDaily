"""
    1st approach: hashset
    - get the numbers which are the power of x
    - get the numbers which are the power of y
    - put the number to the res set if x^i + y^j <= bound

    Time    O(logB/logX + logB/logY) where B, X, Y = bound, x, y 
    Space   O(logB/logX + logB/logY) the arrays which stores the powers
    16 ms, faster than 97.92%
"""


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """

        # get the numbers which are the power of x
        mx = []
        temp = 1
        while temp < bound:
            mx.append(temp)
            temp *= x
            if x == 1:
                break
        # get the numbers which are the power of y
        my = []
        temp = 1
        while temp < bound:
            my.append(temp)
            temp *= y
            if y == 1:
                break
        # put the number to the res set if x^i + y^j <= bound
        res = set()
        for a in mx:
            for b in my:
                temp = a + b
                if temp <= bound:
                    res.add(temp)
                else:
                    break
        return list(res)
