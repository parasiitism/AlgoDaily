"""
    1st: math + sort
    - transform the time to hour * 60 + minute

    Time    O(NlogN)
    Space   O(N)
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for s in timePoints:
            hh, mm = s.split(":")
            hh = int(hh)
            mm = int(mm)
            times.append((hh*60 + mm))
        times.sort()
        if len(times) > 1:
            first = times[0]
            times.append(first + 60*24)
        res = 60*24
        for i in range(1, len(times)):
            res = min(res, times[i] - times[i-1])
        return res