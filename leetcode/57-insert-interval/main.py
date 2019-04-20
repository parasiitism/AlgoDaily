"""
    1st approach: binary search + merge intervals
    1. upper bound binary search the intervals to insert the new interval
    2. merge the intervals

    Time    O(logn + n) => O(n)
    Space   O(n) result
    64 ms, faster than 31.56%
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        if newInterval == None or len(newInterval) == 0:
            return intervals
        # insert the new interval into the right position
        upperIdx = self.bsearch(intervals, newInterval)
        intervals.insert(upperIdx, newInterval)
        # merge the intervals
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged

    # upper bound binary search
    def bsearch(self, intervals, target):
        left = 0
        right = len(intervals)
        while left < right:
            mid = (left + right)/2
            if target[0] >= intervals[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
