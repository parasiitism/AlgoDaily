"""
    1st approach: hashtable

    Time  O(n)
    Space O(n)
    40 ms, faster than 66.68%
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            num = nums[i]
            remain = target - num
            if remain in ht:
                return [ht[remain], i]
            else:
                ht[num] = i
        return []
