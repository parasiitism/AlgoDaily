from datetime import date

"""
    1st: use built-in method

    Time    O(N)
    Space   O(1)
    20 ms, faster than 45.35%
"""


class Solution(object):
    def daysBetweenDates(self, date1, date2):
        d0 = date(int(date1[:4]), int(date1[5:7]), int(date1[8:]))
        d1 = date(int(date2[:4]), int(date2[5:7]), int(date2[8::]))
        delta = d1 - d0
        return abs(delta.days)
