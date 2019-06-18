"""
    1st approach: hashtable

    Time    O(2n)
    Space   O(n)
    156 ms, faster than 60.47% 
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        maxCnt = 0
        res = -1
        for key in m:
            if m[key] > maxCnt:
                maxCnt = m[key]
                res = key
        return res
