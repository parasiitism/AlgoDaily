from typing import List

"""
    1st: 2 pointers

    Time    O(N)
    Space   O(1)
"""
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        con_val = 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if i < j:
                left = nums[i]
                right = nums[j]
                con_val += int(str(left) + str(right))
                i += 1
                j -= 1
            else:
                con_val += nums[i]
                i += 1
        return con_val