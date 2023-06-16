"""
    sort
    - sort every row, and then sum up the max value column by column

    Time    O(RC * RlogR + RC)
    Space   O(1)
"""


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        R, C = len(nums), len(nums[0])
        res = 0
        for j in range(C):
            max_col = 0
            for i in range(R):
                max_col = max(max_col, nums[i][j])
            res += max_col
        return res
