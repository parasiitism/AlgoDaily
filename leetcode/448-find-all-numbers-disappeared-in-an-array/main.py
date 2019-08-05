"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    320 ms, faster than 83.63%
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in m:
                res.append(i)
        return res
