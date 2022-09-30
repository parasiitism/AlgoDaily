"""
    2 pointers

    e.g.1
    [4,3,2,1,2,3,1] -> [4, 3, 2, 3, None, 4, None]

    e.g.2
    [1,2,3,4] -> [None, None, 10, None]
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n-1
        res = 0
        while L <= R:
            if nums[L] == nums[R]:
                L += 1
                R -= 1
            elif nums[L] < nums[R]:
                nums[L+1] += nums[L]
                nums[L] = None
                L += 1
                res += 1
            elif nums[L] > nums[R]:
                nums[R-1] += nums[R]
                nums[R] = None
                R -= 1
                res += 1
        # print(nums)
        return res
