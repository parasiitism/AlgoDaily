"""
    1st: math

    Time    O(12)
    Space   O(1)
    20 ms, faster than 39.89%
"""


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        parts = date.split('-')
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])

        res = 0
        for i in range(1, m):
            res += self.numberOfDays(y, i)
        res += d

        return res

    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        if M in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if M != 2:
            return 30
        return 29 if self.ifLeapyear(Y) else 28

    def ifLeapyear(self, Y):
        if Y % 4 == 0:
            if Y % 100 == 0:
                if Y % 400 == 0:
                    return True
                return False
            return True
        return False
