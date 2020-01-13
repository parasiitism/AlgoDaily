"""
    very bad description

    Time    O(N)
    Space   O(N)
    56 ms, faster than 68.38% 
"""
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums) // 2):
            a = nums[2*i]
            b = nums[2*i+1]
            result += a * [b]
        return result