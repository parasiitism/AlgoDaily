"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    100 ms, faster than 90.95%
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hs = set()
        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False
