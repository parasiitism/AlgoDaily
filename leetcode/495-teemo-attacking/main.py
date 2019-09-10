"""
    1st: merge interval

    Time O(n)
    Space O(n)
    244 ms, faster than 31.80%
"""


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0 or duration == 0:
            return 0
        intvs = [[timeSeries[0], timeSeries[0]+duration]]
        for i in range(1, len(timeSeries)):
            s = timeSeries[i]
            e = s + duration
            if intvs[-1][1] >= s:
                intvs[-1][1] = e
            else:
                intvs.append([s, e])
        res = 0
        for s, e in intvs:
            res += e-s
        return res
