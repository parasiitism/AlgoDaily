"""
    1st approach: binary search + hashtable
    - sort the intervals (remember the original index by appending to the end, or create a class)
    - for each sorted interval, binary search to find the interval which start >= end
    - using a hashtable to cache the result such that we can construct the result

    Time    O(nlogn)
    Space   O(n)
    360 ms, faster than 22.68%
"""


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        nodes = []
        for i in range(len(intervals)):
            # start, end, index
            temp = (intervals[i][0], intervals[i][1], i)
            nodes.append(temp)
        # sort by start time
        nodes = sorted(nodes, key=lambda x: x[0])
        # since question said that there will be no duplicate start
        m = {}
        for i in range(len(nodes)):
            x, y, z = nodes[i]
            key = str(x) + ',' + str(y)
            if i+1 == len(nodes):
                m[key] = -1
            else:
                idx = self.upperBSearch(nodes, y) - 1
                # find the interval which the start point is >= target endpoint
                if nodes[idx][0] < y:
                    idx += 1
                # check if found index is within the boundary
                if idx < len(nodes):
                    m[key] = nodes[idx][2]
                else:
                    m[key] = -1
        res = []
        for x, y in intervals:
            key = str(x) + ',' + str(y)
            res.append(m[key])
        return res

    def upperBSearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return left
