"""
    2nd many binary searches LOL
    
	Time O(RlogC)
	144 ms, faster than 25.63% 
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            arr = matrix[i]
            if self.bsearch(arr, target):
                return True
        return False

    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
