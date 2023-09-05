"""
    1st: math + sort
    - transform the time to hour * 60 + minute

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for t in timePoints:
            x = self.s2int(t)
            times.append(x)
            times.append(x+1440)
        times.sort()
        res = 24*60
        for i in range(1, len(times)):
            diff = times[i] - times[i-1]
            res = min(res, diff)
        return res

    def s2int(self, s):
        hh, mm = s.split(':')
        h, m = int(hh), int(mm)
        return h*60+m
