"""
    1st approach: hashtable

    Time    O(n+n+o) n: nums, n: unique chracters, o: averge freq of characters
    Space   O(n)
    212 ms, faster than 62.66%
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # put indeces into a hashtable
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in m:
                m[num] = [i]
            else:
                m[num].append(i)
        # get the max freq as well as its corresponding arrays
        # becos it is possible that there are no than 1 num having the maxFreq
        maxFreq = 0
        maxArrs = []
        for key in m:
            if len(m[key]) > maxFreq:
                maxFreq = len(m[key])
                maxArrs = [m[key]]
            elif len(m[key]) == maxFreq:
                maxArrs.append(m[key])
        # get the result
        res = sys.maxsize
        for arr in maxArrs:
            l = arr[-1] - arr[0] + 1
            res = min(res, l)
        return res
