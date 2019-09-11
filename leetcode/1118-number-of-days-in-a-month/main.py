"""
    1st math:
    - Every year that is exactly divisible by four is a leap year, 
    except for years that are exactly divisible by 100, 
    but these centurial years are leap years if they are exactly divisible by 400. 
    
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are

    ref:
    https://en.wikipedia.org/wiki/Leap_year

    Time    O(1)
    Space   O(1)
    16 ms, faster than 62.98%
"""


class Solution(object):
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
