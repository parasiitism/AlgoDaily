"""
    1st approach: dynamic programming
    
    Time    O(n)
    Space   O(n)
    16 ms, faster than 89.83%
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        included = [0] * len(nums)
        excluded = [0] * len(nums)
        included[0] = nums[0]
        for i in range(1, len(nums)):
            included[i] = max(
                excluded[i-1]+nums[i],
                included[i-1]
            )
            excluded[i] = included[i-1]
        return included[-1]


"""
    2nd approach: dynamic programming
    
    Time    O(n)
    Space   O(1)
    16 ms, faster than 89.83%
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        included = nums[0]
        excluded = 0
        for i in range(1, len(nums)):
            temp = included
            included = max(excluded+nums[i], included)
            excluded = temp
        # return included
        return max(included, excluded)
