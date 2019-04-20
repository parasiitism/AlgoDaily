"""
    1st approach: sort
    1. sort the intervals by start time
    2. iterate the intervals and compare the cur interval start time with the last interval end time

    Time    O(nlogn)
    Space   O(n)
    88 ms, faster than 24.16%
    20apr2019
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        for itv in intervals:
            if itv[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], itv[1])
            else:
                merged.append(itv)
        return merged


a = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(a))
