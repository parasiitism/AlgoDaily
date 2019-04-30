"""
    1st approach
    - sort the array, compare the item[i].start and item[i-1].end
    - takeaway: use sort.slice() to sort a list of structs https:godoc.org/sort#Slice
    Time		O(nlogn)
    Space	  O(1)
    80 ms, faster than 13.44%
"""


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def cptr(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cptr)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = intervals[i-1]
            if cur[0] < prev[1]:
                return False
        return True
