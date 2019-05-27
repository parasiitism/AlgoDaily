"""
    1st approach: just divide by 7

    Time    O(logn/log7)
    Space   O(logn/log7)
    20 ms, faster than 76.48%
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        isNegative = False
        if num < 0:
            isNegative = True
            num = -num
        res = ""
        while num > 0:
            res = str(num % 7) + res
            num /= 7
        if isNegative:
            res = '-' + res
        return res


"""
    2nd approach: just divide by 7, concise version

    Time    O(logn/log7)
    Space   O(logn/log7)
    Interviews
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        n, res = abs(num), ""
        while n > 0:
            res = str(n % 7) + res
            n /= 7
        if num < 0:
            res = '-' + res
        return res
