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
        dic = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday',
        }
        return dic[datetime.date(year, month, day).weekday()]
