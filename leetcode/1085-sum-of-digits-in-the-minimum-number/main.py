import sys

"""
    1st
    - find the minimum number
    - sum the digits of that number

    Time    O(nm)
    Space   O(1)
    20 ms, faster than 78.37%
"""


class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        minNum = sys.maxsize
        for a in A:
            minNum = min(minNum, a)
        digitSum = 0
        while minNum > 0:
            temp = minNum % 10
            digitSum += temp
            minNum /= 10
        return 0 if digitSum % 2 == 1 else 1
