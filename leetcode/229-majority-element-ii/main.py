"""
    1st approach: hashtable

    Time    O(2n)
    Space   O(n)
    104 ms, faster than 73.23%
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        res = []
        for key in m:
            if m[key] > len(nums)//3:
                res.append(key)
        return res
