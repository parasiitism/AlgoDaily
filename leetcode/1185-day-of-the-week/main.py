import datetime

"""
    1st: built-in library

    Time    O(1)
    Space   O(1)
    12 ms, faster than 89.81%
"""


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        dic = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
        ]
        return dic[datetime.date(year, month, day).weekday()]


"""
    2nd: math
    - 1971 Jan 1st is Friday

    Time    O(n) total number of days from 1971 to the input date
    Space   O(n)
    20 ms, faster than 36.53%
"""


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        total = 0
        for i in range(1971, year):
            if self.ifLeapyear(i):
                total += 366
            else:
                total += 365
        for i in range(1, month):
            total += self.numberOfDays(year, i)
        total += day - 1
        dic = ['Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday', 'Saturday', 'Sunday']
        return dic[(total + 4) % 7]

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


s = Solution()
a = 1
b = 1
c = 1981
print(s.dayOfTheWeek(a, b, c))
