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
