"""
    1st approach
    - sort the array
    - create an array of meeting rooms
    - each interval, compare the last meeting(since sorted) amongst the meeting in the meeting rooms
    - if there is no collision, put the meeting in that room, else create a new meeting room for the interval
    
    Time		O(nlogn) sort
    Space 	O(n)	result array
    84 ms, faster than 16.12%
"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0

        def cptr(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intervals = sorted(intervals, cmp=cptr)

        rooms = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            found = False
            for j in range(len(rooms)):
                room = rooms[j]
                if room[1] <= cur[0]:
                    rooms[j] = cur
                    found = True
                    break
            if found == False:
                rooms.append(cur)
        return len(rooms)
