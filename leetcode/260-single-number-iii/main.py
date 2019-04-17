"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    48ms beats 42.29%
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ht = {}
        for num in nums:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
        res = []
        for key in ht:
            if ht[key] == 1:
                res.append(key)
        return res
