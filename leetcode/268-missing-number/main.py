class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        supposed = n*(n+1)/2
        total = sum(nums)
        return supposed - total
